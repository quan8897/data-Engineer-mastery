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
