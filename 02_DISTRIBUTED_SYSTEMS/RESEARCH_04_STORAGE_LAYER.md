# 🧊 RESEARCH 04 — STORAGE LAYER: DELTA LAKE & APACHE ICEBERG (KỶ NGUYÊN LAKEHOUSE)

> **Task:** 2.4 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-18 | **Ngày hoàn thành:** 2026-09-21
> **Trạng thái:** ✅ Hoàn thành

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Hoàn thành bài này, bạn phải đạt được các năng lực cốt lõi:
1. **Giới hạn của Parquet thuần:** Phân tích được vì sao chỉ có Parquet trên HDFS/S3 là CHƯA ĐỦ: thiếu ACID, không thể `UPDATE`/`DELETE` từng dòng, dễ dính dữ liệu rác khi job gãy giữa chừng (Corrupted Data).
2. **Bản chất Transaction Log & ACID:** Hiểu sâu cơ chế **Transaction Log** (như `_delta_log` hoặc Iceberg Metadata Tree) sử dụng **Optimistic Concurrency Control (OCC)** để mang các thuộc tính **ACID** (Nguyên tử, Nhất quán, Cô lập, Bền vững) lên Data Lake.
3. **Cơ chế Time Travel & Snapshot Isolation:** Giải thích được cách hệ thống "quay ngược thời gian" về phiên bản dữ liệu quá khứ mà không cần sao chép tốn dung lượng đĩa.
4. **Tối ưu hóa Storage (Compaction & Z-ORDER):** Làm chủ kỹ thuật giải quyết vấn nạn file nhỏ (**Small Files Problem**) bằng lệnh `OPTIMIZE` và kỹ thuật sắp xếp đa chiều **Z-Ordering** giúp bỏ qua 90% file khi đọc (Data Skipping).
5. **Năng lực so sánh & Lựa chọn công nghệ:** Phân biệt được **Delta Lake** (hệ sinh thái Spark/Databricks) vs **Apache Iceberg** (chuẩn mở đa engine: Spark, Trino, Flink, Snowflake).

---

## 🔗 Kết nối kiến thức cũ

```
Task 2.0: Medallion Architecture (Bronze -> Silver -> Gold)
Task 2.1 (HDFS / S3): Nơi chứa các tệp dữ liệu vật lý
Task 2.3 (SPARK): Cỗ máy tính toán In-Memory siêu tốc
                  → Nhưng Spark ghi dữ liệu xuống ĐÂU và BẰNG CÁCH NÀO?
                  → Nếu ghi tệp Parquet truyền thống: Mất mạng giữa chừng = HỎNG FILE!
Task 2.4 (DELTA LAKE / ICEBERG): LỚP LƯU TRỮ THÔNG MINH (Storage Layer)
                  → Đóng vai trò là "Người gác cổng ACID", biến Data Lake thành LAKEHOUSE!
```

---

## 📖 Từ Điển Thuật Ngữ Cốt Lõi (Key Terminology for Task 2.4)

| Thuật ngữ Tiếng Anh | Nghĩa tiếng Việt | Bản chất kỹ thuật cần nhớ |
|---|---|---|
| **Lakehouse Architecture** | Kiến trúc Lakehouse | Kết hợp: Lưu trữ rẻ của Data Lake + Quản trị ACID & Tối ưu của Data Warehouse. |
| **ACID Transactions** | Giao dịch chuẩn ACID | 4 tính chất: Atomicity (Nguyên tử), Consistency (Nhất quán), Isolation (Cô lập), Durability (Bền vững). |
| **Transaction Log (`_delta_log`)** | Nhật ký giao dịch | "Nguồn chân lý" ghi lại lịch sử từng commit (Add/Remove file) qua các file JSON/Parquet checkpoint. |
| **Optimistic Concurrency Control (OCC)** | Kiểm soát tương tranh lạc quan | Cho phép nhiều job cùng ghi dữ liệu đồng thời, chỉ kiểm tra xung đột lúc commit; nếu trùng file thì tự retry. |
| **Time Travel (Data Versioning)** | Quay ngược thời gian | Khả năng truy vấn hoặc phục hồi dữ liệu về phiên bản cũ (`VERSION AS OF` / `TIMESTAMP AS OF`). |
| **Snapshot Isolation** | Cô lập ảnh chụp | Reader luôn đọc snapshot dữ liệu đã hoàn tất, không bao giờ đọc phải dữ liệu dở dang của Writer. |
| **Copy-on-Write (CoW)** | Sao chép khi ghi | Khi UPDATE/DELETE: Đọc file cũ, sửa dòng cần sửa, ghi file Parquet mới hoàn toàn và tráo đổi trong log. |
| **Merge-on-Read (MoR)** | Hợp nhất khi đọc | Khi UPDATE/DELETE: Chỉ ghi thay đổi vào file delta riêng biệt; khi reader query mới hợp nhất lại. |
| **Compaction (`OPTIMIZE`)** | Gom nén tệp tin | Gộp hàng ngàn file Parquet nhỏ (vài KB-MB) thành file lớn chuẩn (~128MB - 1GB) để giải quyết Small Files Problem. |
| **Z-Ordering** | Sắp xếp đường cong chữ Z | Gom cụm dữ liệu đa chiều (Clustering) trên nhiều cột, tối đa hóa số file bị bỏ qua khi tìm kiếm. |
| **Data Skipping** | Bỏ qua dữ liệu | Dùng thống kê Min/Max trong metadata để bỏ qua 80-95% file Parquet không chứa dữ liệu cần tìm. |
| **Schema Enforcement** | Bắt buộc đúng cấu trúc | Chặn đứng ngay lập tức nếu dữ liệu ghi vào không khớp với schema đã định nghĩa của bảng. |
| **Schema Evolution** | Tiến hóa cấu trúc | Cho phép tự động thêm cột mới an toàn vào bảng (`mergeSchema = true`) mà không làm hỏng dữ liệu cũ. |
| **VACUUM** | Dọn dẹp tệp mồ côi | Lệnh dọn dẹp vật lý: Xóa vĩnh viễn các file Parquet cũ đã bị loại bỏ khỏi transaction log quá hạn lưu trữ. |

---

## 🧠 Framework 5 Tầng — Modern Storage Layer (Delta Lake / Iceberg)

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không copy)*

```
[Delta Lake / Iceberg là một lớp kiến trúc lưu trữ thông minh trên nền data lake, với cơ chế kết hợp với việc xử lý dữ liệu sẽ tạo ra transaction log để lưu trữ tiến trình xử lý, giúp dữ liệu đảm bảo tính ACID, khắc phục những hạn chế mà việc xử lý dữ liệu đối với parquet thuần gây ra: như khi bị crash, ngắt hệ thống làm sai lệch tính toán, dữ liệu nhỏ lẻ, tìm kiếm dữ liệu chưa được tối ưu]
```

---

### Tầng 2 — HOW (Kiến trúc & Cơ chế vận hành)

#### 1. Tại sao Parquet thuần không có ACID? Transaction Log (`_delta_log`) hoạt động thế nào?
```
[Học viên mô tả:
- Nếu đang ghi file Parquet mà job bị crash thì chuyện gì xảy ra? dữ liệu sẽ không xác định được ghi đến đâu đã xong hay chưa, khi chạy tính toán sẽ gây sai lệch, hay khi chạy lại sẽ gây ra sự trùng lặp dữ liệu; ACID là tiêu chuẩn/ A-atominity tính toàn vẹn, dữ liệu chỉ khi được xử lý xong thì mới tạo ra transaction log, nếu có bị mất hay gián đoạn xử lý thì trạng thái sẽ được ghi nhận trước đó vì chưa tạo ra transaction log, 
- Transaction Log ghi lại những gì (Add file, Remove file)? transaction log ghi lại quá trình xử lý dữ liệu được thực thi thành công, đảm bảo dữ liệu phải được thực thi toàn bộ - commit thì mới tạo ra transaction log, ghi dưới dạng Json, dùng để truy xuất ngược lại để đảm bảo dữ liệu luôn sẵn sàng và chuẩn
- ACID được đảm bảo thế nào qua từng file JSON commit?]
a-atomicity tính toàn vẹn: dữ liệu được ghi khi thực hiện xong task, đảm bảo dữ liệu toàn vẹn, nếu có sự gián đoạn trong quá trình xử lý, dữ liệu thay đổi sẽ ko được ghi nhận

c- consistency- tính nhất quán: dữ liệu được đảm bảo đúng định dạng, nhất quán trong tất cả các lần thực hiện, đảm bảo dữ liệu không xảy ra lỗi khi gộp lại và tính toán

I- isolation - tính độc lập: việc đọc và chỉnh sửa dữ liệu được thực hiện song song, nếu quá trình ghi dữ liệu chưa được commit thực hiện xong thì việc đọc dữ liệu sẽ đọc tại trạng thái dữ liệu sẵn sàng nhất trước giai đoạn dữ liệu chỉnh sửa, hay việc cả 2 job cùng ghi dữ liệu vào 1 parquet thì job nào commit trước thì transaction log ghi nhận job được được hoàn thành và xong trước, job sau chỉnh sửa sẽ không được thực thi do kiểm tra file parquet đó đã không còn tồn tại, job sau phải chạy lại với dữ liệu mới nhất
D-Durability- tính bền vững: dữ liệu một khi được ghi xuống thì đảm bảo sự bền vững không thể mất, khi sập hệ thống khởi động lại dữ liệu không thể mất
```

#### 2. Cơ chế Time Travel (Quay ngược thời gian)
```
[Học viên mô tả:
- Làm thế nào để truy vấn lại dữ liệu lúc 9:00 sáng hôm qua hoặc Version 3? cế chế time travel cho phép việc truy xuất dữ liệu tại thời điểm truy vấn theo yêu cầu, đảm bảo khôi phục khi cần
- Spark có phải copy lại toàn bộ 800GB cho mỗi version không? Tại sao?]không spark chỉ cần so sánh sự khác nhau giữa transaction log và dữ liệu parquet thực tế và chỉ thực thi những dữ liệu mới chứ ko copy lại toàn bộ 800Gb
```
> **💡 Mentor chuẩn hóa:** Spark **không bao giờ copy lại 800GB**. Cơ chế Time Travel hoạt động bằng cách **Replay Transaction Log**: Spark đọc log từ commit 0 đến thời điểm/version yêu cầu để tái hiện lại danh sách chính xác các file Parquet đang "Active" tại thời điểm đó. Vì các file cũ chưa bị `VACUUM` xóa vật lý, Spark chỉ việc đọc đúng danh sách file đó lên.

#### 3. Kỹ thuật Dọn dẹp & Tối ưu: OPTIMIZE (Compaction) & VACUUM
```
[Học viên phân biệt:
- Lệnh OPTIMIZE giải quyết Small Files Problem thế nào?OPTIMIZE thực hiện việc gom nhóm các file dung lượng nhỏ để gom thành các file có dung lượng lớn để thực hiện , ví dụ các file nhỏ 5kb, 6kb, 3kb, 7kb,... gom thành file lớn 1Gb, 128mb để thực thi
- Lệnh VACUUM dùng để làm gì? Nếu chạy VACUUM với retention = 0 giờ thì nguy hiểm ra sao?]VACUUM thực thi việc xóa những bản dữ liệu cũ khi không còn nhu cầu sử dụng truy vấn đến nữa, với retention=0 có thể dẫn đến lỗi file ko tồn tại do vacuum đã thực hiện xóa trong khi job đang lấy file parquet để xử lý, thời gian xử lý ngay lập tức có thể làm file đó bị xóa ngay lập tức, bị chuyển trạng thái remove và vacuum xóa ngay lập tức.
```
> **💡 Mentor chuẩn hóa:** Kích thước file chuẩn vàng của Parquet sau khi `OPTIMIZE` là **128MB - 1GB**. Tuyệt đối không gộp lên 4-5GB vì sẽ phá vỡ tính song song (Parallelism) và gây tràn RAM (OOM). Lệnh `VACUUM` với retention = 0 sẽ xóa vật lý ngay các file bị `remove`, gây lỗi `FileNotFoundException` cho bất kỳ query nào đang chạy dở trên snapshot cũ.

#### 4. Kỹ thuật sắp xếp dữ liệu Z-ORDER Clustering
```
[Học viên mô tả: Z-Order là gì? Nó giúp Spark "nhảy cóc" (Data Skipping) bỏ qua các file Parquet không cần đọc như thế nào?] Z-order là việc thực hiện gom nhóm các dữ liệu có tính chất, hay thuộc tính giống nhau// ví dụ phân chia theo tỉnh// khi tìm dữ liệu tỉnh A, thì việc tìm kiếm sẽ nhanh hơn do bỏ qua những dữ liệu không liên quan đến tỉnh A, và nó có sự tự tin tính chắc chắn trong việc bỏ qua ko cần đọc, đảm bảo ko gây ra sự sai lệch lại tiết kiệm thời gian thực hiện
```
> **💡 Mentor chuẩn hóa:** 
> - **1 cột:** Z-Order hoạt động như sắp xếp tuyến tính (đoạn thẳng 1D từ Min đến Max).
> - **Từ 2 cột trở lên:** Z-Order sử dụng thuật toán đan xen bit (Morton space-filling curve) để phân cụm dữ liệu đa chiều như một **lưới ma trận 2D** hoặc **khối rubik 3D** trong cùng các file Parquet 128MB.
> - **Hiệu quả:** Thu hẹp dải Min-Max của nhiều cột đồng thời trên từng file mà **KHÔNG sinh thêm thư mục con vật lý** (tránh sập NameNode do hàng triệu thư mục của Partitioning). Khi lọc theo bất kỳ cột nào trong Z-Order, Spark đọc metadata và bỏ qua (Data Skipping) từ 90% đến 99% số file không liên quan.

---

### Tầng 3 — WHY
> *(Tại sao thế giới chuyển từ Data Warehouse truyền thống sang Kiến trúc Lakehouse: Data Lake + Delta/Iceberg?)*

```
[Học viên điền vào đây: So sánh chi phí lưu trữ, tính mở (Open Format), khả năng hỗ trợ cả BI lẫn AI/ML]
việc chuyển từ dwh sang lakehouse nhằm tận dụng những ưu điểm của Data warehouse và data lake, xét đến chi phí khi tận dụng nền tảng lưu trữ phi tập trung, tăng tốc độ tính toán, giảm chi phí, dữ liệu đa dạng so với việc chỉ xử lý dữ liệu có cấu trúc trong DWH, việc lưu trữ dữ liệu thống nhất trên 1 hệ thống thay vì phải lưu trữ nhiều nơi trung gian, tốn chi phí đồng bộ và chồng chéo giữa các hệ thống, dữ liệu được đảm bảo xuyên suốt phục vụ cho BI lẫn AI/ML 
```

---

### Tầng 4 — FAILURE
> *(Xung đột đồng thời — Concurrent Write Conflict là gì?)*

```
[Học viên điền vào đây:
- Khi 2 job Spark cùng lúc chạy lệnh UPDATE vào cùng 1 bảng Delta, chuyện gì xảy ra? khi cả 2 củng chạy update vào cùng 1 bảng, dữ liệu lúc này sẽ thực hiện đồng thời tuy nhiên job nào xong trước được ghi nhận trước, thay vì thực hiện lần lượt, job sau khi commit sẽ xảy ra lỗi vì bảng lúc này đã bị biến đổi sau job đầu, việc thực hiện sẽ là job sau cập nhật bảng sau job 1 và thực hiện lại job 2
- Cơ chế Optimistic Concurrency Control (OCC) xử lý xung đột này thế nào?]
```
> **💡 Mentor chuẩn hóa:** Cơ chế **OCC (Optimistic Concurrency Control)** giả định các job ít khi đụng độ. Cả 2 job đều đọc snapshot ban đầu và tính toán độc lập. Khi commit: Job nào commit trước ghi thành công vào log; Job commit sau kiểm tra xem các file mà nó định ghi đè có bị Job trước `remove` hoặc thay đổi hay không. Nếu có xung đột (Conflict), Delta Lake sẽ hủy commit của Job 2, báo `ConcurrentModificationException` và tự động retry trên snapshot mới nhất.

---

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG nên dùng Delta Lake / Iceberg?)*

```
[Học viên điền vào đây] không nên dùng khi dữ liệu nhỏ, dữ liệu ít có sự thay đổi, cần tốc độ tính toán nhanh
```
> **💡 Mentor chuẩn hóa:** Không nên dùng Delta Lake/Iceberg khi:
> 1. Dữ liệu quá nhỏ (vài MB đến vài trăm MB) — chi phí quản lý Transaction Log là overkill.
> 2. Yêu cầu độ trễ cực thấp dưới 1 giây (Sub-second streaming / Low-latency OLTP) — lúc này cần Redis, HBase, hoặc Kafka State Store.

---

## 🛠️ BÀI TẬP THỰC CHIẾN — Thiết Kế Bảng Dân Số 100 Triệu Dân (Bộ Nội Vụ)

**Tình huống:**
- Bạn quản lý bảng dữ liệu CCCD của 100 triệu công dân lưu dưới dạng **Delta Lake** trên Cloud Storage / HDFS.
- Mỗi ngày có **500.000 công dân thay đổi địa chỉ thường trú hoặc làm lại thẻ CCCD**.
- Đồng thời, các hệ thống Cổng Dịch Vụ Công Quốc Gia truy vấn liên tục 24/7 để xác thực công dân.

**Câu hỏi bài tập:**

### Câu 1: Xử lý Cập nhật (UPDATE) trên Parquet thuần vs Delta Lake
Nếu dùng **Parquet thuần**, khi muốn cập nhật địa chỉ của 500.000 người, bạn phải làm gì với toàn bộ file 800GB? 
- *Học viên:* có thể phải chạy toàn bộ 800gb
- *Chuẩn hóa:* Parquet là file bất biến. Muốn sửa, bắt buộc phải đọc toàn bộ file/partition chứa dữ liệu lên RAM, sửa đổi, rồi ghi đè lại toàn bộ (Full rewrite).
Khi chuyển sang **Delta Lake**, lệnh `MERGE INTO` hoạt động dưới nắp ca-pô thế nào (Copy-on-Write)? 
- *Học viên:* merge into hoạt động bằng cách gom nhóm dữ liệu Z-order thành nhóm dữ liệu dạng ma trận giúp giảm bớt việc truy vấn đến những dữ liệu không liên quan theo trục x-y
- *Chuẩn hóa (Copy-on-Write 3 bước):* 
  1. **Scan:** Dùng Data Skipping (Min/Max stats) tìm đúng những file Parquet đang chứa 500.000 dòng cần update.
  2. **Rewrite:** Đọc những file này lên RAM, cập nhật dữ liệu, rồi ghi ra các file Parquet MỚI toanh. Các file không chứa dữ liệu cần sửa được giữ nguyên 100%.
  3. **Commit Log:** Ghi vào `_delta_log`: `remove` các file cũ và `add` các file mới.

### Câu 2: Sự cố ETL và Khắc phục sự cố bằng Time Travel
Lúc 02:00 sáng, một đoạn code ETL bị lỗi logic dẫn đến việc xóa nhầm toàn bộ cột `so_dien_thoai` của người dân tỉnh Bình Dương.
Đến 08:00 sáng, cán bộ phát hiện sự cố. Bạn dùng tính năng gì của Delta Lake để khôi phục lại dữ liệu nguyên vẹn lúc 01:59 sáng trong vòng 1 câu lệnh? Hãy viết câu lệnh SQL/PySpark đó.
- *Học viên:* mở transaction log, truy vấn đến thời điểm dữ liệu bị xóa, xác định thời điểm xóa, dùng time travel và khôi phục lại dữ liệu số điện thoại tại 1:59
- *Câu lệnh chuẩn hóa:*
  ```sql
  RESTORE TABLE dan_so TO TIMESTAMP AS OF '2026-09-21 01:59:00';
  ```

### Câu 3: Tối ưu hóa truy vấn xác thực CCCD
Người dân đi làm thủ tục hành chính thường tra cứu theo 2 tiêu chí: `so_cccd` và `ngay_cap`.
Hãy đề xuất câu lệnh tối ưu hóa tệp dữ liệu lưu trữ để khi tìm kiếm theo 2 cột này, Spark chỉ phải đọc vài megabyte thay vì quét toàn bộ 800GB.
- *Học viên:* phân chia dữ liệu theo xét theo 2 tiêu chí nhằm thực thi copy-on-write với câu lệnh OPTIMIZE dan_so ZORDER BY (so_cccd, ngay_cap)
- *Câu lệnh chuẩn hóa:*
  ```sql
  OPTIMIZE dan_so ZORDER BY (so_cccd, ngay_cap);
  ```
  *(Cơ chế: Gom cụm đa chiều dạng ma trận 2D, thu hẹp Min-Max stats của cả 2 cột trên từng file Parquet 128MB-1GB, giúp Spark Data Skipping bỏ qua 90-99% file).*
---

## 📝 Ghi Chú Cá Nhân

```
[Học viên điền vào đây]
```
