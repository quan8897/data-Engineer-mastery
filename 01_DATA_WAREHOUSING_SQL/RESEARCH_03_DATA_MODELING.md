# 🛡️ NGHIÊN CỨU TASK 3: DATA MODELING NÂN CAO (STAR VS SNOWFLAKE & SCD)

> **Giao thức học tập (Feynman Technique):** Anh hãy tự nghiên cứu và trả lời các câu hỏi dưới đây bằng ngôn ngữ của chính mình. Có thể tham khảo cuốn **[THE_DATA_WAREHOUSE_TOOLKIT.md](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/01_DATA_WAREHOUSING_SQL/THE_DATA_WAREHOUSE_TOOLKIT.md)** (Chương 2 và 5) để có căn cứ lý thuyết chuẩn mực.

---

## ❓ TRỰC GIÁC BAN ĐẦU (Trả lời trước khi đọc tài liệu)
*   **Câu hỏi:** Tưởng tượng thông tin địa chỉ thường trú của công dân trên CCCD thay đổi. Sự khác biệt cốt lõi trong cách lưu trữ lịch sử của SCD Type 1, Type 2, và Type 3 là gì? Nếu là Cơ sở dữ liệu quốc gia, anh chọn Type nào để quản lý hộ khẩu/thường trú? Tại sao?
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*

---

## 📘 PHẦN 1: BẢN VẼ HỆ THỐNG (STAR VS SNOWFLAKE SCHEMA)

*   **Câu hỏi 1.1:** Phân biệt sự khác biệt cốt lõi giữa mô hình Sao (Star Schema) và mô hình Bông tuyết (Snowflake Schema).
*   **Câu hỏi 1.2:** Dưới góc độ hiệu năng truy vấn (Query Performance) và tính dễ dùng đối với các nhà phân tích (User Usability):
    - Tại sao Star Schema lại là lựa chọn mặc định của đa số Kho dữ liệu?
    - Việc "Chuẩn hóa" (Normalize) các bảng Dimension trong Snowflake Schema nhằm tiết kiệm dung lượng đĩa có thực sự còn quan trọng trong thời đại lưu trữ đám mây giá rẻ ngày nay?
*   **Trả lời của anh:**
    1. Về hình dáng: 
       - **Star Schema (Phi chuẩn hóa):** Dữ liệu Dimension được gom hết vào 1 bảng duy nhất (bị lặp lại dữ liệu). Xung quanh Fact table chỉ có 1 lớp Dimension.
       - **Snowflake Schema (Chuẩn hóa):** Bảng Dimension bị chia nhỏ tiếp thành các bảng Dimension con để tránh lặp dữ liệu (ví dụ: bảng Sản phẩm nối sang bảng Loại Sản Phẩm).
    2. Về hiệu năng và tính dễ dùng:
       - Các Data Analyst rất ghét Snowflake vì muốn lấy đủ thông tin phải viết lệnh `JOIN` quá nhiều bảng, vừa phức tạp vừa dễ sai.
       - Star Schema có tốc độ truy vấn nhanh hơn vì ít phải `JOIN`.
       - Trong thời đại Cloud hiện tại (lưu trữ S3, ổ cứng rẻ), việc tiết kiệm dung lượng đĩa của Snowflake không còn ý nghĩa. Đổi lại, việc bắt CPU phải xử lý hàng đống lệnh `JOIN` (Compute) lại vô cùng đắt đỏ. Vì vậy Star Schema luôn thắng trong Analytics.
    
    **3. Thiết kế Star Schema cho hệ thống BHXH:**
    - Bảng trung tâm: `fact_chi_tra`
      + `id_cong_dan` (Khóa ngoại)
      + `id_thoi_gian` (Khóa ngoại)
      + `id_dia_phuong` (Khóa ngoại)
      + `id_loai_tro_cap` (Khóa ngoại)
      + `tong_chi_tra` (Con số đo lường - LƯU Ý: Không dùng SUM() trong cấu trúc bảng, SUM chỉ dùng khi viết query SQL).

---

## 🥈 PHẦN 2: QUẢN LÝ LỊCH SỬ THAY ĐỔI (SLOWLY CHANGING DIMENSIONS - SCD)

*   **Tình huống:** Công dân Nguyễn Văn A thay đổi địa chỉ thường trú từ *Tỉnh Hải Dương* sang *Thành phố Hà Nội* vào ngày 01/07/2026.
*   **Câu hỏi 2.1:** Hãy điền vào bảng dưới đây cách các Type của SCD xử lý sự thay đổi này:

| Loại SCD | Cách lưu trữ dòng dữ liệu mới | Dòng dữ liệu cũ biến đi đâu? | Khi truy vấn doanh thu giao dịch của Nguyễn Văn A trong năm 2025, báo cáo sẽ ghi nhận địa chỉ của anh A ở đâu? |
| :--- | :--- | :--- | :--- |
| **Type 1** | Ghi đè địa chỉ mới là "Thành phố Hà Nội" lên chính dòng hiện tại | Bị xóa vĩnh viễn (Mất lịch sử cư trú ở Hải Dương) | Ra kết quả là "Hà Nội" (Sai lệch lịch sử vì năm 2025 A ở Hải Dương) |
| **Type 2** | Thêm 1 dòng Dimension hoàn toàn mới với địa chỉ "Hà Nội", có cột `start_date` là 01/07/2026 | Dòng cũ vẫn giữ nguyên, nhưng cột `end_date` được cập nhật thành 30/06/2026 và đánh dấu `is_active = false` | Ra kết quả là "Hải Dương" (Bảo toàn lịch sử 100% hoàn hảo) |
| **Type 3** | Thêm một cột mới (VD: `previous_address`) để chứa giá trị cũ, cột `current_address` cập nhật thành "Hà Nội" | Nằm ở cột `previous_address` (Nhưng chỉ lưu được 1 lần thay đổi gần nhất) | Rất rủi ro. Nếu A chuyển nhà 3 lần, lịch sử năm 2025 sẽ bị mất hoàn toàn vì Type 3 chỉ giữ được 1 giá trị cũ. |

*   **Câu hỏi 2.2:** Đối với hệ thống CSDL Quốc gia (như BHXH, Thuế), tại sao **SCD Type 2** gần như là bắt buộc? Nếu dùng SCD Type 1 cho địa chỉ thường trú của công dân, thảm họa kiểm toán (Audit Disaster) nào sẽ xảy ra khi ta cần đối chiếu chi trả trợ cấp của các địa phương trong lịch sử?
*   **Trả lời của anh:**
    Nếu dùng SCD Type 1, bảng Dimension chỉ còn lưu địa chỉ mới nhất (Hà Nội). Những giao dịch nhận tiền trợ cấp thực tế xảy ra năm 2024 tại Hải Dương vẫn còn trong bảng Fact, nhưng khi JOIN với bảng Dimension hiện tại, các giao dịch đó sẽ bị tính nhầm cho Hà Nội.
    **Hậu quả:** Số tiền chi trả của Hải Dương trên báo cáo sẽ bị **THẤP HƠN** thực tế (vì bị mất những người đã chuyển đi). Số tiền của Hà Nội sẽ bị **CAO HƠN** thực tế. Gây ra thảm họa sai lệch số liệu kiểm toán.

---

## 🔑 PHẦN 3: BẢN CHẤT CỦA KHÓA THAY THẾ (SURROGATE KEYS)

*   **Câu hỏi 3.1:** Tại sao Kimball khuyên ta tuyệt đối **không được** dùng khóa tự nhiên (Natural Key - ví dụ: Số CCCD, Mã số thuế) làm Khóa chính (Primary Key) trong các bảng Dimension của Kho dữ liệu, mà bắt buộc phải dùng Khóa thay thế (Surrogate Key - ví dụ: Số nguyên tự tăng 1, 2, 3...)?
*   **Câu hỏi 3.2:** Khóa thay thế (Surrogate Key) giúp ta giải quyết bài toán lưu trữ nhiều phiên bản lịch sử (SCD Type 2) của cùng một số CCCD trong bảng Dimension như thế nào?
*   **Trả lời của anh:**
    Kimball bắt buộc dùng Khóa thay thế (Surrogate Key) thay vì Khóa tự nhiên (Natural Key) vì 3 lý do cốt lõi:
    1. **Bảo toàn quy tắc Khóa chính trong SCD Type 2 (Quan trọng nhất):** Bảng Dimension dùng SCD Type 2 sẽ chứa NHIỀU dòng cho cùng 1 số CCCD (mỗi dòng tương ứng một giai đoạn lịch sử). Nếu lấy CCCD làm Khóa chính, thao tác `INSERT` dòng lịch sử thứ 2 sẽ báo lỗi trùng lặp (Primary Key Violation). Surrogate Key (1, 2, 3...) giúp mỗi dòng có một định danh độc nhất.
    2. **Hiệu năng truy vấn (Performance):** Khóa tự nhiên thường là chuỗi văn bản (String/VARCHAR) dài (như CCCD 12 số). Việc CPU thực hiện hàng tỷ phép `JOIN` trên kiểu dữ liệu Chuỗi sẽ chậm và tốn RAM hơn rất nhiều so với `JOIN` trên số nguyên (Integer) của Surrogate Key.
    3. **Cách ly khỏi biến động của hệ thống gốc:** Khóa tự nhiên hoàn toàn có thể bị thay đổi ở thế giới thực (ví dụ: Nhà nước nâng cấp CMND 9 số lên CCCD 12 số). Nếu dùng nó làm PK trong Kho dữ liệu, ta sẽ phải UPDATE hàng tỷ dòng Fact cũ để đồng bộ. Surrogate Key giúp Kho dữ liệu miễn nhiễm với những biến động này.

---

## 🛠️ PHẦN THỰC HÀNH: SQL THIẾT KẾ SCD TYPE 2
```sql
CREATE TABLE dim_citizen (
    id_cong_dan INT AUTO_INCREMENT PRIMARY KEY,  -- Surrogate Key (Khóa thay thế)
    so_cccd VARCHAR(12) NOT NULL,                -- Natural Key (Khóa tự nhiên)
    ho_ten VARCHAR(100),
    dia_chi VARCHAR(255),
    
    -- Các cột theo dõi lịch sử chuẩn SCD Type 2
    start_date DATE NOT NULL,                    -- Ngày bắt đầu hiệu lực của dòng này
    end_date DATE,                               -- Ngày hết hạn (NULL hoặc 9999-12-31 nếu là hiện tại)
    is_active BOOLEAN NOT NULL                   -- TRUE nếu là dòng địa chỉ mới nhất
);
```
