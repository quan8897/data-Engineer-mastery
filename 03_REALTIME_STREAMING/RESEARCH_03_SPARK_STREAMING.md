# ⚡ RESEARCH 03 — STREAM PROCESSING VỚI SPARK STRUCTURED STREAMING

> **Task:** 3.3 | **Module:** 3 — Real-time Streaming & Integration  
> **Ngày bắt đầu:** 2026-10-12  
> **Trạng thái:** 🔄 Đang học  

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Sau khi hoàn thành bài nghiên cứu này, bạn làm chủ các năng lực cốt lõi:
1. **Triết lý Bảng Vô Hạn (Unbounded Table):** Hiểu cách Spark Structured Streaming trừu tượng hóa dòng dữ liệu vô tận thành một bảng liên tục được append dữ liệu mới.
2. **Cơ chế Micro-batch vs Continuous:** Nắm vững cách Spark chia nhỏ stream thành các micro-batch cực nhanh (độ trễ ~100ms) để tái sử dụng toàn bộ sức mạnh tối ưu hóa của Catalyst Optimizer từ Spark SQL.
3. **Phân biệt 3 loại thời gian:** Phân biệt rạch ròi **Event Time** (thời điểm xảy ra sự kiện ở đời thực), **Ingestion Time** (thời điểm vào Kafka), và **Processing Time** (thời điểm worker Spark bắt đầu tính toán).
4. **Watermarking & Late Data:** Hiểu cơ chế Watermark đóng vai trò "hạn chót" để chấp nhận dữ liệu đến muộn và tự động dọn dẹp RAM (State Store) chống sập hệ thống (OOM).
5. **3 Chế độ đầu ra (Output Modes):** Sử dụng chính xác `Append`, `Update`, và `Complete` tùy theo bài toán có hay không có Aggregation/Windowing.

---

## 🔗 Kết nối kiến thức cũ

```
Module 2 — Task 2.3 (Spark Internals):
  Bạn đã biết Spark xử lý dữ liệu Batch qua DataFrame, Catalyst Optimizer và DAG.
  → Spark Structured Streaming mang 100% cú pháp DataFrame đó sang thế giới Streaming! Viết code streaming giống hệt như viết code batch.

Task 3.1 & 3.2 (Kafka & CDC Debezium):
  Kafka là nơi chứa hàng triệu event biến động được Debezium bơm vào liên tục.
  → Spark Structured Streaming đứng ở đầu ra của Kafka, đóng vai trò là Consumer siêu mạnh mẽ để tính toán, làm giàu dữ liệu và đẩy xuống Delta Lakehouse.
```

---

## 📖 Từ Điển Thuật Ngữ Cốt Lõi (Key Terminology & IPA Pronunciation)

| Thuật ngữ Tiếng Anh | Phiên âm IPA / Loại từ | Nghĩa đen đời thường (Bẻ khóa) | Nghĩa kỹ thuật chuyên ngành cần nhớ |
|---|---|---|---|
| **Stream Processing** | /striːm ˈprəʊ.ses.ɪŋ/ (n) | Xử lý dòng suối | Xử lý dữ liệu liên tục theo thời gian thực ngay khi từng sự kiện vừa phát sinh. |
| **Unbounded Table** | /ʌnˈbaʊn.dɪd ˈteɪ.bəl/ (n) | Cái bàn không có ranh giới/đáy | Mô hình tư duy cốt lõi của Spark: Coi dòng stream như một bảng dữ liệu vô tận, dòng mới liên tục được thêm vào đáy. |
| **Micro-batch** | /ˈmaɪ.krəʊ bætʃ/ (n) | Lô hàng siêu nhỏ | Cơ chế gom các sự kiện trong một khoảng thời gian cực ngắn (vd: 500ms) thành một mẻ nhỏ để xử lý bằng Spark Engine. |
| **Event Time** | /ɪˈvent taɪm/ (n) | Giờ xảy ra sự kiện | Thời điểm thực tế sự kiện diễn ra tại thiết bị người dùng (được nhúng trong dữ liệu, vd: lúc quẹt thẻ ở cây ATM). |
| **Processing Time** | /ˈprəʊ.ses.ɪŋ taɪm/ (n) | Giờ xử lý | Thời điểm đồng hồ của máy chủ Spark thực sự chạm tay vào xử lý bản tin đó. |
| **Late Data** | /leɪt ˈdeɪ.tə/ (n) | Dữ liệu đến trễ | Bản tin bị gửi muộn hơn bình thường do mạng di động yếu, nghẽn mạng hoặc thiết bị bị mất sóng tạm thời. |
| **Watermark** | /ˈwɔː.tə.mɑːk/ (n) | Vạch ngấn nước lũ | Mốc thời gian "hạn chót" cho phép dữ liệu đến muộn. Dữ liệu trễ hơn vạch này sẽ bị vứt bỏ để giải phóng RAM. |
| **State Store** | /steɪt stɔːr/ (n) | Kho lưu trữ trạng thái | Bộ nhớ RAM (hoặc RocksDB trên đĩa) lưu giữ các phép tính tích lũy trung gian (vd: tổng tiền tạm tính trong 10 phút). |
| **Tumbling Window** | /ˈtʌm.blɪŋ ˈwɪn.dəʊ/ (n) | Cửa sổ lộn nhào (không đè nhau) | Cửa sổ thời gian cố định, không chồng lấn (vd: 0h-1h, 1h-2h, 2h-3h). |
| **Sliding Window** | /ˈslaɪ.dɪŋ ˈwɪn.dəʊ/ (n) | Cửa sổ trượt (chồng lấn nhau) | Cửa sổ thời gian trượt đều đặn và chồng lên nhau (vd: cửa sổ 10 phút, trượt mỗi 5 phút một lần). |
| **Checkpoint Directory** | /ˈtʃek.pɔɪnt daɪˈrek.tər.i/ (n) | Thư mục trạm kiểm soát | Thư mục trên HDFS/S3 lưu trữ tiến độ offset và state, giúp stream tự hồi phục chính xác điểm dừng khi server bị crash. |
| **Output Mode** | /ˈaʊt.pʊt məʊd/ (n) | Chế độ xuất kết quả | Cách Spark ghi kết quả của từng micro-batch ra ngoài: `Append` (chỉ dòng mới), `Update` (dòng thay đổi), `Complete` (toàn bộ bảng). |

---

## 🧠 Framework 5 Tầng — Spark Structured Streaming

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không dùng thuật ngữ rườm rà)*

```
[Học viên điền vào đây]:

```

---

### Tầng 2 — HOW (Cơ chế hoạt động & Cú pháp kỹ thuật)

#### 1. Cú pháp cơ bản: `readStream` $\rightarrow$ `writeStream`
```python
# Đọc dòng stream từ Kafka:
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "cdc.db_danso.nhan_khau") \
    .load()

# Xử lý và ghi ra Delta Lake:
query = df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start("/path/to/delta/table")
```

#### 2. Phân biệt 3 Chế độ đầu ra (Output Modes)
```
[Học viên điền vào đây: Phân tích sự khác biệt giữa 3 chế độ:
1. Append Mode: Khi nào được dùng? Tại sao khi có phép tính tổng hợp (Aggregation) mà không có Watermark thì Spark CẤM dùng Append?
2. Update Mode: Xuất ra những dòng nào? Khác gì với Append?
3. Complete Mode: Xuất ra những dòng nào? Tại sao chế độ này dễ làm sập bộ nhớ nếu stream chạy qua nhiều năm?]
```

#### 3. Cơ chế Cửa sổ (Windowing) & Watermark
```
[Học viên điền vào đây:
- Cú pháp hàm window(): groupBy(window(col("timestamp"), "10 minutes", "5 minutes"))
- Cú pháp withWatermark(): withWatermark("timestamp", "10 minutes")
- Vẽ sơ đồ hoặc giải thích cách vạch Watermark di chuyển theo Event Time lớn nhất]
```

---

### Tầng 3 — WHY
> *(Tại sao trong bài toán thời gian thực, Event Time và Watermark là sự sống còn?)*

```
[Học viên điền vào đây: Phân tích 2 câu hỏi sống còn:
1. Tại sao KHÔNG ĐƯỢC dùng Processing Time để tính toán số liệu kinh doanh? Ví dụ: Nếu một giao dịch xảy ra lúc 23h59 ngày 31/12/2026, nhưng do nghẽn mạng nên 00h02 ngày 01/01/2027 Spark mới nhận được. Nếu dùng Processing Time thì doanh thu bị ghi sai năm tài chính như thế nào?
2. Tại sao nếu không có Watermark, hệ thống Stateful Streaming chắc chắn sẽ bị sập vì lỗi Out Of Memory (OOM)?]
```

---

### Tầng 4 — FAILURE & CẠM BẪY PRODUCTION
> *(Những thảm họa thực tế khi vận hành Spark Streaming)*

```
[Học viên điền vào đây: Phân tích 3 sự cố kinh điển:
1. Thảm họa State Store Bloat: Khi khoảng thời gian Watermark đặt quá dài (ví dụ: cho phép trễ 7 ngày) trong hệ thống hàng triệu giao dịch/giây, chuyện gì sẽ xảy ra với RAM của Executor?
2. Dữ liệu đến trễ bị "bốc hơi" (Silently Dropped): Khi một sự kiện có Event Time nằm ngoài vạch Watermark, Spark xử lý sự kiện đó như thế nào? Có báo lỗi không hay âm thầm bỏ qua?
3. Cạm bẫy hỏng Checkpoint Directory: Khi bạn thay đổi code logic trong hàm transform giữa chừng rồi khởi động lại job Spark từ thư mục checkpoint cũ, tại sao job bị crash? Khi nào bắt buộc phải xóa checkpoint làm lại từ đầu?]
```

---

### Tầng 5 — TRADE-OFF (Khi nào KHÔNG DÙNG Spark Streaming?)

```
[Học viên điền vào đây:
1. So sánh đối đầu Spark Structured Streaming vs Apache Flink:
   - Spark (Micro-batch): Độ trễ ~100ms.
   - Flink (Native Event-by-event): Độ trễ ~1ms (Sub-millisecond).
   - Trong bài toán nào (ví dụ: giao dịch tài chính cao tần High-Frequency Trading, điều khiển tên lửa) thì Spark Streaming hoàn toàn không đủ tiêu chuẩn và buộc phải dùng Flink?
2. Khi nào một job Batch chạy định kỳ 15 phút bằng Spark Batch lại tốt hơn, rẻ hơn và ít lỗi hơn việc duy trì một job Spark Streaming chạy 24/7?]
```

---

## 🛠️ TÌNH HUỐNG THỰC CHIẾN — Phát Hiện Gian Lận Quẹt Thẻ CCCD Thời Gian Thực

**Bối cảnh:**
- Cổng dịch vụ công quốc gia tiếp nhận sự kiện xác thực thẻ CCCD từ khắp các bệnh viện và chi nhánh ngân hàng trên toàn quốc.
- Hacker thực hiện hành vi gian lận: Dùng cùng 1 mã thẻ CCCD quẹt tại 2 địa điểm cách nhau 500km chỉ trong vòng 10 phút.

**Nhiệm vụ của bạn:**
1. Thiết kế câu truy vấn Spark Streaming sử dụng **Sliding Window (10 phút, trượt 2 phút)** kèm **Watermark 5 phút** để phát hiện các thẻ CCCD có số lần quẹt $\ge 2$ tại các địa điểm khác nhau.
2. Trình bày cách chọn `outputMode` và giải thích lý do lựa chọn.

---

*Tài liệu nghiên cứu Task 3.3 — Data Engineering Mastery*  
*Bắt đầu phiên học: 2026-10-12*
