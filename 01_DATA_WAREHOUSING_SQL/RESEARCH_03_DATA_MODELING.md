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
    *(Viết câu trả lời của anh tại đây)*

---

## 🥈 PHẦN 2: QUẢN LÝ LỊCH SỬ THAY ĐỔI (SLOWLY CHANGING DIMENSIONS - SCD)

*   **Tình huống:** Công dân Nguyễn Văn A thay đổi địa chỉ thường trú từ *Tỉnh Hải Dương* sang *Thành phố Hà Nội* vào ngày 01/07/2026.
*   **Câu hỏi 2.1:** Hãy điền vào bảng dưới đây cách các Type của SCD xử lý sự thay đổi này:

| Loại SCD | Cách lưu trữ dòng dữ liệu mới | Dòng dữ liệu cũ biến đi đâu? | Khi truy vấn doanh thu giao dịch của Nguyễn Văn A trong năm 2025, báo cáo sẽ ghi nhận địa chỉ của anh A ở đâu? |
| :--- | :--- | :--- | :--- |
| **Type 1** | | | |
| **Type 2** | | | |
| **Type 3** | | | |

*   **Câu hỏi 2.2:** Đối với hệ thống CSDL Quốc gia (như BHXH, Thuế), tại sao **SCD Type 2** gần như là bắt buộc? Nếu dùng SCD Type 1 cho địa chỉ thường trú của công dân, thảm họa kiểm toán (Audit Disaster) nào sẽ xảy ra khi ta cần đối chiếu chi trả trợ cấp của các địa phương trong lịch sử?
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*

---

## 🔑 PHẦN 3: BẢN CHẤT CỦA KHÓA THAY THẾ (SURROGATE KEYS)

*   **Câu hỏi 3.1:** Tại sao Kimball khuyên ta tuyệt đối **không được** dùng khóa tự nhiên (Natural Key - ví dụ: Số CCCD, Mã số thuế) làm Khóa chính (Primary Key) trong các bảng Dimension của Kho dữ liệu, mà bắt buộc phải dùng Khóa thay thế (Surrogate Key - ví dụ: Số nguyên tự tăng 1, 2, 3...)?
*   **Câu hỏi 3.2:** Khóa thay thế (Surrogate Key) giúp ta giải quyết bài toán lưu trữ nhiều phiên bản lịch sử (SCD Type 2) của cùng một số CCCD trong bảng Dimension như thế nào?
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*
