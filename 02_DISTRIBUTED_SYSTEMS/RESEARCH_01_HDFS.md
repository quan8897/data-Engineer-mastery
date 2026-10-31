# 🗄️ RESEARCH 01 — HDFS: KHI Ổ CỨNG ĐƠN KHÔNG CÒN ĐỦ

> **Task:** 2.1 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-03
> **Trạng thái:** ✅ Đã hoàn thành — 2026-09-07

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Hoàn thành bài này, bạn phải đạt được các năng lực cốt lõi:
1. **Tư duy Scale-out:** Giải thích được vì sao Scale-out (dùng hàng trăm commodity servers) tối ưu chi phí và mở rộng tốt hơn Scale-up (mua siêu máy chủ đắt đỏ) khi dữ liệu đạt quy mô Big Data.
2. **Kiến trúc Master-Worker:** Phân biệt rõ trách nhiệm của **NameNode** (quản lý metadata, namespace trong RAM) và **DataNode** (lưu trữ các block dữ liệu vật lý trên ổ cứng).
3. **Cơ chế Block & Replication:** Hiểu sâu tại sao HDFS chọn Block Size lớn (128MB) và Replication Factor = 3 để đảm bảo khả năng chịu lỗi (Fault-Tolerance) và tối ưu băng thông đọc tuần tự (Sequential I/O).
4. **Vận hành & Giới hạn:** Nhận diện điểm yếu SPOF (Single Point of Failure), cơ chế HA (Active-Standby), bài toán "Small Files Problem" và hiểu rõ bối cảnh vì sao Cloud Object Storage (S3, GCS) đang dần thay thế HDFS on-premise.

---

## 🧠 Framework 5 Tầng — HDFS

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không copy)*

```
[HDFS Là lưu trữ dữ liệu phân tán ở nhiều máy tính khác nhau, giải quyết bài toán chỉ lưu dữ liệu ở 1 máy tính, nhằm tối ưu chi phí nâng cấp và xử lý, nếu 1 máy hư thì hệ thống coi như sập]
```

### Tầng 2 — HOW (Kiến trúc)

#### NameNode
```
[NameNode lưu metadata (file nào → block nào → DataNode nào), không phải là nơi trực tiếp lưu dữ liệu.
Lưu ý quan trọng: Mặc định có 1 NameNode Active duy nhất → Nguy cơ SPOF. Cần HA (Active-Standby) để dự phòng. Secondary NameNode không phải là backup mà chỉ làm nhiệm vụ Checkpoint helper.]
```

#### DataNode
```
[NameNode không lưu dữ liệu thật mà lưu metadata/địa chỉ; dữ liệu thật được chia thành các block nằm trực tiếp trên đĩa cứng của các DataNode.]
```

#### Block & Replication
```
[Block là đơn vị lưu trữ vật lý cơ bản (mặc định 128MB). Replication Factor = 3 nghĩa là mỗi block sẽ được sao lưu thành 3 bản giống hệt nhau, phân bổ trên các DataNode khác nhau để đảm bảo khả năng chịu lỗi (fault-tolerance).]
```

### Tầng 3 — WHY
> *(Scale-up vs Scale-out: tại sao HDFS thắng khi dữ liệu rất lớn?)*

```
[Dữ liệu càng lớn thì chi phí scale-up (mua siêu máy chủ) tăng theo cấp số nhân và chạm trần vật lý. HDFS chọn scale-out (thêm nhiều máy tính bình thường - commodity hardware vào cluster), chi phí tăng tuyến tính và mở rộng gần như vô hạn.]
```

### Tầng 4 — FAILURE
> *(SPOF là gì? NameNode chết thì sao?)*

```
[SPOF là Single Point of Failure - điểm hỏng duy nhất khiến toàn bộ hệ thống sụp đổ. Nếu NameNode chết mà không có cấu hình HA (Standby), toàn bộ cluster bị tê liệt hoàn toàn vì không ai biết dữ liệu nằm ở DataNode nào, dù dữ liệu trên DataNode vẫn còn nguyên.]
```

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG dùng HDFS? Năm 2026 thực tế thế nào?)*

```
Không dùng HDFS khi:
1. Dữ liệu nhỏ (< vài TB) → 1 server đơn lẻ hoặc PostgreSQL là đủ, không tốn công vận hành cluster.
2. Cần độ trễ cực thấp (OLTP, truy vấn real-time < 10ms) → HDFS thiết kế cho throughput lớn (batch read/write tuần tự), không tối ưu cho random access độ trễ mili-giây.
3. Vấn đề Small Files Problem: Quá nhiều file nhỏ (vài KB - vài MB) sẽ làm tràn RAM NameNode vì mỗi file/block chiếm ~150 bytes metadata.
4. Môi trường Cloud-native hiện đại: Chi phí vận hành cluster HDFS 24/7 rất tốn kém so với Cloud Object Storage (AWS S3, Google Cloud Storage) kết hợp Storage-Compute Separation.
```

---

## 🛠️ BÀI TẬP — Tính Toán HDFS Cho Bộ Nội Vụ

**Tình huống:**
- File dữ liệu dân số 63 tỉnh = **800GB**
- Cluster: **10 DataNode**, mỗi máy có **1TB ổ cứng**
- Replication Factor: **3**
- Block size: **128MB**

**Kết quả bài làm:**

### Câu 1: File 800GB chia thành bao nhiêu block?
```
800 GB = 800 * 1024 MB = 819.200 MB
Số blocks = 819.200 MB / 128 MB = 6.400 blocks.
```

### Câu 2: Tổng dung lượng thực tế chiếm trên cluster (vì replication = 3)?
```
Dung lượng gốc = 800 GB.
Dung lượng thực tế chiếm trên cluster = 800 GB * 3 = 2.400 GB (khoảng 2,34 TiB hay 2,4 TB).
(Hoặc: 6.400 blocks * 128 MB * 3 = 2.457.600 MB = 2.400 GB).
```

### Câu 3: Cluster 10 máy × 1TB có đủ chỗ không? Dư bao nhiêu?
```
Tổng dung lượng cluster = 10 máy * 1 TB = 10 TB.
Dữ liệu chiếm = 2,4 TB (hoặc 2,34 TiB).
Kết luận: ĐỦ CHỖ. Còn dư khoảng 7,6 TB cho các dữ liệu hoặc tác vụ phát sinh.
```

### Câu 4: Nếu DataNode số 5 chết đột ngột, HDFS mất dữ liệu không? Cơ chế phục hồi thế nào?
```
Dữ liệu KHÔNG bị mất vì mỗi block trên DataNode 5 đều có 2 bản sao khác nằm ở các DataNode còn sống.
Cơ chế tự phục hồi (Self-healing):
1. Heartbeat: DataNode 5 ngừng gửi heartbeat (nhịp tim định kỳ 3 giây). Sau timeout (thường ~10 phút 30 giây), NameNode xác định DataNode 5 đã chết.
2. Under-replicated blocks: NameNode quét thấy các block trên DataNode 5 bị tụt replication factor từ 3 xuống 2.
3. Re-replication: NameNode ra lệnh cho các DataNode đang giữ bản sao còn lại nhân bản (copy) block đó sang một DataNode khỏe mạnh khác để đưa replication factor trở về 3. Quá trình này diễn ra tự động ngầm dưới nền.
```

### Câu 5 — Sơ đồ NameNode Metadata cho file `/data/dan_so.csv`
```
NameNode lưu trong RAM:
/data/dan_so.csv 
  Block 0001 → DataNode 3, DataNode 7, DataNode 9
  Block 0002 → DataNode 1, DataNode 5, DataNode 8
  Block 0003 → DataNode 2, DataNode 6, DataNode 4
  ... (tổng cộng 6.400 blocks ánh xạ tới 10 DataNodes)
```

---

## 📝 Ghi Chú Cá Nhân & Đúc Kết

```
- Quy đổi đơn vị: Phải nhân 1024 khi đổi từ GB sang MB trước khi tính số Block!
- NameNode quản lý toàn bộ File-to-Block-to-DataNode mapping trong RAM.
- DataNode lưu raw block data trên disk cục bộ.
- Chống mất dữ liệu nhờ Replication + Heartbeat + Re-replication.
```
