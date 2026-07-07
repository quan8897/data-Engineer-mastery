# 📦 MỤC LỤC MODULE 01: DATA WAREHOUSING & SQL MASTERY

> **Mục tiêu:** Nắm vững tư duy thiết kế Kho Dữ liệu (Data Warehouse) và SQL từ cơ bản đến nâng cao. Đây là kỹ năng cốt lõi phân biệt một Data Engineer với một lập trình viên thông thường.

---

## ✅ Task đã hoàn thành

### Task 1: Nền tảng Data Warehouse & SQL Cơ bản
- **Khái niệm cốt lõi đã nắm:**
  - OLTP vs OLAP — Bản chất khác biệt về mục đích và cấu trúc
  - Star Schema — Fact Table & Dimension Tables
  - Thứ tự thực thi SQL: `FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`
- **SQL đã thành thạo:**
  - `SELECT`, `FROM`, `JOIN ... ON`
  - `WHERE` — Lọc hàng thô (trước GROUP BY)
  - `GROUP BY` + `SUM()` — Gom nhóm và tính tổng
  - `HAVING` — Lọc sau khi đã gom nhóm
  - `ORDER BY DESC/ASC` — Sắp xếp kết quả
  - `LIMIT` — Giới hạn số dòng trả về

---
- ôn tập ngày 30/6/2026:
### Tình huống:
Hệ thống BHXH quốc gia có hai nhu cầu xử lý dữ liệu sau:

## Yêu cầu A: 
Người dân quét mã QR tại quầy để nhận tiền trợ cấp thất nghiệp. Hệ thống phải ghi nhận giao dịch, trừ số dư và phản hồi trong vòng 100ms để tránh lỗi trùng lặp.
## Yêu cầu B: 
Cuối năm, Bộ trưởng yêu cầu báo cáo tổng số tiền đã chi trả trợ cấp thất nghiệp của 63 tỉnh thành trong 5 năm qua để hoạch định chính sách mới.
📋 CÂU HỎI ÔN TẬP:
# Câu 1 (OLTP vs OLAP):
Yêu cầu A và Yêu cầu B tương ứng với loại hệ thống nào (OLTP hay OLAP)? Tại sao?
yêu cầu A tương ứng với OLTP, đây là loại giao dịch thường xuyên hàng ngày, với thời gian xử lý ngắn, đo bằng tốc độ 100ms, hàng ngày sẽ có rất nhiều hàng triệu giao dịch như vậy; đối với yêu cầu B là OLAP vì nó phân tích dữ liệu trong thời gian dài và tổng hợp, không thực hiện thường xuyên
Tại sao ta tuyệt đối không được chạy câu lệnh truy vấn của Yêu cầu B trực tiếp trên cơ sở dữ liệu đang vận hành Yêu cầu A?
khối lượng dữ liệu của yêu cầu A là rất lớn, việc truy vấn trực tiếp là tốn lượng lớn tài nguyên, thay vì đó là tổng hợp, gom nhóm lại rồi phân tích sẽ hợp lý hơn.; đối với khối lượng giao dịch A phải có bước làm sạch tổng hợp trước khi lưu trữ và lúc này mới phân tích sẽ hợp lý hơn
# Câu 2 (Star Schema):
Nếu thiết kế Kho dữ liệu (Data Warehouse) cho Yêu cầu B theo mô hình Star Schema:
Bảng nào sẽ là Fact Table? Nó chứa cái gì?
Các bảng nào sẽ là Dimension Tables? Chúng chứa cái gì?
Bảng Fact là bảng sự kiện giao dịch nhận tiền trợ cấp thất nghiệp/ nó chứa các khóa ngoại về (id công dân, id thời gian, id đơn vị), tổng số tiền nhận trợ cấp thất nghiệp;
còn bảng dimension chứ các bảng để trả lời cho câu hỏi: Ai, khi nào, ở đâu, như thế nào...; dim_id_congdan, dim_id_time, dim_id_citizen
# Câu 3 (Thứ tự thực thi SQL):
Tại sao trong SQL, anh không thể lọc dữ liệu bằng cách viết: WHERE SUM(doanh_so) > 1000000 mà bắt buộc phải dùng HAVING?
Hãy giải thích dựa trên thứ tự thực thi (Execution Order) của các mệnh đề SQL mà anh đã học ở Task 1.
thứ tự thực hiện thực tế: from - where - group by - having - select - order by- limit
điều kiện where được gọi đến nhưng thứ tự thực thi lúc này giá trị sum (doanh số) chưa tồn tại nên sẽ không thể thực thi được; where dùng để đặt điều kiện cho từng dòng của dữ liệu còn having đặt trước order by sau group by để điều kiện sau khi gom nhóm dữ liệu
ví dụ: giao dịch rút tiền của các công dân trong 1 năm có 12 tháng là 12 lần rút, chúng ta sẽ tính tổng 1 năm của mỗi công dân, nếu điều kiện trong mỗi lần rút là 100k thì dùng where lên bảng amount(số tiền), còn nều điều kiện trong 1 năm rút > 500k thì dùng having sum(số tiền các tháng trong năm)


---Để kiểm tra độ sâu trong tư duy kiến trúc của anh, hãy trả lời nhanh 2 câu hỏi nhỏ sau:

# Về OLTP & OLAP: 
Anh bảo không nên chạy truy vấn OLAP trên database OLTP vì tốn tài nguyên. Vậy trong thực tế, làm thế nào ta đồng bộ dữ liệu từ hệ thống giao dịch (OLTP) sang kho dữ liệu (OLAP) mà không làm ảnh hưởng đến hiệu năng của OLTP trong giờ làm việc của hành chính công?
>>chúng ta sẽ viết một pipeline và đưa vào kho riêng biệt, không chạy trên hệ thống OLTP
# Về thứ tự thực thi SQL: Hãy xem câu lệnh sau:
sql:
SELECT quy, SUM(doanh_so) AS tong_doanh_so
FROM fact_sales
GROUP BY quy
HAVING tong_doanh_so > 1000000;
Theo anh, câu lệnh này có chạy được trên các hệ quản trị cơ sở dữ liệu tiêu chuẩn (như PostgreSQL hay SQL Server) không?không
Gợi ý: Nhìn lại thứ tự thực thi: HAVING chạy trước hay SELECT chạy trước? Liệu HAVING có nhìn thấy cái tên tong_doanh_so do SELECT đặt ra không? having chạy trước và chúng ko thể thấy tong_doanh_so từ select, nếu đúng phải là having sum(doanh_so)>1000000; với cột doanh số nằm trong bảng fact_sales
>>
---✅ Acknowledge (Ghi nhận)
1. Về thứ tự thực thi SQL (HAVING với Alias): Cực kỳ chính xác! Câu lệnh đó sẽ báo lỗi ngay lập tức trên PostgreSQL, Oracle hay SQL Server vì HAVING được biên dịch trước SELECT, nên nó hoàn toàn mù tịt về cái tên tong_doanh_so. Rất tốt!
2. Về đồng bộ OLTP sang OLAP: Ý tưởng "viết pipeline đẩy sang kho riêng" là đúng. Nhưng để hệ thống cấp quốc gia chạy mượt mà không làm chậm hệ thống dịch vụ công đang chạy, trong thực tế người ta dùng 3 chiêu thức sau (anh ghi nhớ để áp dụng sau này):
- Chỉ đọc từ Read Replica: Không bao giờ chọc trực tiếp vào Database Master (nơi đang ghi giao dịch). Ta tạo một bản sao chỉ đọc (Read Replica) được đồng bộ thời gian thực, và pipeline ETL sẽ lấy dữ liệu từ bản sao này.
- CDC (Change Data Capture): Thay vì chạy lệnh SELECT * quét toàn bộ bảng (gây tốn I/O ổ cứng), ta dùng công cụ (như Debezium, Kafka Connect) để "đọc trộm" log ghi nhận giao dịch (WAL log/Binlog) của database. Việc đọc log này tốn gần như 0% tài nguyên CPU của database.
- Lập lịch giờ thấp điểm (Off-peak Batching): Chạy pipeline vào lúc 2 giờ sáng (như anh thiết kế ở Module 0).

## 🔒 Task đang chờ thực hiện

### Task 2: Window Functions (SQL Nâng cao)
> *Cấp độ SQL mà 90% Junior không biết nhưng được hỏi trong mọi cuộc phỏng vấn Senior.*
- `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
- `LAG()`, `LEAD()` — So sánh với hàng trước/sau
- `SUM() OVER()`, `AVG() OVER()` — Tính tổng lũy kế
- Bài toán thực chiến: Xếp hạng tỉnh thành theo doanh số từng quý


### Task 3: Data Modeling Nâng cao
- Snowflake Schema vs Star Schema
- Slowly Changing Dimensions (SCD Type 1, 2, 3)
- Thiết kế schema cho bài toán dân số quốc gia

### Task 4: Query Optimization (Tối ưu truy vấn)
- Index — Tại sao thiếu Index là "án tử" cho Data Warehouse?
- Execution Plan — Đọc hiểu EXPLAIN ANALYZE
- Partition — Chia nhỏ bảng 1 tỷ dòng để truy vấn siêu nhanh

---

*Cập nhật lần cuối: 27/06/2026 — Task 1 hoàn thành.*
