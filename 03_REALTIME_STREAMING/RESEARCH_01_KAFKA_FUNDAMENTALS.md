# ⚡ RESEARCH 01 — REAL-TIME STREAMING: APACHE KAFKA FUNDAMENTALS

> **Task:** 3.1 | **Module:** 3 — Real-time Streaming & Integration
> **Ngày bắt đầu:** 2026-09-22
> **Trạng thái:** ✅ Đã hoàn thành (Đạt sát hạch xuất sắc 8.9/10) - 1/10/2026

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Sau khi hoàn thành bài nghiên cứu này, bạn phải làm chủ các năng lực cốt lõi:
1. **Kiến trúc Pub/Sub & Sự cần thiết của Message Broker:** Phân biệt được điểm yếu chí mạng của API REST/Direct DB connection khi chịu tải hàng triệu request/s; hiểu tại sao Kafka là "xương sống đệm" (Decoupling & Backpressure) của toàn bộ hệ thống dữ liệu quốc gia.
2. **Giải phẫu Topic & Partition:** Hiểu cấu trúc phân vùng vật lý (Partition), Distributed Commit Log trên đĩa, thứ tự ghi tuần tự (Append-only Sequential Write), và tại sao Partition là đơn vị co giãn (Scalability) của Kafka.
3. **Cơ chế Partitioning & Message Ordering:** Hiểu rõ cách Producer đẩy tin nhắn: `Key = null` (Round-Robin) vs `Key != null` (Hashing key). Nắm vững nguyên tắc: Kafka CHỈ bảo đảm thứ tự (Ordering) trên CÙNG MỘT PARTITION, không bảo đảm trên toàn Topic.
4. **Consumer Group & Cân bằng tải (Rebalance):** Cơ chế chia việc giữa các Consumer trong cùng một nhóm; quan hệ 1:1 giữa Consumer và Partition; hiện tượng Rebalancing khi có consumer chết hoặc join mới.
5. **Độ tin cậy & Bền vững (Replication & `acks`):** Leader/Follower replica, In-Sync Replicas (ISR), các mức cam kết của Producer (`acks=0`, `acks=1`, `acks=all`).

---

## 🔗 Kết nối kiến thức cũ

```
Task 2.1 - 2.4 (BATCH COMPUTING & STORAGE):
  HDFS/S3 + Spark + Delta Lake: Xử lý theo lô (Hàng giờ / Hàng ngày), độ trễ phút/giờ.
  → Nhưng nếu người dân quẹt thẻ CCCD tại sân bay hoặc chuyển tiền ngân hàng, 
    họ KHÔNG THỂ chờ 1 giờ để Spark Batch chạy xong!

Task 3.1 (REAL-TIME STREAMING):
  APACHE KAFKA: Hấp thụ (Ingest) hàng triệu sự kiện/giây với độ trễ tính bằng mili-giây (Low Latency).
  → Đóng vai trò là "Trạm trung chuyển dữ liệu thời gian thực", tiếp thức ăn cho Flink/Spark Streaming và đẩy về Lakehouse!
```

---

## 📖 Từ Điển Thuật Ngữ Cốt Lõi (Key Terminology for Task 3.1)

| Thuật ngữ Tiếng Anh | Nghĩa tiếng Việt | Bản chất kỹ thuật cần nhớ |
|---|---|---|
| **Event / Message** | Bản tin / Sự kiện | Một bản ghi gồm Key, Value, Timestamp, Headers đại diện cho 1 hành động đã diễn ra trong thực tế. |
| **Topic** | Chủ đề dữ liệu | Kênh phân loại logic chứa các sự kiện cùng thể loại (vd: `giao_dich_cccd`, `log_dang_nhap`). |
| **Partition** | Phân vùng vật lý | Mỗi Topic chia thành nhiều Partition. Mỗi Partition là 1 file log ghi tuần tự độc lập trên đĩa. |
| **Producer** | Bên phát tin | Ứng dụng/dịch vụ đẩy dữ liệu vào các Topic của Kafka. |
| **Consumer** | Bên nhận tin | Ứng dụng/dịch vụ đọc dữ liệu từ Topic ra để xử lý hoặc lưu trữ. |
| **Consumer Group** | Nhóm tiêu thụ | Tập hợp các Consumer cùng chia nhau đọc các Partition của một Topic để xử lý song song. |
| **Offset** | Chỉ số vị trí | Số nguyên tăng dần duy nhất gán cho mỗi message trong một Partition, đánh dấu vị trí đọc/ghi. |
| **Broker** | Máy chủ Kafka | Một server chạy tiến trình Kafka, quản lý lưu trữ Partition và phục vụ Producer/Consumer. |
| **Cluster** | Cụm máy chủ | Tập hợp nhiều Broker phối hợp với nhau để đạt tính sẵn sàng cao (High Availability). |
| **Replication Factor** | Hệ số sao chép | Số lượng bản sao lưu trữ của mỗi Partition trên các Broker khác nhau để chống mất dữ liệu khi sập node. |
| **Leader / Follower** | Nút chủ / Nút tớ | Broker chứa Leader Partition xử lý toàn bộ Read/Write; Follower chỉ đồng bộ ngầm dữ liệu từ Leader. |
| **ISR (In-Sync Replicas)** | Danh sách bản sao đồng bộ | Tập hợp các Follower đang sao chép bám sát kịp thời với Leader. |
| **Backpressure / Buffer** | Đệm chống sốc tải | Khả năng hấp thụ lượng tin nhắn khổng lồ gửi tới dồn dập mà không làm sập các hệ thống hạ nguồn chậm chạp. |

---

## 🧠 Framework 5 Tầng — Apache Kafka

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không copy)*

```
[Học viên điền vào đây]là một hệ thống lưu trữ và xử lý phân tán, gồm các nhóm cluster chứa các máy chủ broker, là nơi tiếp nhận các sự kiện từ các ứng dụng, API, các giao dịch, producer và consumer đọc các partition để thực hiện khai thác dữ liệu cho tính toán, phân tích, bảo mật, ....// là lớp trung gian điều phối dữ liệu
```

---

### Tầng 2 — HOW (Kiến trúc & Cơ chế vận hành)

#### 1. Cơ chế Partition & Thứ tự tin nhắn (Message Ordering)
```
[Học viên mô tả:
- Tại sao Kafka không lưu toàn bộ 1 Topic vào 1 file duy nhất mà phải chia thành nhiều Partition? đảm bảo tính dự phòng, cũng như xử lý song song thay vì thực hiện tuần tự, việc chia vào nhiều partition giúp dữ liệu được consumer khai thác nhanh hơn
- Nếu Producer gửi 100 giao dịch của cùng một công dân (có số_cccd làm Key), các giao dịch này sẽ bay vào cùng nhiều partition với sự kiện gắn liền được đảm bảo về thứ tự tuần tự (ofset)
- Kafka bảo đảm thứ tự tin nhắn (First-In, First-Out) trong phạm vi nào: Toàn Topic hay từng Partition?] chỉ đảm bảo thứ tự trong partition chứ không đảm bảo thứ tự trong topic, trong partition các sự kiện được lưu theo thứ tự gọi là ofset đảm bảo theo thứ tự
```

#### 2. Cơ chế Consumer Group & Xử lý song song
```
[Học viên giải thích:
- Một Topic có 4 Partition. Nếu trong 1 Consumer Group có 2 Consumer (C1, C2), Kafka sẽ phân bổ đọc thế nào?c1 đọc p1, p2; c2 đọc p3, p4
- Nếu nhóm này tăng lên 6 Consumer (C1 -> C6) cho 4 Partition, chuyện gì xảy ra với 2 Consumer thừa?tốn tài nguyên, không cần thiết, chúng ở trạng thái nhàn rỗi, c1-p1; c2-p2; c3-p3; c4-p4; c5, c6 nhàn rỗi
- Nếu 1 Consumer bị crash đột ngột, cơ chế Rebalance hoạt động ra sao?]Rebalance cân bằng lại bằng cách chuyển việc đọc partion của consumer bị crash sang consumer khác, vẫn đảm bảo việc thực thi
```

#### 3. Độ tin cậy dữ liệu: `acks` và ISR
```
[Học viên phân biệt 3 mức cấu hình acks của Producer:
- acks = 0: có thể gây ra mất dữ liệu
- acks = 1: có thể gây ra trùng lặp dữ liệu
- acks = all (-1) kết hợp min.insync.replicas:
Khi nào hệ thống ngân hàng hoặc dữ liệu công dân BẮT BUỘC dùng acks = all?] acks=all là trạng thái Leader và Follower cùng phải thực hiện xác nhận, cần được mô tả cụ thể kèm min.insync.replicas;trường hợp ISR bị thu hẹp còn 1 mình Leader → acks=all mất ý nghĩa và enable.idempotence=true — giải pháp triệt để cho trùng lặp do retry.
```

---

### Tầng 3 — WHY
> *(Tại sao hệ thống Microservices & Big Data không kết nối trực tiếp với nhau mà phải có Kafka đứng giữa?)*

```
[Học viên điền vào đây: Phân tích 3 yếu tố: Decoupling (Tách rời phụ thuộc), Buffer/Backpressure (Chống sốc tải), và Fan-out (1 bên phát, nhiều bên đọc độc lập).] khi kết nối trực tiếp phía producer làm việc trực tiếp với consumer, ok làm việc được đó, nhưng khi số lượng 2 bên tăng lên, các giao dịch tăng lên, nhiều task cần đọc và xử lý đồng thời, sẽ gây ra rối hệ thống, sự chằng chịt thực thi, nếu chỉ cần thay đổi cấu trúc dữ liệu phía producer thì có thể toàn bộ consumer phải hiệu chỉnh theo, gây tê liệt hệ thống// kaffka đứng giữa như một lớp trung gian có nhiệm vụ nhận dữ liệu từ producer, có khả năng xử lý, lưu trữ và cung cấp cho consumer đọc và thực hiện các nhiệm vụ//Kafka cho phép 1 Topic được đọc bởi nhiều Consumer Group hoàn toàn độc lập.AI đối soát, Bộ Công An, Delta Lake có thể cùng đọc 1 Topic mà không ảnh hưởng nhau — Producer chỉ cần ghi 1 lần, tất cả cùng nhận.
```

---

### Tầng 4 — FAILURE
> *(Những thảm họa thực tế với Kafka)*

```
[Học viên hoàn thiện]:
1. Consumer Lag:
- Định nghĩa: Lag = Log End Offset (LEO) - Current Offset (khoảng cách giữa tin mới nhất ghi vào Partition và tin cuối cùng Consumer đã commit).
- Hệ quả khi Producer ghi nhanh gấp 10 lần Consumer:
  + Dữ liệu bị trễ nghiêm trọng (Data Latency), báo cáo và cảnh báo không còn tính thời gian thực.
  + Mất trắng dữ liệu do chính sách dọn dẹp (Retention Policy): Nếu trễ quá hạn (vd retention.ms = 7 ngày), Kafka tự xóa dữ liệu cũ trên đĩa dù Consumer chưa kịp đọc.
  + Tràn ổ cứng Broker (Disk Pressure) nếu cố tăng thời gian lưu trữ để đợi Consumer.
  + Trigger Rebalance liên tục: Consumer xử lý quá tải lâu hơn max.poll.interval.ms mà không gọi poll() sẽ bị Coordinator coi là đã chết và kick ra ngoài, gây gián đoạn toàn bộ Consumer Group.
- Khắc phục: Tăng số Partition và tăng Consumer tương ứng để xử lý song song; tối ưu code Consumer (Async/Worker pool, batching); scale hạ tầng (CPU/RAM/Pod).

2. Poison Pill & DLQ:
- Poison Pill: Bản tin lỗi định dạng (sai cú pháp JSON, thiếu trường, gây crash runtime).
- Cơ chế gây nghẽn: Đọc tin lỗi -> crash trước khi commit offset -> restart lại đọc đúng tin đó -> crash tiếp (Infinite Crash-Loop) làm tắc nghẽn toàn bộ Partition, chặn đứng các tin nhắn hợp lệ phía sau và khiến Lag tăng vọt.
- Giải pháp Dead Letter Queue (DLQ): "Cách ly bệnh nhân, cứu lấy đoàn tàu":
  + Bọc try-catch, bắt Unrecoverable Error (DeserializationException).
  + Thử lại với Exponential Backoff (vd 3 lần).
  + Nếu vẫn lỗi, đóng gói message kèm stack trace gửi sang DLQ Topic riêng (vd: orders.DLQ).
  + Commit Offset để tiến lên đọc tiếp các bản tin hợp lệ phía sau bình thường.
  + Đội kỹ thuật kiểm tra và xử lý lỗi trên DLQ Topic độc lập sau.
```

---

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG NÊN dùng Apache Kafka?)*

```
[Học viên điền vào đây: Kafka quá phức tạp và tốn kém cho hệ thống nhỏ — khi chỉ cần xử lý vài trăm events/giây, một cái RabbitMQ hay PostgreSQL queue là quá đủ."]
```

---

## 🛠️ BÀI TẬP THỰC CHIẾN — Thiết Kế Luồng Xử Lý Sự Kiện Quẹt Thẻ CCCD Toàn Quốc

**Bối cảnh:**
- Cả nước có hàng chục nghìn cổng quét CCCD (sân bay, ga tàu, bệnh viện, cơ quan hành chính) gửi tín hiệu xác thực về hệ thống trung tâm.
- Cao điểm: **200.000 lượt quét thẻ mỗi giây (200.000 events/sec)**.
- Hạ nguồn gồm 3 hệ thống tiêu thụ:
  1. Dịch vụ AI đối soát khuôn mặt (chạy mất 50ms/lần).
  2. Dịch vụ chống tội phạm truy nã Bộ Công An (cần cảnh báo dưới 10ms).
  3. Dịch vụ lưu trữ Delta Lake (Ghi batch sau mỗi 5 phút).

**Câu hỏi bài tập:**
1. Hãy thiết kế **Topic** và chọn **Partition Key** cho sự kiện quẹt thẻ này. Nếu chọn `Key = so_cccd`, điều này mang lại lợi ích gì cho việc theo dõi lịch sử di chuyển theo đúng thứ tự thời gian của từng công dân?
3 topic trong đó lần lượt đại diện cho 3 nguồn: đối soát khuôn mặt, đối soát dữ liệu truy nã, lưu trữ xuống delta lake// Partition Key là Key = so_cccd// việc theo dõi lịch sử di chuyển theo đúng thứ tự thời gian sẽ giúp xác định thời điểm xuất hiện gần nhất của tội phạm, đối soát khuôn mặt sau 50ms sẽ chuyển dữ liệu cảnh báo về để xác định người này đang xuất hiện tại địa điểm nào vào thời điểm nào, sau đó xuất cảnh báo khi có nghi vấn, 
2. Nếu 1 Partition có thể xử lý tối đa 10.000 events/sec, bạn cần tối thiểu bao nhiêu Partition cho Topic này để gánh mức tải cao điểm 200.000 events/sec? tối thiểu 20+2(dự phòng)
3. Ba hệ thống hạ nguồn (AI khuôn mặt, Cảnh báo tội phạm, Delta Lake) sẽ chia `Consumer Group` như thế nào: Dùng chung 1 Consumer Group hay mỗi hệ thống 1 Consumer Group riêng? Tại sao?trong consumer group sẽ có các consumer tự phân chia đọc các partition, đảm bảo đọc đồng thời, khi consumer trong group crash thì các consumer khác sẽ chịu tải thực thi thay, đảm bảo consumer <= partition// theo tôi nên chia thành các group riêng để dễ trong việc quản lý, đọc đồng thời// xử lý các nghiệp vụ, task vụ riêng

---

## 📝 Ghi Chú Cá Nhân

```
[Học viên điền vào đây]
```
