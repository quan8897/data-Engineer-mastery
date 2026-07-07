# 🛡️ NGHIÊN CỨU TASK 2: WINDOW FUNCTIONS (SQL NÂNG CAO)

> **Giao thức học tập (Feynman Technique):** Anh hãy tự nghiên cứu và trả lời các câu hỏi dưới đây bằng ngôn ngữ của chính mình (có thể kết hợp chèn từ khóa tiếng Anh chuyên ngành vào ngoặc đơn).

---

## ❓ TRỰC GIÁC BAN ĐẦU (Trả lời trước khi đọc tài liệu)
*   **Câu hỏi:** Theo trực giác kỹ sư của anh — tại sao `SUM() OVER()` vừa tính tổng dữ liệu mà lại vừa không làm mất (gộp) các dòng chi tiết như `GROUP BY`? Cơ chế hoạt động bên dưới của SQL Engine ở đây khác gì so với `GROUP BY`?
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*
    - SUM() OVER() có cơ chế hoạt động khác, chúng gom nhóm nhưng tạo bổ sung thêm một cột không làm mất các dòng dữ liệu ban đầu, còn group by là gom nhóm và database tự động tính tổng số này theo nhóm dữ liệu đã được gom
GROUP BY:

Gom các dòng lại → mất dữ liệu chi tiết.

OVER():

Nhìn các dòng như một "cửa sổ", tính toán trên cửa sổ đó → giữ nguyên tất cả các dòng, chỉ thêm kết quả tính toán.
---

## 📘 PHẦN 1: BẢN CHẤT CỦA "CỬA SỔ" (WINDOW)
So sánh hai câu lệnh sau:
```sql
-- Câu lệnh A (GROUP BY)
SELECT quy, SUM(doanh_so) 
FROM fact_sales 
GROUP BY quy;

-- Câu lệnh B (WINDOW FUNCTION)
SELECT tinh_id, quy, doanh_so, SUM(doanh_so) OVER (PARTITION BY quy)
FROM fact_sales;
```

*   **Câu hỏi 1.1:** Phân biệt sự khác biệt cốt lõi về kết quả đầu ra (output rows) giữa hai câu lệnh trên. câu lệnh A kết quả sẽ gom nhóm theo quý, các dòng ban đầu sẽ bị mất
*   **Câu hỏi 1.2:** Dùng một ẩn dụ (ví dụ: chiếc kính lúp, khung cửa sổ, hay máy quét...) để giải thích từ `OVER` (cửa sổ) trong SQL nghĩa là gì? kết quả sẽ giữ nguyên các hàng ban đầu và bổ dung 1 cột tính toán doanh số theo Quý, chúng người xem xác định được từng quý có sự thay đổi như thế nào so với quý trước, và chiếm tỷ lệ như nào với số tổng
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*

---

## 🥈 PHẦN 2: BỘ BA XẾP HẠNG (RANKING)
Anh cần xếp hạng doanh số các tỉnh trong từng quý để trao thưởng. Hãy phân tích sự khác nhau giữa `ROW_NUMBER()`, `RANK()`, và `DENSE_RANK()`.

*   **Tình huống:** Giả sử Quý 1 có doanh số của 3 tỉnh như sau:
    *   Tỉnh A: 100 triệu
    *   Tỉnh B: 100 triệu
    *   Tỉnh C: 80 triệu
*   **Câu hỏi 2.1:** Kết quả xếp hạng (hạng của Tỉnh A, B, C) sẽ như thế nào đối với mỗi hàm? Điền vào bảng dưới đây:

| Tỉnh | Doanh số | ROW_NUMBER() | RANK() | DENSE_RANK() |
| :--- | :--- | :--- | :--- | :--- |
| A | 100tr | 1| 1|1 |
| B | 100tr | 2| 1| 1|
| C | 80tr | 3| 3| 2|
ROW_NUMBER() → Mỗi dòng một số, không quan tâm trùng.
RANK() → Có đồng hạng, hạng sau bị nhảy số.
DENSE_RANK() → Có đồng hạng, không nhảy số.
*   **Câu hỏi 2.2:** Nếu chính sách quốc gia yêu cầu **"Trao thưởng cho tất cả các tỉnh nằm trong Top 2 doanh số"**, dùng sai hàm nào sẽ khiến Tỉnh C bị mất cơ hội nhận thưởng một cách oan ức? Tại sao?
*   **Trả lời của anh:**
    *(Viết câu trả lời của anh tại đây)*
dùng row_number hoặc rank () sẽ khiến tỉnh C bị mất cơ hội nhận thưởng  vì row_number đánh số theo thứ tự không có trùng nhau và không quan tâm đến giá trị doanh số, rank () có đánh giá theo doanh số tuy nhiên hàng sau bị nhảy số nên tỉnh C bị mất cơ hội nhận thưởng
---

## ⏳ PHẦN 3: CỖ MÁY THỜI GIAN (LAG & LEAD)
Để tính toán tỷ lệ tăng trưởng doanh số của từng tỉnh so với quý trước, ta cần lấy dữ liệu của quý trước đặt cạnh dữ liệu của quý này.

*   **Câu hỏi 3.1:** Hàm `LAG()` và `LEAD()` dùng để làm gì? Sự khác nhau giữa chúng là gì? lag lấy dữ liệu từ các hàng phía trước, lead lấy dữ liệu từ các hàng phía sau
cú pháp:
LAG(cột_cần_lấy [, offset] [, giá_trị_mặc_định]) OVER (PARTITION BY nhóm ORDER BY cột_sắp_xếp)
LEAD(cột_cần_lấy [, offset] [, giá_trị_mặc_định]) OVER (PARTITION BY nhóm ORDER BY cột_sắp_xếp)

*   **Câu hỏi 3.2:** Viết một đoạn mã giả SQL (pseudo-SQL) sử dụng hàm `LAG()` để lấy ra doanh số quý trước (`doanh_so_quy_truoc`) đặt bên cạnh doanh số quý này (`doanh_so_quy_nay`) của từng tỉnh (chia nhóm theo `tinh_id` và sắp xếp theo `quy`).
*   **Trả lời của anh:**
    ```sql
    with ds_3 as (
        select tinh_id, quy, sum(doanh_so) as tong_doanh_so_tinh_theo_quy
        from fact_sales
        group by tinh_id, quy
    ),
    ds_4 as (
        select tinh_id, quy, tong_doanh_so_tinh_theo_quy,
        lag (tong_doanh_so_tinh_theo_quy, 1, null) over (partition by tinh_id order by quy) as Doanh_so_quy_truoc
        from ds_3
    )
    select *,
    ((tong_doanh_so_tinh_theo_quy - Doanh_so_quy_truoc) / Doanh_so_quy_truoc) * 100 as ty_le_tang_truong_doanh_so
    from ds_4;
    ```

---

## ⚡ TÓM TẮT LAB THỰC CHIẾN & PHÂN TÍCH BIÊN
1. **Sự khác biệt của ORDER BY trong OVER():**
   - Khi không có `ORDER BY`, cửa sổ mặc định là toàn bộ phân vùng (tổng tĩnh).
   - Khi có `ORDER BY`, cửa sổ mặc định co lại thành từ dòng đầu tiên đến dòng hiện tại (tổng lũy kế / running total).
   - Nếu `ORDER BY` theo một trường bị trùng lặp (ví dụ `tinh_id`), SQL Engine (sử dụng `RANGE` mặc định) sẽ cộng gộp tất cả các dòng trùng giá trị xếp hạng lại rồi mới thực hiện lũy kế.

2. **Xử lý NULL vs 0 trong bài toán tăng trưởng:**
   - Sử dụng `LAG(..., 1, 0)` dẫn đến phép chia cho 0 (`/ 0`) sinh ra lỗi `NaN` ở SQLite hoặc làm **treo hệ thống** (Division by zero) trên PostgreSQL/SQL Server.
   - Sử dụng `LAG(..., 1, NULL)` (hoặc không truyền tham số mặc định) khiến phép toán với `NULL` tự động trả về `NULL`. Điều này an toàn hơn và giúp các hàm tính toán trung bình (`AVG`) sau đó không bị lệch mẫu số.

3. **Bảo vệ dữ liệu khỏi lỗi nhảy quý (Data Gap):**
   - Để tránh việc so sánh sai khi một quý bị mất (ví dụ so sánh Q3 với Q1 do mất Q2):
   - Ta sử dụng kỹ thuật tính toán khoảng cách quý:
     ```sql
     CASE 
         WHEN (CAST(SUBSTR(quy, 2) AS INT) - CAST(SUBSTR(lag_quy, 2) AS INT)) = 1 
         THEN ((nay - truoc) / truoc) * 100
         ELSE NULL 
     END
     ```


Kịch bản 1 — Bẫy "Lũy kế" (Running Total):
Trong SQL, hai câu lệnh sau chỉ khác nhau duy nhất mệnh đề ORDER BY bên trong OVER():

Câu lệnh 1: SUM(doanh_so) OVER (PARTITION BY quy)
Câu lệnh 2: SUM(doanh_so) OVER (PARTITION BY quy ORDER BY ngay_giao_dich)
Câu hỏi 1: Kết quả trả về của Câu lệnh 2 khác gì so với Câu lệnh 1? Mệnh đề ORDER BY đã vô tình thay đổi khung cửa sổ mặc định (Default Window Frame) của SQL Engine như thế nào?
- câu lệnh 2 kết quả trả ra được sắp xếp theo thứ tự ngày so với kết quả thứ 1 sắp xếp ko theo thứ tự
Kịch bản 2 — Giá trị 0 vs NULL (Tính toàn vẹn dữ liệu):
Trong đoạn code của anh: lag(doanh_so, 1, 0).

Câu hỏi 2: Trong thiết kế Kho dữ liệu cấp quốc gia, tại sao việc điền mặc định là 0 thay vì để nguyên NULL cho dòng đầu tiên đôi khi lại cực kỳ nguy hiểm? Sự khác biệt giữa "Tỉnh đó không có hoạt động kinh doanh (doanh số thực sự bằng 0)" và "Tỉnh đó chưa được thành lập hoặc chưa có dữ liệu báo cáo (NULL)" sẽ ảnh hưởng như thế nào đến các báo cáo thống kê (như tính trung bình AVG doanh số qua các quý)?