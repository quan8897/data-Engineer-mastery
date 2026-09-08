# 📚 THAM KHẢO — BÀI GIẢNG SENIOR DATA ENGINEER: HDFS

> **Loại file:** Tài liệu tham khảo — ĐỌC SAU khi đã tự điền Framework 5 Tầng
> **Nguồn:** Học viên tổng hợp từ nghiên cứu độc lập
> **Cảnh báo:** Đọc tài liệu này KHÔNG thay thế được việc làm bài tập và kiểm tra

---

# BÀI GIẢNG SENIOR DATA ENGINEER — HDFS

## 0. Mục tiêu bài học

Sau bài này, bạn không chỉ trả lời được **"HDFS là gì?"** mà phải hiểu được:
- Tại sao HDFS ra đời?
- NameNode và DataNode làm gì?
- Block và Replication hoạt động thế nào?
- Data Locality là gì?
- Small Files Problem nguy hiểm thế nào?
- Khi nào KHÔNG nên dùng HDFS?
- HDFS liên quan thế nào đến Spark, Data Lake và Medallion Architecture?

---

## 1. Vấn đề: Scale-up vs Scale-out

```text
Scale-up (cách cũ):
1 server → nâng cấp → giới hạn, đắt, SPOF

Scale-out (HDFS):
Nhiều máy thường → tổng hợp thành 1 hệ thống lớn
→ Không giới hạn lý thuyết, giá tuyến tính
```

## 2. HDFS là gì?

**HDFS — Hadoop Distributed File System** là hệ thống file phân tán thiết kế để lưu dữ liệu rất lớn trên nhiều máy, biến nhiều máy tính thành một hệ thống lưu trữ có vẻ như một filesystem lớn.

## 3. Mental Model — Kho hàng

| HDFS | Kho hàng |
|---|---|
| NameNode | Người quản lý kho (sổ ghi vị trí) |
| DataNode | Kho chứa hàng thật |
| Block | Kiện hàng |
| Metadata | Sổ ghi "kiện ở kho nào" |
| Replication | Nhiều bản sao của kiện hàng |

## 4. Kiến trúc: NameNode + DataNode

```text
            NameNode
        (Chỉ lưu METADATA)
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
DataNode 1  DataNode 2  DataNode 3
(Lưu dữ liệu thật theo block)
```

**NameNode lưu gì?**
```text
/data/dan_so.csv
  Block 1 → DN3, DN7, DN9
  Block 2 → DN1, DN5, DN8
  ...
```
→ KHÔNG lưu dữ liệu thật. Chỉ lưu "dữ liệu ở đâu".

**DataNode làm gì?**
- Lưu block thật (128MB mỗi block)
- Gửi Heartbeat cho NameNode (chứng minh còn sống)
- Báo cáo danh sách block đang có

## 5. Block — đơn vị lưu trữ

```text
File 800GB ÷ Block 128MB = 6.400 blocks
→ Phân phối lên 10 DataNode → mỗi DataNode ~640 blocks
```

**Tại sao chia block?**
1. Phân phối dữ liệu đều lên nhiều máy
2. Xử lý song song (Spark xử lý từng block trên máy chứa nó)
3. Fault tolerance (mất 1 DataNode không mất toàn bộ file)

## 6. Replication Factor 3

```text
Block A:
  → DataNode 1 (bản gốc)
  → DataNode 4 (copy 1)
  → DataNode 8 (copy 2)

DataNode 1 chết → DataNode 4 + 8 vẫn còn
→ HDFS tự tạo thêm 1 copy để đủ 3
```

**Chi phí:** 800GB × 3 = 2.4TB dung lượng thực tế

## 7. SPOF — Điểm yếu của NameNode

```text
NameNode chết → không biết block nào ở đâu → cluster tê liệt
Dù 10 DataNode hoạt động bình thường → vô dụng

Giải pháp: HA Mode (Active + Standby NameNode)
Active chết → Standby tự động lên thay (Failover)
```

**FsImage + EditLog:**
```text
FsImage = "ảnh chụp" metadata tại một thời điểm
EditLog = "nhật ký" các thay đổi sau đó
Current Metadata = FsImage + EditLog
```

## 8. Data Locality

```text
Cách ngây thơ: DataNode → (1TB qua network) → Compute Server
Cách HDFS: Spark chạy TRÊN DataNode → đọc data local, không qua network

"Move Computation to Data" thay vì "Move Data to Computation"
```

## 9. Rack Awareness

```text
BAD: 3 replica cùng Rack 1 → Rack chết → mất hết
GOOD:
  Block A → DN1 (Rack 1)
  Block A → DN5 (Rack 2)
  Block A → DN9 (Rack 3)
→ 1 rack chết → vẫn còn 2 replica
```

## 10. Small Files Problem

```text
1,000,000 files × 1KB = 1GB dữ liệu
→ NameNode phải quản lý 1 triệu metadata entries
→ NameNode RAM bị ăn hết → cluster gặp vấn đề

Giải pháp: Compaction — gộp nhiều file nhỏ thành Parquet file lớn
```

## 11. HDFS vs S3

| | HDFS | S3/GCS |
|---|---|---|
| Compute + Storage | Dính chặt nhau | Tách biệt hoàn toàn |
| Scale | Thêm DataNode vật lý | Vô hạn, tự động |
| Chi phí | Trả máy chủ 24/7 | Trả theo GB dùng |
| Năm 2026 | Dùng trong on-premise | Chiếm 90% dự án mới |

## 12. HDFS trong Medallion Architecture

```text
HDFS = Storage Technology (công nghệ lưu trữ)
Medallion = Architecture Pattern (mẫu kiến trúc)

HDFS
├── bronze/   ← Raw data
├── silver/   ← Cleaned data
└── gold/     ← Business metrics

ĐỪNG NHẦM: HDFS không phải Medallion
```

## 13. Khi nào KHÔNG dùng HDFS

| Không dùng khi | Dùng gì thay |
|---|---|
| OLTP, random write | PostgreSQL, MySQL |
| Cần latency < 10ms | Redis, SSD local |
| Nhiều file nhỏ | Object Storage (S3) |
| Cloud-native | S3 + Parquet/Iceberg |
| Team nhỏ | Serverless (Athena, BigQuery) |

## 14. Câu hỏi Senior DE trước khi chọn HDFS

```
1. Data Volume? (10GB? 10TB? 10PB?)
2. Data Velocity? (MB/s hay GB/s?)
3. Workload? (Batch? Streaming? OLTP? Analytics?)
4. Latency Requirement? (ms? s? phút? giờ?)
5. Deployment? (On-premise? Cloud? Hybrid?)
6. Storage-Compute Separation cần không?
7. Operational complexity team có handle được không?
```

## 15. Lab Commands HDFS

```bash
# Tạo thư mục
hdfs dfs -mkdir /data

# Upload file
hdfs dfs -put orders.csv /data/

# Xem file
hdfs dfs -ls /data

# Xem blocks và locations
hdfs fsck /data/orders.csv -files -blocks -locations

# Đặt replication factor
hdfs dfs -setrep 3 /data/orders.csv
```

## 16. Bài tập tư duy Senior

**Bài 1:** File 1TB, Block 128MB → bao nhiêu block?
**Bài 2:** Data 1TB, Replication 3 → Physical Storage?
**Bài 3:** Block A ở DN1, DN2, DN3. DN2 chết → mất không? HDFS làm gì?
**Bài 4:** 3 replica ở Rack 1. Rack 1 chết → vấn đề gì?
**Bài 5:** 500M JSON files × 2KB vs 10M Parquet × 100MB → tác động lên NameNode?

---

## Knowledge Map

```text
Distributed Systems → HDFS → NameNode + DataNode + Block + Replication
                           → Fault Tolerance + Data Locality + Rack Awareness
                           → Small Files Problem
                           → Spark → Data Lake → Lakehouse → Cloud Object Storage
```

---

> **Nhớ 5 điều này là đủ:**
> 1. HDFS = Distributed File System
> 2. File → Blocks → phân phối lên nhiều DataNode
> 3. NameNode = quản lý metadata, KHÔNG chứa dữ liệu thật
> 4. Replication 3 = Fault Tolerance
> 5. Senior DE hỏi "Workload này cần gì?" trước khi chọn HDFS
