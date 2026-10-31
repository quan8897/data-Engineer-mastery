# ⚡ RESEARCH 02 — CDC (CHANGE DATA CAPTURE) VỚI DEBEZIUM & KAFKA CONNECT

> **Task:** 3.2 | **Module:** 3 — Real-time Streaming & Integration  
> **Ngày bắt đầu:** 2026-10-01  
> **Trạng thái:** 🔄 Đang học  

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Sau khi hoàn thành bài nghiên cứu này, bạn làm chủ các năng lực cốt lõi:
1. **Bản chất của CDC (Change Data Capture):** Hiểu rõ tại sao các hệ thống dữ liệu hiện đại không dùng Polling (`SELECT * WHERE updated_at > ...`) để đồng bộ dữ liệu mà bắt buộc phải dùng Log-based CDC.
2. **Cơ chế Log-based CDC (WAL / Binlog):** Nắm vững cách Debezium "nghe trộm" trực tiếp vào file Transaction Log (Write-Ahead Log của PostgreSQL, Binlog của MySQL, Redo Log của Oracle) mà không tạo gánh nặng CPU/RAM/Locks lên Database nguồn.
3. **Kiến trúc Kafka Connect Ecosystem:** Phân biệt Source Connector (Kéo data từ DB vào Kafka) và Sink Connector (Đẩy data từ Kafka xuống Lakehouse/Data Warehouse/Elasticsearch).
4. **Bắt trọn 3 loại biến động (INSERT, UPDATE, DELETE):** Hiểu tại sao phương pháp Polling truyền thống KHÔNG THỂ bắt được sự kiện `DELETE` (Hard Delete), trong khi Log-based CDC bắt trọn được cả trạng thái trước (`before`) và sau (`after`) của bản ghi.
5. **Schema Evolution & Tombstone Message:** Hiểu cách Debezium xử lý khi bảng bị sửa cấu trúc (thêm/bớt cột) và cách biểu diễn bản ghi bị xóa trong Kafka (Tombstone message với `Value = null`).

---

## 🔗 Kết nối kiến thức cũ

```
Module 0 — Task 7 & Task 8:
  Hiểu về Write-Ahead Log (WAL) và tính Idempotent trong ghi đĩa. Mọi thao tác ghi DB đều phải ghi vào WAL trước khi ghi vào bảng dữ liệu chính thức!

Module 1 — Task 1 & Task 3:
  Hệ thống OLTP (PostgreSQL/MySQL) cần đồng bộ dữ liệu sang Data Warehouse (OLAP) để phân tích báo cáo.

Task 3.1 (KAFKA FUNDAMENTALS):
  Kafka là băng chuyền sự kiện. Nhưng dữ liệu gốc nằm ở Database tác nghiệp của các Bộ/Ngành. 
  → CDC + Debezium chính là "chiếc máy bơm tự động", hút mọi biến động từ Database nguồn bắn thẳng lên Kafka Topic theo thời gian thực!
```

---

## 📖 Từ Điển Thuật Ngữ Cốt Lõi (Key Terminology & IPA Pronunciation)

| Thuật ngữ Tiếng Anh | Phiên âm IPA / Loại từ | Nghĩa tiếng Việt | Bản chất kỹ thuật cần nhớ |
|---|---|---|---|
| **Change Data Capture (CDC)** | /ˈtʃeɪndʒ ˈdeɪ.tə ˈkæp.tʃər/ (n) | Bắt biến động dữ liệu | Kỹ thuật phát hiện và ghi lại tất cả các thay đổi (INSERT, UPDATE, DELETE) trong cơ sở dữ liệu nguồn theo thời gian thực. |
| **Transaction Log (WAL / Binlog)** | /trænˈzæk.ʃən lɒɡ/ (n) | Nhật ký giao dịch | File log ghi tuần tự mọi thao tác thay đổi dữ liệu của Database trước khi commit xuống đĩa (PostgreSQL: WAL, MySQL: Binlog). |
| **Logical Decoding** | /ˈlɒdʒ.ɪ.kəl diːˈkəʊ.dɪŋ/ (n) | Giải mã logic | Cơ chế nội tại của PostgreSQL cho phép trích xuất các thao tác DML từ WAL thành cấu trúc dữ liệu logic (dòng/cột) dễ đọc thay vì raw bytes. |
| **Replication Slot** | /ˌrep.lɪˈkeɪ.ʃən slɒt/ (n) | Khe sao chép | Cơ chế của PostgreSQL lưu con trỏ `restart_lsn` để bảo đảm WAL không bị xóa/recycle chừng nào consumer chưa xác nhận đã đọc xong. |
| **Log Sequence Number (LSN)** | /lɒɡ ˈsiː.kwəns ˈnʌm.bər/ (n) | Số thứ tự nhật ký | Mã định danh 64-bit chỉ vị trí byte chính xác của bản ghi trong chuỗi file WAL của PostgreSQL. |
| **WAL Bloat** | /wɔːl bləʊt/ (n) | Phình to nhật ký WAL | Hiện tượng đĩa máy chủ PostgreSQL bị đầy 100% do Replication Slot giữ chân các file WAL không cho giải phóng khi consumer sập. |
| **Replica Identity** | /ˈrep.lɪ.kə aɪˈden.tə.ti/ (n) | Danh tính bản sao | Cấu hình bảng trong PostgreSQL quy định thông tin nào của dòng CŨ (old tuple) được ghi vào WAL khi `UPDATE`/`DELETE` (`DEFAULT`, `FULL`, `NOTHING`, `INDEX`). |
| **Write Amplification** | /raɪt ˌæm.plɪ.fɪˈkeɪ.ʃən/ (n) | Hiện tượng khuếch đại ghi (Khuếch đại ghi đĩa) | Hiện tượng một thao tác sửa nhỏ (1 cột) khiến dung lượng ghi log tăng vọt gấp nhiều lần (khi bật `REPLICA IDENTITY FULL`). |
| **Log-based CDC** | /lɒɡ beɪst siː-diː-siː/ (n) | CDC dựa trên file Log | Kỹ thuật đọc trực tiếp file WAL/Binlog ở mức byte, không chạy câu lệnh SQL nào vào Database, độ trễ mili-giây, tải gần như bằng 0. |
| **Query-based Polling** | /ˈkwɪə.ri beɪst ˈpəʊ.lɪŋ/ (n) | Quét định kỳ bằng SQL | Cách làm thô sơ: Chạy định kỳ `SELECT * WHERE updated_at > last_time`. Gây lock contention, trễ dữ liệu và mù trước Hard Delete. |
| **Lock Contention** | /lɒk kənˈten.ʃən/ (n) | Tranh chấp khóa | Hiện tượng các lệnh SELECT lớn chiếm giữ Shared Lock làm nghẽn các câu lệnh INSERT/UPDATE của người dùng OLTP. |
| **Kafka Connect** | /ˈkæf.kə kəˈnekt/ (n) | Khung kết nối Kafka | Nền tảng phân tán mã nguồn mở của Kafka giúp kéo/đẩy dữ liệu ra vào Kafka mà không cần tự viết code Producer/Consumer bằng tay. |
| **Source Connector** | /sɔːs kəˈnek.tər/ (n) | Bộ kết nối đầu vào | Kéo dữ liệu từ hệ thống bên ngoài (PostgreSQL, MySQL, S3) đưa VÀO Kafka Topic (ví dụ: Debezium). |
| **Sink Connector** | /sɪŋk kəˈnek.tər/ (n) | Bộ kết nối đầu ra | Lấy dữ liệu TỪ Kafka Topic đẩy sang hệ thống hạ nguồn (Delta Lake, Elasticsearch, Snowflake, BigQuery). |
| **Debezium** | /dəˈbiː.zi.əm/ (n) | Nền tảng CDC phân tán | Bộ công cụ CDC hàng đầu thế giới được xây dựng trên Kafka Connect, chuyên phân tích log của PostgreSQL, MySQL, SQL Server, Oracle. |
| **Tombstone Message** | /ˈtuːm.stəʊn ˈmes.ɪdʒ/ (n) | Bản tin bia mộ | Bản tin đặc biệt trong Kafka có `Key = ID` và `Value = null`, dùng để thông báo cho downstream và Log Compaction biết bản ghi đã bị DELETE. |
| **Log Compaction** | /lɒɡ kəmˈpæk.ʃən/ (n) | Nén nhật ký Kafka | Tính năng của Kafka chỉ giữ lại bản ghi mới nhất cho mỗi Key, loại bỏ các bản ghi cũ cùng Key để tiết kiệm đĩa. |
| **Schema Evolution** | /ˈskiː.mə ˌiː.vəˈluː.ʃən/ (n) | Tiến hóa lược đồ | Khả năng tự động thích ứng và cập nhật cấu trúc bảng khi có thay đổi DDL (thêm cột, đổi kiểu dữ liệu) mà không làm sập pipeline. |
| **Outbox Pattern** | /ˈaʊt.bɒks ˈpæt.ən/ (n) | Mẫu thiết kế Outbox | Kỹ thuật bảo đảm tính nhất quán: Ứng dụng ghi sự kiện vào bảng `outbox` trong cùng 1 transaction DB, sau đó Debezium bắt log từ bảng này đẩy vào Kafka. |
| **Dead Letter Queue (DLQ)** | /ded ˈlet.ər kjuː/ (n) | Hàng đợi thư chết | Topic Kafka lưu trữ các tin nhắn lỗi/hỏng cấu trúc không thể parse được, giúp pipeline không bị sập toàn bộ. |

---

## 🧠 Framework 5 Tầng — CDC & Debezium

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không copy)*

```
[Học viên hoàn thiện]:
CDC (Change Data Capture) là cơ chế biến các thao tác thay đổi dữ liệu (INSERT, UPDATE, DELETE) trên cơ sở dữ liệu tác nghiệp (OLTP) thành các dòng sự kiện (Event Stream) thời gian thực và đẩy vào Kafka để các hệ thống hạ nguồn khai thác mà không làm ảnh hưởng đến hệ thống chính.
```

---

### Tầng 2 — HOW (Cơ chế vận hành & So sánh đối đầu)

#### 1. So sánh đối đầu: Log-based CDC vs Query-based Polling
```
[Học viên hoàn thiện]:
- Tại sao Polling (SELECT * WHERE updated_at > ...) gặp giới hạn lớn:
  + Bắt Database phải quét bảng liên tục (Full Table Scan nếu thiếu index), gây tranh chấp CPU/RAM và Lock bảng với người dùng thật.
  + Không tự động bắt được bản ghi bị xóa (Hard Delete): Dòng đã bị DELETE khỏi current-state table thì câu lệnh SELECT không thể phát hiện nếu không có cơ chế lưu dấu vết riêng (như Soft-delete is_deleted/deleted_at hoặc bảng Audit trigger).
  + Bỏ sót trạng thái trung gian (Loss of Intermediate States): Nếu trong 5 phút một đơn hàng đổi từ CREATED -> PAID -> CANCELLED, lệnh SELECT chỉ thấy CANCELLED, mất trắng lịch sử thanh toán.
  + Buộc bảng nguồn phải có cột updated_at (xâm phạm thiết kế của các hệ thống di sản Legacy).
- Cơ chế đọc WAL/Binlog của Debezium:
  + Không phải tự mở file WAL thô để parse từng byte, mà sử dụng cơ chế **Logical Decoding / Logical Replication** (thông qua plugin như pgoutput) và **Replication Slot** của PostgreSQL (hoặc Binlog event stream của MySQL) để nhận luồng thay đổi đã được giải mã.
  + Tác động thấp hơn rất nhiều so với Polling (nhưng không phải zero-impact vì DB vẫn tốn CPU giải mã và I/O duy trì slot).
```

#### 2. Cấu trúc một thông điệp Debezium CDC
```
[Học viên hoàn thiện]:
- "before": Chứa trạng thái dữ liệu cũ của bản ghi TRƯỚC KHI bị thay đổi (null nếu là thao tác INSERT).
- "after": Chứa trạng thái dữ liệu mới của bản ghi SAU KHI được thay đổi (null nếu là thao tác DELETE).
- "op": Thao tác tác động vào dữ liệu:
  + 'c' (Create / Insert)
  + 'u' (Update)
  + 'd' (Delete)
  + 'r' (Read - dữ liệu chụp snapshot ban đầu khi vừa kích hoạt Debezium).
- Ý nghĩa với SCD Type 2:
  + Cấu trúc before/after phân định rõ quá trình biến đổi của dữ liệu theo mốc thời gian.
  + Cực kỳ quý giá để xây dựng bảng lịch sử thay đổi: Lấy giá trị 'before' để đóng bản ghi cũ (is_current = false, end_date = ts_ms), và lấy giá trị 'after' để mở bản ghi mới (is_current = true, start_date = ts_ms) mà không cần tốn công truy vấn ngược lại kho dữ liệu.
```

#### 3. Hệ sinh thái Kafka Connect (Source vs Sink)
```
[Học viên hoàn thiện]:
- Kiến trúc luồng đi: [OLTP Database] -> [Debezium Source Connector] -> [Kafka Topic] -> [Delta Lake Sink Connector] -> [Data Lakehouse].
- Ưu điểm của Kafka Connect so với tự viết script Python thủ công:
  + Tự động lưu vị trí (Offset / LSN Tracking): Debezium lưu con trỏ đọc log vào Kafka topic nội bộ, khi crash/restart tự đọc tiếp chính xác từng byte, không mất dữ liệu. Script Python tự viết nếu chết giữa chừng rất khó xác định dòng nào đã gửi/chưa gửi.
  + Cụm phân tán chịu lỗi (Distributed Fault Tolerance): Kafka Connect chạy dạng cluster, tự chia tải và tự động fail-over khi có worker node sập.
  + Tự thích ứng Schema (Schema Evolution): Bảng thêm cột mới thì Debezium tự phát hiện và cập nhật schema mà không cần sửa code hay restart.
  + Khung cấu hình No-Code: Chỉ cần khai báo file JSON kết nối, không phải bảo trì hàng trăm dòng code script dễ sinh lỗi.
```

---

### Tầng 3 — WHY
> *(Tại sao trong kiến trúc dữ liệu hiện đại, Log-based CDC là giải pháp vượt trội để đồng bộ dữ liệu thời gian thực?)*

```
[Học viên điền vào đây: Phân tích 3 khía cạnh:
1. Low Impact trên hệ thống tác nghiệp: Tại sao cơ chế Logical Decoding của CDC lại ít ảnh hưởng đến hiệu năng OLTP hơn nhiều so với việc chạy câu lệnh SELECT liên tục?
khi select liên tục tốn ram/cpu liên tục, việc này đồng thời tác động trực tiếp đến database và chỉ ghi nhận được trạng thái mới nhất của dữ liệu tại thời điểm select, có thể kết quả sẽ lỗi thời và ko còn chính xác (đã thêm, sửa, xóa ngay sau đó), cơ chế Logical Decoding của CDC có ảnh hưởng đến hiệu năng nhưng ít hơn vì chỉ quan tâm đến những biển đổi mới tác động trực tiếp lên dữ liệu khi đã được commit
2. Real-time Latency: Tốc độ đẩy biến động sang các hạ nguồn (Elasticsearch, Cache Redis, Fraud Detection) đạt độ trễ mili-giây như thế nào? trong phạm vi ms gần như là ngay lập tức, mà ko cần quan tâm đến database tổng thể
3. Bắt trọn Audit Trail: Tại sao chỉ có CDC mới bảo toàn được toàn bộ lịch sử các bước nhảy trạng thái trung gian của giao dịch?
cơ chế của nó giải mã việc lịch sử các bước nhảy trạng thái được lưu trữ hoàn toàn tại log mà ko mất đi ngay sau đó giúp cho chúng ta có cái nhìn toàn cảnh về sự biến đổi của dữ liệu]
```

---

### Tầng 4 — FAILURE & CẠM BẪY SỐNG CÒN TRONG PRODUCTION
> *(Những thảm họa thực tế khi vận hành CDC & Debezium)*

```
[Học viên điền vào đây: Phân tích 4 thảm họa kinh điển:
1. Thảm họa WAL Bloat (Tràn ổ cứng Database nguồn):
   - Khi cụm Kafka/Connect bị sập hoặc nghẽn mạng nhiều ngày, tại sao Replication Slot của PostgreSQL lại khiến ổ cứng máy chủ DB nguồn bị phình to đến 100% và crash?
   - Cấu hình tham số an toàn nào trên PostgreSQL (ví dụ: max_slot_wal_keep_size) để cứu sống Database nguồn? Cái giá phải đánh đổi khi slot bị drop là gì?
  

2. Cạm bẫy REPLICA IDENTITY (Mất dữ liệu "before"):
   - Tại sao ở cấu hình mặc định (DEFAULT) của PostgreSQL, phần "before" trong bản tin UPDATE/DELETE chỉ có Primary Key mà không có các cột khác?
   - Muốn lấy đủ toàn bộ giá trị cũ của mọi cột để làm SCD Type 2 ở Data Warehouse thì phải cấu hình gì trên bảng PostgreSQL (REPLICA IDENTITY FULL)? Điểm bất lợi về dung lượng WAL là gì?

3. Schema Evolution không phải phép màu:
   - Khi bảng nguồn đột ngột thay đổi cấu trúc phá vỡ tương thích (Breaking DDL như đổi kiểu dữ liệu, drop cột bắt buộc), chuyện gì xảy ra với Debezium và Schema Registry? Làm sao để không làm sập pipeline?

4. Phân biệt CDC DELETE Event vs Kafka Tombstone:
   - Bản tin CDC DELETE ({ op: 'd', before: ... }) khác gì với bản tin Kafka Tombstone ({ Key: id, Value: null })?
   - Tại sao Consumer hạ nguồn nếu không xử lý cẩn thận sẽ bị dính lỗi NullPointerException khi gặp tin nhắn Tombstone?]
```

---

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG NÊN dùng Debezium / CDC?)*

```
[Học viên điền vào đây:
1. So sánh chi phí vận hành: CDC đòi hỏi cả hệ sinh thái (Kafka, Kafka Connect, Schema Registry, Giám sát slot, xử lý re-snapshot). Trong trường hợp nào thì một job Batch ETL (SQL/Spark chạy định kỳ) đơn giản, rẻ và hiệu quả hơn gấp nhiều lần?
2. Những loại dữ liệu hoặc bài toán nghiệp vụ nào KHÔNG phù hợp với mô hình CDC?]
```

---

## 🛠️ TÌNH HUỐNG THỰC CHIẾN — Đồng Bộ Dữ Liệu Thay Đổi Cư Dân Cho 63 Tỉnh Thành

**Bối cảnh:**
- Bộ Công An quản lý bảng `nhan_khau` trên hệ thống cơ sở dữ liệu tác nghiệp PostgreSQL.
- Mỗi ngày có hàng triệu biến động: sinh mới (INSERT), thay đổi nơi thường trú/kết hôn (UPDATE), và xóa hồ sơ chuyển định cư (DELETE).
- Cần đồng bộ liên tục về Trung tâm Phân tích Dữ liệu Quốc gia (Delta Lakehouse) để phục vụ dự báo dân số và quản lý an ninh.

**Nhiệm vụ của bạn:**
1. Trình bày luồng kiến trúc đồng bộ từ PostgreSQL sang Delta Lake thông qua Debezium và Kafka.
2. Thiết kế giải pháp xử lý sự kiện một công dân bị xóa khỏi hộ khẩu (`DELETE` event): Hạ nguồn sẽ nhận dạng và cập nhật trạng thái trong Data Warehouse như thế nào?

---

*Tài liệu nghiên cứu Task 3.2 — Data Engineering Mastery*  
*Bắt đầu phiên học: 2026-10-01*
