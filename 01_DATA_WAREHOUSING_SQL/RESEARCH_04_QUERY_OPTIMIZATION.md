# RESEARCH 04: QUERY OPTIMIZATION (TỐI ƯU HÓA TRUY VẤN)

## 📘 PHẦN 1: INDEX VÀ FULL TABLE SCAN

*   **Câu hỏi 1.1:** So sánh Full Table Scan (O(n)) và Index Scan (O(log n)). Hãy dùng ví dụ "Cuốn từ điển" để giải thích cho một người không biết IT hiểu cách B-Tree Index hoạt động.
*   **Câu hỏi 1.2:** Tại sao Index giúp lệnh `SELECT` chạy siêu tốc, nhưng lại là "kẻ thù" của lệnh `INSERT` / `UPDATE`? Dựa vào Trade-off này, tại sao Kho dữ liệu (Data Warehouse) lại cho phép tạo rất nhiều Index, còn Database Vận hành (OLTP) thì phải cực kỳ dè dặt?
*   **Trả lời của anh:**
    **1. Về bản chất của Index (Ví dụ cuốn từ điển):**
    - **Full Table Scan (O(n)):** Giống như việc bạn lật từ trang 1, dò từng dòng, từng chữ một cho đến khi tìm thấy từ "Data" ở trang 500. Rất thô sơ và chậm chạp.
    - **Index Scan (O(log n)):** Giống như việc bạn nhìn vào các tab chữ cái (A, B, C, D...) ở mép cuốn từ điển, lật ngay đến phần chữ "D", tìm tiếp chữ "Da"... rồi lập tức tra ra chữ "Data". 
    - **Bản chất của Index:** Là việc database tạo ra một "mục lục" (cấu trúc cây B-Tree) được **sắp xếp theo thứ tự**. Khi tìm kiếm, nó không cần đọc dữ liệu gốc, mà lướt trên cái mục lục này để lấy "số trang" (pointer) rồi nhảy nhảy cóc đến đúng dòng dữ liệu.

    **2. Cái giá phải trả (Trade-off) của Index:**
    - Khi có lệnh `INSERT/UPDATE`, Database không chỉ ghi dữ liệu vào bảng chính, mà còn phải chạy vào "Mục lục" để tìm đúng vị trí, chèn thêm từ mới vào, và đẩy các từ khác sang một bên để giữ đúng thứ tự bảng chữ cái (rebalance B-Tree). Điều này tốn rất nhiều tài nguyên Disk I/O. 1 lệnh `INSERT` vào bảng có 5 Index thực chất là 6 lệnh `INSERT` ngầm định.
    - **OLTP (Vận hành):** Cần tốc độ Ghi (`INSERT`) siêu nhanh (hàng ngàn giao dịch/giây). Nếu tạo nhiều Index, hệ thống sẽ bị thắt cổ chai khi ghi. Do đó, OLTP cực kỳ dè dặt tạo Index.
    - **OLAP (Data Warehouse):** Dữ liệu thường được đẩy vào (Load) một lần vào ban đêm bằng Bulk Insert. Ban ngày, hệ thống hoàn toàn chỉ nhận lệnh Đọc (`SELECT`) từ các báo cáo. Do tính chất "Ghi 1 lần, Đọc triệu lần", Data Warehouse thoải mái đắp hàng tá Index để phục vụ tốc độ truy vấn báo cáo.

---

## 🛠️ PHẦN 2: THỰC HÀNH EXPLAIN QUERY PLAN
Khi chạy lệnh `EXPLAIN QUERY PLAN` để xem xét kế hoạch thực thi của Database:
1. **Khi KHÔNG CÓ Index:** Database sẽ báo cáo hành động `SCAN TABLE` (Quét toàn bảng). Tức là nó phải chạy qua từng dòng một (từ dòng 1 đến dòng 10 triệu) để tìm ra kết quả.
2. **Khi CÓ Index:** Database sẽ báo cáo hành động `SEARCH TABLE USING INDEX` (Tìm qua chỉ mục). Nó sẽ dùng cấu trúc B-Tree để nhảy thẳng vào đúng địa chỉ chứa ID "Hà Nội" cực kỳ nhanh chóng.

**Kết luận qua Toán học (O(n) vs O(log n)):**
Với một bảng Fact có 1 tỷ (1,000,000,000) dòng:
- Nếu dùng **Full Table Scan O(n)**: Phải đọc qua 1 tỷ dòng.
- Nếu dùng **Index B-Tree O(log n)**: Chỉ mất tối đa **30 bước** (vì $log_2(1,000,000,000) \approx 30$).
Sự chênh lệch giữa 1.000.000.000 và 30 là sức mạnh tuyệt đối của Index. Do đó trong Star Schema, bắt buộc phải đắp Index lên các cột **Khóa ngoại (Foreign Key)** nối về Dimension, vì đây là những cột bị `JOIN` và `WHERE` liên tục nhất.

---

## 📂 PHẦN 3: PARTITIONING (CHIA NHỎ DỮ LIỆU)

*   **Câu hỏi 3.1:** Phân biệt Range Partition và List Partition. Nêu một ví dụ thực tế cho mỗi loại.
*   **Câu hỏi 3.2:** Khái niệm "Partition Pruning" (Tỉa nhánh) là gì? Nó giúp tiết kiệm chi phí tính toán như thế nào?
*   **Trả lời của anh:**
    **1. Phân biệt các loại Partition:**
    - **Range Partition (Theo khoảng):** Giống như chia dữ liệu theo khoảng thời gian (ví dụ: 2001-2010, 2011-2020, 2021-nay).
    - **List Partition (Theo danh sách):** Phân chia theo một danh sách giá trị cố định (ví dụ: giới tính, năm sinh, danh sách 63 tỉnh/thành phố). Các giá trị này thường ít biến động.

    **2. Partition Pruning (Tỉa nhánh):**
    - Là cơ chế giúp hệ thống truy xuất **chính xác** đến đúng phân vùng (ngăn kéo) cần tính toán (ví dụ: chỉ mở thư mục dữ liệu năm 2024).
    - Lợi ích: Thay vì phải load và truy vấn toàn bộ cơ sở dữ liệu (tất cả các năm), hệ thống bỏ qua (tỉa) toàn bộ những dữ liệu không liên quan. Trên các hệ thống Cloud như BigQuery hay Snowflake (tính tiền dựa trên số Byte dữ liệu được quét), cơ chế này trực tiếp giúp **tiết kiệm hàng ngàn đô la**.
    **3. Code SQL tạo bảng Partition (PostgreSQL):**
    ```sql
    -- Tạo bảng định tuyến (Bảng mẹ)
    CREATE TABLE fact_giao_dich_partitioned ( 
        id INT, 
        so_tien INT, 
        ngay_giao_dich DATE
    ) PARTITION BY RANGE (ngay_giao_dich);

    -- Tạo các phân vùng vật lý (Bảng con)
    CREATE TABLE fact_giao_dich_2023 PARTITION OF fact_giao_dich_partitioned
        FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

    CREATE TABLE fact_giao_dich_2024 PARTITION OF fact_giao_dich_partitioned
        FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

    CREATE TABLE fact_giao_dich_2025 PARTITION OF fact_giao_dich_partitioned
        FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');

    CREATE TABLE fact_giao_dich_2026 PARTITION OF fact_giao_dich_partitioned
        FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');
    ```

    **4. Sức mạnh của Partition Pruning:**
    - Khi truy vấn dữ liệu năm 2024 trên bảng 1 tỷ dòng (5 năm, mỗi năm 200 triệu), hệ thống chỉ mở **duy nhất 1 ngăn kéo** (2024).
    - Nó chỉ phải quét **200 triệu dòng** thay vì 1 tỷ dòng, giúp **tiết kiệm được việc quét vô ích 800 triệu dòng**.
    - **Combo Hoàn Hảo (Partition + Index):** Partition hoạt động ở cấp độ vĩ mô (chặt file lớn thành file nhỏ). Khi kết hợp với Index (B-Tree cấp độ dòng), ta có kịch bản hoàn hảo: Partition giúp loại bỏ 800 triệu dòng không liên quan, sau đó Index giúp tìm kiếm cực nhanh bên trong 200 triệu dòng còn lại. Tốc độ sẽ nhanh gấp hàng vạn lần.
