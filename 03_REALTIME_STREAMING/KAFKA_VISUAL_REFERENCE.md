# 🗺️ BẢN ĐỒ TƯ DUY — APACHE KAFKA FUNDAMENTALS
> Chuẩn hóa toàn bộ kiến thức Task 3.1 · Trực quan hóa · Ví dụ đời thường

---

## 🎯 Một câu bao trùm tất cả

> **Apache Kafka là hệ thống BĂNG CHUYỀN DỮ LIỆU phân tán — nhận sự kiện từ hàng ngàn nguồn, lưu trữ có thứ tự, và phân phối cho nhiều hệ thống tiêu thụ hoàn toàn độc lập nhau.**

---

## 🏭 Ví dụ đời thường: Trung Tâm Phân Loại Bưu Kiện Quốc Gia (GHN/FedEx)

Hãy tưởng tượng một trung tâm phân loại bưu kiện khổng lồ. Mọi thứ trong Kafka đều có tương đương ở đây.

```
                    TRUNG TÂM PHÂN LOẠI QUỐC GIA
                    ════════════════════════════

NGƯỜI GỬI HÀNG                    KAFKA CLUSTER                   ĐỘI NHẬN HÀNG
(PRODUCER)                        (BROKER CLUSTER)                 (CONSUMER)

  🏪 Shop A ──┐                 ┌─────────────────────┐        ┌── 🚚 Đội ship nội thành
              │   gửi hàng      │   TOPIC: "don_hang"  │        │
  🏪 Shop B ──┼────────────────▶│  ┌───────────────┐  │◀───────┤── 🚚 Đội ship liên tỉnh
              │                 │  │ Băng chuyền 0 │  │        │
  🏪 Shop C ──┘                 │  │ Băng chuyền 1 │  │        └── 🏢 Đội lưu kho
                                │  │ Băng chuyền 2 │  │
                                │  │ Băng chuyền 3 │  │
                                │  └───────────────┘  │
                                └─────────────────────┘

        Băng chuyền = PARTITION
        Mỗi đội nhận = CONSUMER GROUP
```
> ### 📌 ĐỊNH LUẬT VÀNG PHÂN PHỐI (Consumer Group Assignment):
> 
> * **Trong CÙNG 1 Đội (Same Group)**: 
>   * **1 Partition chỉ được giao cho DUY NHẤT 1 Consumer** xử lý tại một thời điểm (để tránh tranh chấp hàng hóa và đảm bảo tuyệt đối thứ tự xử lý theo Offset).
>   * **1 Consumer có thể gánh NHIỀU Partition** (ví dụ: đội chỉ có 2 người nhưng có 4 băng chuyền thì mỗi người ôm 2 băng chuyền).
>   * *Hệ quả*: Nếu số Consumer > số Partition, những Consumer thừa sẽ phải "ngồi chơi xơi nước" (nhàn rỗi).
> 
> * **GIỮA CÁC ĐỘI KHÁC NHAU (Different Groups - Fan-out)**:
>   * Các đội hoạt động **hoàn toàn độc lập**. Tại cùng một Băng chuyền 0, có thể có 1 nhân viên Đội Nội Thành, 1 nhân viên Đội Liên Tỉnh, và 1 nhân viên Đội Lưu Kho cùng đọc song song để làm 3 nhiệm vụ khác nhau mà không hề cướp mất dữ liệu của nhau!
---

## 🔑 Bảng đối chiếu: Kafka ↔ Bưu kiện

| Kafka | Trung tâm bưu kiện | Hệ thống CCCD |
|---|---|---|
| **Topic** | Loại hàng ("Đơn hàng", "Hàng lạnh") | `events_cccd_scan` |
| **Partition** | Băng chuyền số 0, 1, 2... | Khu vực phân loại số 7 |
| **Partition ID** | Số hiệu băng chuyền (0, 1, 2...) | Số `7` (kết quả của hàm hash) |
| **Partition Key** | Mã bưu chính → xác định băng chuyền | `so_cccd` → xác định Partition nào |
| **Offset** | Số thứ tự kiện hàng trên băng | Thứ tự sự kiện trong Partition |
| **Producer** | Shop/người gửi hàng | Cổng quét CCCD |
| **Consumer** | Nhân viên bốc dỡ cuối băng | AI đối soát / Bộ Công An / Delta Lake |
| **Consumer Group** | Đội xử lý (mỗi đội lo 1 mục đích) | Nhóm AI / Nhóm Công An / Nhóm Lưu trữ |
| **Broker** | Máy tính điều phối băng chuyền | Server chạy Kafka |
| **Replication** | Sao chụp danh sách đơn hàng vào kho dự phòng | Leader + Follower Partition |
| **ISR** | Danh sách kho dự phòng đang đồng bộ kịp | In-Sync Replicas |
| **acks=all** | Cả kho chính và kho phụ đều ký xác nhận nhận hàng | Leader + all Follower xác nhận |
| **Rebalance** | Trưởng ca phân lại băng chuyền khi nhân viên nghỉ | Group Coordinator giao Partition lại |
| **Consumer Lag** | Đống hàng tồn đọng chưa bốc dỡ | Consumer đọc không kịp Producer ghi |
| **Poison Pill** | Kiện hàng rò rỉ axit làm dừng băng chuyền | Message lỗi format làm Consumer crash |
| **DLQ** | Khu cách ly hàng lỗi xử lý sau | Dead Letter Queue — tách tin lỗi ra xử lý riêng |

---

## 🏗️ Kiến trúc tổng thể — Hệ thống CCCD Quốc Gia

```
                          200.000 events/giây
     ┌─────────────────────────────────────────────────┐
     │              PRODUCER LAYER                      │
     │  [Cổng Nội Bài] [Cổng Tân Sơn Nhất] [Ga Hà Nội]│
     │  [Bệnh viện...]  [Cơ quan hành chính...] ...    │
     └──────────────────────┬──────────────────────────┘
                            │ Key = so_cccd
                            │ hash(so_cccd) % 20
                            ▼
     ┌─────────────────────────────────────────────────┐
     │         KAFKA CLUSTER (3 Brokers)                │
     │                                                  │
     │  Topic: "events_cccd_scan"                       │
     │  ┌──────────────────────────────────────────┐   │
     │  │ P0  [off:0][off:1][off:2]...[off:50k]    │   │
     │  │ P1  [off:0][off:1][off:2]...[off:48k]    │   │
     │  │ P2  [off:0][off:1]...[off:51k]           │   │
     │  │ ...                                      │   │
     │  │ P7  [Cô A: 07:50][Cô A: 07:55][Cô A: 08:10] │  ← Cùng cccd, cùng Partition
     │  │ ...                                      │   │
     │  │ P19 [off:0][off:1]...[off:47k]           │   │
     │  └──────────────────────────────────────────┘   │
     │  Replication Factor = 3 (mỗi Partition có 3 bản)│
     └──────┬──────────────────┬──────────────┬────────┘
            │                  │              │
            │ Fan-out: 1 Topic, 3 Consumer Group độc lập
            │                  │              │
            ▼                  ▼              ▼
     ┌────────────┐   ┌──────────────┐  ┌──────────────┐
     │ GROUP: AI  │   │ GROUP: CÔNG  │  │ GROUP: LAKE  │
     │ (20 worker)│   │ AN (20 wkr)  │  │ (20 worker)  │
     │            │   │              │  │              │
     │ Đối soát   │   │ Cảnh báo tội │  │ Ghi batch    │
     │ khuôn mặt  │   │ phạm < 10ms  │  │ mỗi 5 phút  │
     │ 50ms/lần   │   │              │  │ vào Delta    │
     └────────────┘   └──────────────┘  └──────────────┘
```

---

## 🔢 Partition Key — Cơ chế Hash

```
Câu hỏi: 100 giao dịch của công dân "001099012345" bay vào đâu?

Bước 1:  Kafka chạy hàm hash:
         hash("001099012345") % 20 partitions = 7

Bước 2:  Lần 1: Vào cổng  → Partition 7, Offset 523
         Lần 2: Mua hàng  → Partition 7, Offset 524
         Lần 3: Ra cổng   → Partition 7, Offset 525

         Kết quả: CẢ 100 giao dịch → Partition 7 (cùng ngăn kéo)
                  Consumer đọc Offset 523→524→525 = đúng thứ tự thời gian ✅

Quan trọng: Partition 7 KHÔNG phải có tên là "001099012345"
            Partition 7 chứa dữ liệu của ~4,8 triệu công dân
            nhưng dữ liệu của TỪNG công dân vẫn tuần tự theo Offset
```

---

## 📜 Chi tiết giải phẫu bên trong 1 Partition (Append-Only Log & Offset)

Mỗi Partition thực chất là một chuỗi các khối dữ liệu (Record/Message) được ghi nối tiếp nhau theo thứ tự thời gian, được đánh số bằng Offset:
consumer A và B phải thuộc 2 group khác nhau
```
Partition 0 (Append-only Log):
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Offset 0 │ Offset 1 │ Offset 2 │ Offset 3 │ Offset 4 │ Offset 5 │ Offset 6 │ ... (Ghi tiếp vào đuôi)
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
     ▲                                           ▲
     │                                           │
Consumer A (Đã xử lý đến đây)              Consumer B (Đang đọc tin mới nhất)
(Current Offset = 0)                       (Current Offset = 4)
```

**3 Bí mật kiến trúc tạo nên sức mạnh của Kafka:**
1. **Append-Only Log (Bất biến - Immutable)**: 
   - Dữ liệu chỉ được ghi nối tiếp vào đuôi (`O(1)` write). Tuyệt đối **không sửa, không xóa chèn giữa chừng**.
   - Nhờ ghi tuần tự liên tục (Sequential I/O), tốc độ ghi của Kafka đạt hàng triệu tin nhắn/giây, nhanh ngang ngửa ghi trực tiếp vào RAM.
2. **Đọc KHÔNG làm mất dữ liệu (Khác biệt hoàn toàn với Message Queue truyền thống)**:
   - Trong RabbitMQ/ActiveMQ, Consumer lấy tin xong thì tin biến mất khỏi queue.
   - Trong Kafka, tin nhắn **vẫn nằm nguyên trên đĩa** sau khi đọc (chỉ bị xóa khi hết hạn lưu trữ `retention.ms`, ví dụ sau 7 ngày).
3. **Con trỏ Offset độc lập tuyệt đối**:
   - Consumer A (Ví dụ: Batch Data Lake) đọc chậm ở Offset 0 hoàn toàn không ảnh hưởng đến Consumer B (Realtime Alert) đang đọc băng băng ở Offset 4.
   - Mỗi Consumer/Group tự lưu và quản lý con trỏ vị trí của riêng mình (lưu tại Topic nội bộ `__consumer_offsets`).

---

## 👥 Consumer Group — Quy tắc vàng

```
Topic: "events_cccd_scan" — 4 Partitions (đơn giản hóa)
════════════════════════════════════════════════════════

Trường hợp 1: 2 Consumer trong group
  P0 ──▶ C1
  P1 ──▶ C1
  P2 ──▶ C2
  P3 ──▶ C2
  → C1 và C2 mỗi người đọc 2 Partition

Trường hợp 2: 4 Consumer trong group (tối ưu)
  P0 ──▶ C1
  P1 ──▶ C2
  P2 ──▶ C3
  P3 ──▶ C4
  → Mỗi Consumer đọc đúng 1 Partition (throughput tối đa)

Trường hợp 3: 6 Consumer trong group (lãng phí)
  P0 ──▶ C1
  P1 ──▶ C2
  P2 ──▶ C3
  P3 ──▶ C4
       C5 ──▶ 💤 Nhàn rỗi
       C6 ──▶ 💤 Nhàn rỗi

QUY TẮC VÀNG: Số Consumer tối ưu = Số Partition (không hơn không kém)
               Consumer > Partition = Lãng phí tài nguyên
               Consumer < Partition = Chưa tận dụng hết throughput
```

---

## ⚡ Rebalancing — Khi nhân viên vắng mặt

```
Bình thường:                    C1 crash đột ngột:

P0 ──▶ C1  ┐                   P0 ──▶ C2  ┐  ← C2 ôm thêm việc
P1 ──▶ C1  ┘                   P1 ──▶ C2  ┘
P2 ──▶ C2  ┐                   P2 ──▶ C2     ← C2 vẫn làm
P3 ──▶ C3  ┘                   P3 ──▶ C3

Cơ chế:
1. Kafka phát hiện C1 mất heartbeat (sau session.timeout.ms)
2. Group Coordinator kích hoạt Rebalancing
3. C2 và C3 dừng đọc tạm thời (Stop-the-World Rebalance)
4. Phân công lại Partition
5. C2 và C3 tiếp tục đọc từ Offset đã commit cuối cùng của C1
   → Không mất dữ liệu vì Offset đã được lưu
```

---

## 🔄 Replication & High Availability: Cơ Chế Leader - Follower

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                  KAFKA CLUSTER                                         │
│                                                                                        │
│   TOPIC: "orders" (Được chia làm 2 Partitions, Cấu hình sao lưu Replication Factor = 2)│
│   ──────────────────────────────────────────────────────────────────────────────────   │
│   • Partition 0: Gồm 1 Leader + 1 Follower                                             │
│   • Partition 1: Gồm 1 Leader + 1 Follower                                             │
│                                                                                        │
│        ┌────────────────────────┐                   ┌────────────────────────┐         │
│        │        BROKER 1        │                   │        BROKER 2        │         │
│        │                        │                   │                        │         │
│        │  ┌──────────────────┐  │    Đồng bộ dữ liệu│  ┌──────────────────┐  │         │
│        │  │   Partition 0    │  │ ═════════════════>│  │   Partition 0    │  │         │
│        │  │     (LEADER)     │  │  (Sync Replicas)  │  │    (FOLLOWER)    │  │         │
│        │  └────────▲─────────┘  │                   │  └──────────────────┘  │         │
│        │           │            │                   │                        │         │
│        │           │            │                   │  ┌──────────────────┐  │         │
│        │  ┌────────┴─────────┐  │    Đồng bộ dữ liệu│  │   Partition 1    │  │         │
│        │  │   Partition 1    │  │<═════════════════ │  │     (LEADER)     │  │         │
│        │  │    (FOLLOWER)    │  │  (Sync Replicas)  │  └────────▲─────────┘  │         │
│        │  └──────────────────┘  │                   │           │            │         │
│        └────────────────────────┘                   └───────────┼────────────┘         │
└────────────────────▲────────────────────────────────────────────┼──────────────────────┘
                     │                                            │
           (Ghi/Đọc Partition 0)                        (Ghi/Đọc Partition 1)
                     │                                            │
        ┌────────────┴─────────────┐                 ┌────────────┴────────────┐
        │   PRODUCER / CONSUMER    │                 │   PRODUCER / CONSUMER   │
        │  (Ứng dụng Gửi / Nhận)   │                 │  (Ứng dụng Gửi / Nhận)  │
        └──────────────────────────┘                 └─────────────────────────┘
```

### ⚙️ Nguyên lý hoạt động nhìn từ mô hình:

1. **Topic trải rộng trên nhiều Broker**:
   * Topic `"orders"` không nằm riêng ở Broker 1 hay Broker 2. Nó gồm 2 Partition (Partition 0 và Partition 1) được phân tán sang cả hai máy chủ.
   * *Bản chất*: Topic chỉ là định danh logic, Partition mới là đơn vị lưu trữ vật lý thực tế trên đĩa cứng.

2. **Leader nhận việc, Follower sao lưu**:
   * Khi ứng dụng (Producer/Consumer) muốn gửi hoặc nhận dữ liệu của Partition 0, nó sẽ kết nối thẳng tới **Leader trên Broker 1**.
   * Cùng lúc đó, bản **Follower trên Broker 2** âm thầm kéo dữ liệu từ Broker 1 về để lưu trữ dự phòng (duy trì trạng thái **ISR - In-Sync Replicas**).

3. **Cân bằng tải (Load Balancing)**:
   * Đối với Partition 1, quyền Leader được giao cho **Broker 2**, còn Follower nằm ở **Broker 1**.
   * Nhờ vậy, cả 2 Broker đều cùng tham gia gánh tải xử lý đọc/ghi chứ không có máy nào phải "ngồi chơi xơi nước".

4. **Khả năng chịu lỗi (Fault Tolerance)**:
   * Nếu Broker 1 bị sập, Kafka Controller sẽ phát hiện và ngay lập tức nâng bản sao **Partition 0 (FOLLOWER) trên Broker 2 thành LEADER mới**.
   * Hệ thống tiếp tục chạy bình thường mà không bị gián đoạn hay mất mát dữ liệu.

---

## 🛡️ Độ tin cậy: Ba mức acks

```
BĂNG CHUYỀN BƯU KIỆN — Ký xác nhận hàng:

acks = 0  (Gửi & Quên)
  Shop gửi hàng → Ném lên băng chuyền → Đi về, không cần biết
  Rủi ro: Băng chuyền bị đứt → Kiện hàng rơi mất → MẤT DỮ LIỆU
  Dùng khi: Log hệ thống không quan trọng, metric monitoring

acks = 1  (Kho chính xác nhận)
  Shop gửi → Kho chính ký nhận → Shop đi về
  Rủi ro: Kho chính cháy trước khi sao chép sang kho phụ
            → MẤT DỮ LIỆU
           Hoặc: Kho chính ký xong nhưng phiếu bị mất (network)
            → Shop gửi lại → TRÙNG LẶP

acks = all  (Cả kho chính VÀ kho phụ cùng ký)
  Shop gửi → Kho chính ký → Kho phụ 1 ký → Kho phụ 2 ký → Shop đi về
  Yêu cầu thêm:
    min.insync.replicas = 2  ← Ít nhất 2 kho phải ký (chặn trường hợp chỉ còn 1 kho)
    enable.idempotence = true ← Kafka tự phát hiện và loại bỏ đơn hàng trùng lặp

  Kết quả: Exactly-Once — Chính xác 1 lần, không mất, không thừa ✅
  Dùng khi: Ngân hàng, CCCD, thanh toán — BẮT BUỘC
```

---

## 💥 Tầng 4: Thảm họa thực tế & Chiến lược cứu hộ

### 1. Consumer Lag & Hệ quả khi Producer ghi nhanh gấp 10 lần Consumer

* **Consumer Lag là gì?**
  * **Định nghĩa**: Là độ trễ (khoảng cách) giữa tin nhắn mới nhất vừa được ghi vào Partition (**Log End Offset - LEO**) và tin nhắn cuối cùng mà Consumer đã đọc/commit (**Current Offset**).
  * **Công thức**:
    $$\text{Lag} = \text{Log End Offset (LEO)} - \text{Current Offset}$$
  * **Hình ảnh đời thực**: Quầy tiếp nhận đã nhận được lá đơn số 1.000, nhưng nhân viên xử lý mới chỉ đang duyệt tới lá đơn số 100 $\rightarrow$ $\text{Lag} = 900$ lá đơn đang tồn đọng trên bàn.

* **Hệ quả khi tốc độ Producer gấp 10 lần Consumer:**
  1. **Dữ liệu hiển thị trễ nghiêm trọng (Data Latency / Stale Data)**: Báo cáo, dashboard hoặc các giao dịch nghiệp vụ (gửi email, tính điểm thưởng, trừ tiền, cảnh báo thời gian thực) bị trễ hàng giờ, thậm chí hàng ngày so với thời gian thực.
  2. **Nguy cơ MẤT TRẮNG DỮ LIỆU do cơ chế dọn dẹp (Retention Policy)**: Mặc định Kafka sẽ xóa dữ liệu cũ sau một khoảng thời gian (ví dụ `retention.ms = 7 ngày`) hoặc theo dung lượng (`retention.bytes`). Nếu Consumer xử lý quá chậm và độ trễ vượt qua thời hạn lưu trữ, các message cũ chưa kịp đọc sẽ **bị xóa vĩnh viễn khỏi Broker** trước khi Consumer chạm tới!
  3. **Tràn dung lượng ổ cứng Broker (Disk Pressure)**: Nếu tăng cấu hình `retention` để chờ Consumer đọc hết, ổ cứng của các Broker sẽ phình to rất nhanh, dễ dẫn đến cạn kiệt dung lượng đĩa và làm crash toàn bộ Kafka Cluster.
  4. **Trigger Rebalance liên tục (`max.poll.interval.ms`)**: Nếu Consumer quá tải, tốn quá nhiều thời gian để xử lý 1 batch message vượt ngưỡng timeout (`max.poll.interval.ms`, mặc định 5 phút) mà không gọi lại `.poll()`, Kafka Coordinator sẽ phán quyết Consumer đó đã bị treo/chết và kích hoạt Rebalance liên tục, gây gián đoạn toàn bộ Consumer Group (hiện tượng Stop-The-World).

* **Cách khắc phục:**
  * **Tăng số lượng Partition**: Nếu Topic chỉ có 2 Partition, tối đa chỉ có 2 Consumer chạy song song. Cần tăng số Partition (ví dụ lên 10) và thêm các Consumer instance tương ứng vào cùng Consumer Group để chia tải xử lý song song. *(Lưu ý: Nên quy hoạch số Partition ngay từ khâu thiết kế để tránh làm thay đổi công thức hash key).*
  * **Tối ưu code phía Consumer**: Dùng xử lý bất đồng bộ (Async/Worker Thread Pool), chuyển từ xử lý từng bản ghi sang xử lý theo lô (batch processing), hoặc tối ưu lại câu lệnh ghi vào Database downstream.
  * **Scale hạ tầng Consumer**: Tăng CPU/RAM hoặc scale số lượng Pod/Container chạy Consumer.

---

### 2. Hiện tượng Poison Pill (Bản tin thuốc độc) & Giải pháp DLQ

* **Hiện tượng Poison Pill là gì?**
  * Là hiện tượng một bản ghi (message) bị lỗi định dạng (ví dụ: chuỗi JSON sai cú pháp, thiếu trường bắt buộc, dữ liệu gây lỗi chia cho 0, hoặc giá trị null bất thường).

* **Cơ chế gây nghẽn toàn hệ thống (Infinite Crash-Loop):**
  1. Consumer đọc trúng bản ghi lỗi này $\rightarrow$ Quá trình parse/xử lý gặp ngoại lệ (Exception) và văng lỗi (crash).
  2. Vì bị crash trước khi kịp commit Offset, nên khi Consumer khởi động lại (hoặc pod khác nhận lại Partition), nó lại đọc đúng bản ghi tại vị trí Offset đó một lần nữa.
  3. **Kết quả**: Tạo thành **vòng lặp vô tận (Infinite Crash-Loop)**. Consumer dừng hẳn tiến trình đọc các bản ghi phía sau, Partition đó bị đóng băng hoàn toàn và làm Consumer Lag tăng vọt.

* **Giải pháp: Cơ chế Dead Letter Queue (DLQ)**
  * **Triết lý cốt lõi**: *"Cách ly bệnh nhân, cứu lấy đoàn tàu"*. Thay vì để cả pipeline sập vì một bản ghi lỗi, ta bắt ngoại lệ, đưa bản tin lỗi sang một Topic riêng biệt để mổ xẻ sau, rồi cho phép Consumer tiếp tục đọc các message tiếp theo.
  * **Quy trình triển khai chuẩn công nghiệp:**
    1. **Bọc mã xử lý trong khối `try - catch`**: Khi gặp lỗi không thể khắc phục được (*Unrecoverable Error* như `DeserializationException`, `JsonParseException`), bắt lại không để ném ra crash luồng.
    2. **Cơ chế Thử lại (Retry Policy)**: Nếu là lỗi tạm thời (ví dụ timeout mạng, cơ sở dữ liệu bận), thử lại với khoảng cách thời gian tăng dần (*Exponential Backoff*, ví dụ thử lại tối đa 3 lần).
    3. **Đẩy vào DLQ Topic**: Nếu sau 3 lần vẫn lỗi hoặc xác định là lỗi sai định dạng, tự động đóng gói message đó (kèm theo thông tin: stack trace lỗi, tên lỗi, thời gian lỗi, Offset gốc) và gửi sang một Topic riêng biệt gọi là DLQ Topic (ví dụ: `orders.DLQ`).
    4. **Commit Offset và tiếp tục**: Consumer ghi nhận commit xong vị trí message lỗi đó, tiến hành đọc tiếp bản ghi bình thường tiếp theo.
    5. **Xử lý hậu kỳ (Offline Troubleshooting)**: Đội ngũ kỹ sư sẽ kiểm tra các tin nhắn trong `orders.DLQ`, tìm hiểu nguyên nhân gốc rễ (Root Cause) để sửa code hoặc fix dữ liệu rồi bắn ngược lại Topic chính để xử lý lại.

---

## ⚖️ Tầng 5: Khi nào KHÔNG dùng Kafka?

```
Kafka phù hợp khi:                    KHÔNG dùng Kafka khi:
✅ > 10.000 events/giây               ❌ Vài trăm events/giây
✅ Nhiều hệ thống cùng đọc 1 luồng   ❌ Chỉ 1 bên nhận
✅ Cần lưu lại lịch sử sự kiện       ❌ Chỉ cần "fire and forget"
✅ Real-time, độ trễ ms               ❌ Chấp nhận độ trễ phút/giờ

Thay thế phù hợp hơn:
  Hệ thống nhỏ    → RabbitMQ (đơn giản, nhẹ, rẻ)
  Chỉ cần queue   → PostgreSQL LISTEN/NOTIFY
  Serverless nhỏ  → AWS SQS / Google Pub/Sub managed
```

---

## 🏆 Tổng kết 5 Tầng — 5 câu cốt lõi

```
Tầng 1 WHAT:     Kafka là băng chuyền sự kiện phân tán —
                  nhận từ nhiều nguồn, lưu có thứ tự, phân phối cho nhiều đích.

Tầng 2 HOW:      Key → hash → cùng Partition → Offset đảm bảo thứ tự.
                  Consumer Group: mỗi Partition chỉ 1 Consumer đọc trong group.
                  acks=all + min.insync.replicas=2 + idempotence = Exactly-Once.

Tầng 3 WHY:      Decoupling (tách rời), Backpressure (đệm sốc tải),
                  Fan-out (1 nguồn, nhiều đích đọc độc lập).

Tầng 4 FAILURE:  Consumer Lag = tắc nghẽn → trễ dữ liệu.
                  Poison Pill = tin lỗi → dùng DLQ để cách ly.

Tầng 5 TRADE-OFF: Kafka quá nặng cho hệ thống nhỏ.
                   < 10k events/giây → RabbitMQ / PostgreSQL queue.
```

---

*Tài liệu này chuẩn hóa toàn bộ kiến thức Task 3.1 — Apache Kafka Fundamentals*  
*Tạo ngày: 2026-10-01 · Data Engineering Mastery · Module 3*
