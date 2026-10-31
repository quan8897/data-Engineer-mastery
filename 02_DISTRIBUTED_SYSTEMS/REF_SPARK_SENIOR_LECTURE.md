# 📚 THAM KHẢO — BÀI GIẢNG SENIOR DATA ENGINEER: APACHE SPARK INTERNALS

> **Loại file:** Tài liệu tham khảo kiến trúc chuyên sâu — Dành cho Kỹ sư trưởng (Senior / Lead Data Engineer)
> **Chủ đề:** Mổ xẻ Bộ nhớ (Memory Management), 5 Chiến lược JOIN, Catalyst Optimizer & Kỹ thuật xử lý Data Skew
> **Mục tiêu:** Cung cấp mô hình hóa (Mental Model) trực quan và hiểu bản chất sát phần cứng của Apache Spark.

---

## 🧭 MỤC LỤC BÀI HỌC

1. **Mental Model: Spark — "Dây chuyền sản xuất lắp ráp siêu tốc"**
2. **Giải phẫu Bộ nhớ Executor (Unified Memory Architecture)**
   - Phân chia 4 ngăn trong RAM JVM (Reserved, User, Storage, Execution)
   - Cơ chế "Mượn RAM linh hoạt" & Thảm họa "Spill to Disk"
3. **Mổ xẻ 5 Chiến lược JOIN trong Spark (Join Strategies)**
   - Broadcast Hash Join (BHJ) — Vũ khí tối thượng O(N) không Shuffle
   - Sort Merge Join (SMJ) — Xương sống xử lý bảng khổng lồ
   - Shuffle Hash Join, Cartesian Product & Broadcast Nested Loop
4. **Cỗ máy bí mật: Catalyst Optimizer & Project Tungsten**
   - 4 bước biên dịch truy vấn của Catalyst (Logical to Physical Plan)
   - Project Tungsten: Vượt mặt Java Garbage Collection nhờ Off-Heap
5. **Shuffling Internals: Dưới nắp ca-pô khi dữ liệu bay qua mạng**
   - Shuffle Write: Partitioning, Sorting & Tệp `.data` + `.index`
   - Shuffle Read: Kéo dữ liệu qua mạng (Network Fetch)
6. **Bài toán thực chiến: Diệt trừ Data Skew bằng kỹ thuật Salting**
7. **Bảng tra cứu cấu hình vàng của Senior Spark Engineer (Tuning Cheat Sheet)**

---

## 1. MENTAL MODEL: SPARK — DÂY CHUYỀN SẢN XUẤT SIÊU TỐC

Để hình dung Spark hoạt động thế nào trong cụm phân tán, hãy tưởng tượng một **Nhà máy chế tạo ô tô tự động hóa**:

```
[ CLIENT ] ──(Gửi bản thiết kế)──> [ DRIVER / KỸ SƯ TRƯỞNG ]
                                         │
                                         ├─ Catalyst Optimizer (Vẽ & tối ưu sơ đồ dây chuyền)
                                         ├─ DAGScheduler (Cắt thành từng công đoạn: Stage)
                                         └─ TaskScheduler (Giao việc cho thợ)
                                                 │
                   ┌─────────────────────────────┴─────────────────────────────┐
                   ▼                                                           ▼
       [ EXECUTOR 1 / XƯỞNG 1 ]                                    [ EXECUTOR 2 / XƯỞNG 2 ]
  ┌─────────────────────────────────┐                         ┌─────────────────────────────────┐
  │ Task 1 (Thợ 1)   Task 2 (Thợ 2) │                         │ Task 3 (Thợ 3)   Task 4 (Thợ 4) │
  │    (Lắp khung)      (Sơn màu)   │                         │    (Lắp khung)      (Sơn màu)   │
  │ ─────────────────────────────── │                         │ ─────────────────────────────── │
  │        BỘ NHỚ RAM CHUNG         │                         │        BỘ NHỚ RAM CHUNG         │
  └─────────────────────────────────┘                         └─────────────────────────────────┘
                   ▲                                                           ▲
                   └─────────── [ SHUFFLE: XE VẬN CHUYỂN QUA MẠNG ] ───────────┘
```

* **Driver (Kỹ sư trưởng):** Ngồi phòng điều khiển. Không trực tiếp bê vác dữ liệu, chỉ phân tích code, vẽ sơ đồ DAG, chia Stage và phân công Task.
* **Executor (Xưởng gia công):** Là các tiến trình Java (JVM) chạy trên worker node do YARN cấp phát.
* **Core / CPU (Thợ gia công):** Mỗi Core tương ứng với 1 luồng (Thread) chạy đúng 1 Task tại 1 thời điểm trên đúng 1 Partition dữ liệu.
* **Shuffle (Xe tải chuyển hàng giữa các xưởng):** Khi Xưởng 1 cần linh kiện từ Xưởng 2, xe tải phải chạy qua đường lộ (Dây mạng mạng LAN cluster) $\implies$ Điểm gây kẹt xe lớn nhất.

---

## 2. GIẢI PHẪU BỘ NHỚ EXECUTOR (UNIFIED MEMORY MANAGEMENT)

Khi bạn cấu hình `spark.executor.memory = 16GB`, thực chất 16GB này nằm trong **JVM Heap** của Executor và được Spark phân chia cực kỳ tinh vi:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TỔNG RAM EXECUTOR (VD: 16 GB)                         │
├─────────────┬───────────────────────────────────────────────────────────────┤
│  Reserved   │                   USABLE MEMORY (15.7 GB)                     │
│   Memory    ├──────────────────────────────┬────────────────────────────────┤
│  (300 MB)   │      User Memory (40%)       │       Spark Memory (60%)       │
│  Cố định    │           (~6.28 GB)         │            (~9.42 GB)          │
│  hệ thống   │  Chứa metadata, data struct, │ ┌──────────────┬─────────────┐ │
│             │  UDF, thuật toán của user    │ │   Storage    │  Execution  │ │
│             │                              │ │ Memory (50%) │ Memory (50%)│ │
│             │                              │ │ (~4.71 GB)   │ (~4.71 GB)  │ │
│             │                              │ │ Dùng cho:    │ Dùng cho:   │ │
│             │                              │ │ cache(),     │ Shuffle,    │ │
│             │                              │ │ persist()    │ Join, Sort  │ │
│             │                              │ └──────────────┴─────────────┘ │
└─────────────┴──────────────────────────────┴────────────────────────────────┘
```

### 1. Bốn ngăn bộ nhớ cốt lõi:
1. **Reserved Memory (300MB):** Spark "khóa cứng" 300MB này cho các tác vụ nội bộ của runtime Spark (tránh lỗi sập hệ thống cơ bản).
2. **User Memory (Mặc định 40% của Usable Memory):** 
   - Nơi chứa các cấu trúc dữ liệu do code của bạn tạo ra (ví dụ: các biến Python/Java, cấu trúc Hash map tự viết, mảng nội bộ trong hàm UDF).
3. **Spark Memory (Mặc định 60% của Usable Memory):** Trái tim của Spark, chia làm 2 ngăn:
   - **Storage Memory:** Chuyên dùng để lưu trữ các DataFrame/RDD khi bạn gọi `.cache()` hoặc `.persist()`, và lưu các broadcast variables.
   - **Execution Memory:** Chuyên dùng để cấp phát bộ nhớ đệm (buffer) cho các phép toán nặng: gom nhóm (**Aggregation**), sắp xếp (**Sort**), và chia lại dữ liệu (**Shuffle**).

### 2. Cơ chế "Mượn RAM linh hoạt" (Unified Memory Manager)
Từ Spark 1.6 trở đi, ranh giới giữa **Storage** và **Execution** là **ranh giới mềm (Dynamic Boundary)**:
* **Khi không ai tranh chấp:** Storage có thể mượn RAM của Execution nếu Execution đang rảnh, và ngược lại.
* **Khi có tranh chấp (Execution cần RAM để làm Shuffle/Join):**
  - Execution có quyền **đá văng (Evict)** dữ liệu đang cache trong Storage Memory ra ngoài ổ đĩa (Disk) để lấy RAM xử lý tính toán!
  - Nhưng Storage **KHÔNG BAO GIỜ** được phép đá dữ liệu của Execution đang tính toán. *(Nguyên tắc: Tính toán là ưu tiên số 1, Cache chỉ là ưu tiên số 2)*.

### 3. Thảm họa "Spill to Disk" (Tràn đĩa)
Khi một phép Sort hoặc Shuffle cần 8GB RAM nhưng Execution Memory chỉ còn 4GB:
* Spark buộc phải **Spill (tràn)** 4GB dữ liệu còn lại xuống ổ đĩa cứng cục bộ của Executor.
* **Hậu quả:** Tốc độ RAM (~20-40 GB/s) bị tụt thẳng xuống tốc độ đĩa HDD/SSD (~200MB - 1GB/s) $\implies$ Pipeline chậm đi từ **10 đến 50 lần**.
* Trên **Spark UI**, nếu bạn thấy xuất hiện dòng chữ đỏ: `Spill (Memory): 12.5 GB, Spill (Disk): 4.2 GB` $\implies$ Báo động đỏ: Executor đang thiếu RAM trầm trọng hoặc dính Data Skew!

---

## 3. MỔ XẺ 5 CHIẾN LƯỢC JOIN TRONG SPARK (JOIN STRATEGIES)

Phép JOIN hai bảng dữ liệu là nguồn gốc của 80% vấn đề hiệu năng trong Big Data. Spark có 5 thuật toán JOIN:

```
                                    BẮT ĐẦU PHÉP JOIN
                                            │
                             Có điều kiện bằng (=)? (Equi-Join)
                                    /               \
                                 CÓ                   KHÔNG
                                 /                     \
            Một trong 2 bảng nhỏ hơn                Cartesian Product Join
             ngưỡng Broadcast (10MB)?               (O(M × N) - Cực chậm!)
                     /           \
                   CÓ             KHÔNG
                   /               \
       BROADCAST HASH JOIN     Bảng có Sort được theo key?
       (Siêu tốc - O(N))           /                 \
                                CÓ                    KHÔNG
                                /                       \
                       SORT MERGE JOIN          SHUFFLE HASH JOIN
                       (Chuẩn cho bảng lớn)     (Chỉ khi bảng vừa & RAM đủ)
```

---

### Chiến lược 1: Broadcast Hash Join (BHJ) — Vũ khí tối thượng

* **Điều kiện áp dụng:** Một bảng cực lớn (Bảng A: 800GB CCCD) JOIN với một bảng nhỏ (Bảng B: 63 Tỉnh/Thành phố, ~20KB). Mặc định ngưỡng tự động là `spark.sql.autoBroadcastJoinThreshold = 10MB`.
* **Cơ chế hoạt động:**
  1. Driver đọc toàn bộ bảng nhỏ (63 Tỉnh).
  2. Driver gửi (Broadcast) một bản sao nguyên vẹn của bảng 63 Tỉnh tới **TẤT CẢ các Executor**.
  3. Tại từng Executor, mỗi Task chỉ việc đọc Partition 800GB của mình và dò tìm trong bảng nhỏ đang nằm sẵn trong RAM.

```
[ DRIVER ] ──(Broadcast Bảng Tỉnh 20KB)──┬──> [ Executor 1: 800GB Partition 1 ] ──> Map-side Join (XONG)
                                         ├──> [ Executor 2: 800GB Partition 2 ] ──> Map-side Join (XONG)
                                         └──> [ Executor 3: 800GB Partition 3 ] ──> Map-side Join (XONG)
                      ==> KHÔNG CÓ SHUFFLE QUA MẠNG! TỐC ĐỘ O(N) <==
```
* **Ưu điểm:** **Không có bất kỳ byte dữ liệu nào bị Shuffle qua mạng**. Chạy nhanh nhất có thể.
* **Cạm bẫy:** Nếu bạn ép broadcast (`broadcast(df_large)`) một bảng 5GB, Driver sẽ bị **OOM** ngay lập tức vì không đủ RAM để gom và phát tán bảng đó!

---

### Chiến lược 2: Sort Merge Join (SMJ) — Xương sống xử lý bảng khổng lồ

* **Điều kiện áp dụng:** Cả 2 bảng đều rất lớn (Bảng A: 800GB CCCD JOIN Bảng B: 500GB Lịch sử giao dịch ngân hàng theo `cccd_id`).
* **Cơ chế 3 bước:**
  1. **Shuffle:** Cả 2 bảng đều bị băm (Hash Partition) theo `cccd_id` và bắn qua mạng để đưa các dòng có cùng ID về chung 1 Executor.
  2. **Sort:** Tại từng Executor, dữ liệu của cả 2 bảng được sắp xếp tăng dần theo `cccd_id`.
  3. **Merge:** Dùng thuật toán 2 con trỏ (Two Pointers) duyệt đồng thời qua 2 danh sách đã sort để ghép cặp dữ liệu.

```
Partition Bảng A (Đã sort): [ID: 101, 102, 105, 108] ──┐
                                                      ├──> Thuật toán Two Pointers ghép cặp
Partition Bảng B (Đã sort): [ID: 101, 102, 103, 108] ──┘    (Duyệt tuần tự O(A + B), cực tiết kiệm RAM)
```

* **Tại sao SMJ an toàn chống OOM?** Vì dữ liệu đã sort, Spark không cần nạp toàn bộ dữ liệu vào một Hash Table trong RAM mà chỉ cần đọc dòng nào so sánh dòng đó (Streaming merge). Nếu thiếu RAM, Spark ghi các đoạn sort tạm xuống đĩa (External Sort) rồi merge lại sau.

---

### Bảng so sánh 5 Chiến lược JOIN:

| Chiến lược | Viết tắt | Shuffle qua mạng? | Tốc độ | Khả năng sập OOM | Khi nào dùng? |
|---|---|---|---|---|---|
| **Broadcast Hash Join** | BHJ | **KHÔNG** | ⚡ Siêu tốc | Thấp (trừ khi bảng broadcast quá to làm sập Driver) | 1 bảng nhỏ (<10MB đến vài chục MB) join bảng to |
| **Sort Merge Join** | SMJ | **CÓ** (toàn bộ) | ⚖️ Ổn định | Rất thấp (chống OOM tốt nhờ sort đĩa) | Mặc định cho 2 bảng lớn trong Spark |
| **Shuffle Hash Join** | SHJ | **CÓ** | 🚀 Nhanh hơn SMJ | Dễ sập OOM nếu 1 partition không vừa RAM | 1 bảng to join 1 bảng vừa (không đủ nhỏ để broadcast) |
| **Cartesian Join** | CPJ | **CÓ** (cực nặng) | 🐢 Rùa bò O(M×N) | Cực cao | Phép tích Descartes (không có điều kiện ON) |
| **Broadcast Nested Loop** | BNLJ| **KHÔNG** | 🐢 Chậm | Trung bình | Non-equi join (VD: `ON A.date BETWEEN B.start AND B.end`) |

---

## 4. CỖ MÁY BÍ MẬT: CATALYST OPTIMIZER & PROJECT TUNGSTEN

Tại sao code SQL trong Spark lại chạy nhanh tương đương hoặc nhanh hơn code lập trình Scala/Python viết tay? Nhờ 2 cỗ máy dưới đây:

### 1. Catalyst Optimizer — Bộ não tối ưu hóa
Khi bạn gõ code PySpark hoặc Spark SQL, Catalyst thực hiện 4 bước tự động:

```
[ CÂU LỆNH SQL / PYSPARK ]
          │
          ▼
[ 1. Unresolved Logical Plan ]   ──> Kiểm tra cú pháp (Syntax check)
          │
          ▼
[ 2. Resolved Logical Plan ]     ──> Đối chiếu Catalog: Cột này có trong bảng không? Kiểu dữ liệu đúng không?
          │
          ▼
[ 3. Optimized Logical Plan ]    ──> PHÉP THUẬT:
          │                           ├─ Predicate Pushdown (Đẩy filter xuống sát storage)
          │                           ├─ Column Pruning (Bỏ các cột thừa, chỉ đọc cột cần)
          │                           └─ Constant Folding (VD: 1 + 1 tự rút gọn thành 2)
          │
          ▼
[ 4. Physical Plans (Cost Model)]──> Ước lượng chi phí, chọn cách Join (BHJ hay SMJ?)
          │
          ▼
[ WHOLE-STAGE CODE GENERATION ]  ──> Biên dịch thành mã máy Java Bytecode thực thi trực tiếp
```

#### Ví dụ trực quan về Predicate Pushdown:
```python
# Bạn viết code:
df = spark.read.parquet("cccd_800gb.parquet")
df_hcm = df.filter(df["province"] == "TP.HCM").select("name", "age")
```
* **Không có Catalyst (Ngây thơ):** Đọc toàn bộ 800GB (100 triệu dân) lên RAM $\rightarrow$ Quét từng dòng lọc ra TP.HCM $\rightarrow$ Xóa các cột còn lại giữ lại name, age. (Sập RAM chắc chắn!).
* **Có Catalyst (Predicate Pushdown & Column Pruning):** Catalyst can thiệp vào tầng đọc Parquet. Parquet có metadata ở chân file (Footer Statistics). Spark đọc footer, thấy block nào không chứa tỉnh "TP.HCM" thì **bỏ qua luôn không đọc từ đĩa**; đồng thời **chỉ đọc 3 cột (province, name, age)** thay vì nạp cả 50 cột CCCD $\implies$ Lượng dữ liệu đọc giảm từ 800GB xuống chỉ còn **khoảng 15GB**!

---

### 2. Project Tungsten — Tối ưu hóa sát phần cứng (Hardware-Aware)
Trước Spark 1.4, Spark chạy trên Java JVM thuần túy. JVM có 2 điểm yếu chí mạng:
1. **Java Object Overhead:** Một chuỗi String 4 ký tự trong Java tốn tới **48 bytes** RAM (do các header object của Java). 1 tỷ bản ghi sẽ đốt sạch RAM vô ích.
2. **Garbage Collection (GC) Pauses:** Khi JVM giải phóng bộ nhớ của hàng triệu object con, GC sẽ dừng toàn bộ chương trình ("Stop-the-world"), làm job bị đơ từ vài giây đến vài phút.

**Giải pháp của Tungsten:**
* **Quản lý bộ nhớ Off-Heap (Unsafe Row):** Thay vì tạo các Java Object, Tungsten cấp phát bộ nhớ thô trực tiếp trên RAM hệ điều hành (giống như `malloc` trong C/C++). Dữ liệu được đóng gói thành các mảng byte nhị phân liên tục.
  $\implies$ **Không bị Java Object Overhead (tiết kiệm 70% RAM), loại bỏ hoàn toàn hiện tượng đóng băng do GC!**
* **Whole-Stage Code Generation:** Thay vì gọi các hàm lồng nhau qua lại giữa các class, Spark tổng hợp toàn bộ chuỗi map/filter thành một hàm `for` duy nhất bằng mã máy (bytecode), nạp trực tiếp vào CPU L1/L2 Cache để chạy với tốc độ hàng tỷ phép tính/giây.

---

## 5. SHUFFLING INTERNALS: DƯỚI NẮP CA-PÔ

Khi gặp Wide Dependency (như `groupByKey`, `distinct`, `join`), cơ chế Shuffle diễn ra qua 2 pha:

```
[ EXECUTOR NGUỒN (MAP SIDE) ]                         [ EXECUTOR ĐÍCH (REDUCE SIDE) ]
┌───────────────────────────────────────────┐         ┌─────────────────────────────┐
│ Task 1 tính toán xong                     │         │                             │
│ Phân chia các dòng theo Hash(Key) % N     │         │                             │
│ Sắp xếp cục bộ trong RAM buffer           │         │ Task con kéo partition      │
│ Ghi xuống đĩa thành 2 file:               │──MẠNG──>│ tương ứng của mình          │
│   1. data file (toàn bộ dữ liệu shuffle)  │ (HTTP)  │ từ TẤT CẢ các Executor khác │
│   2. index file (vị trí offset từng phần) │         │ (Shuffle Fetch / Read)      │
└───────────────────────────────────────────┘         └─────────────────────────────┘
```

### Tại sao Shuffle là "Kẻ thù số 1"?
1. **Disk Write:** Executor nguồn phải tuần tự hóa (serialize) dữ liệu và ghi xuống ổ cứng.
2. **Network I/O:** Hàng trăm Gigabyte bay qua thiết bị chuyển mạch mạng (Switch LAN). Nếu băng thông mạng bị nghẽn, toàn bộ cluster phải đứng chờ.
3. **Disk Read & Deserialization:** Executor đích đọc từ mạng về, ghi ra đĩa tạm, rồi giải mã (deserialize) ngược lại thành dữ liệu để tính tiếp.

---

## 6. BÀI TOÁN THỰC CHIẾN: XỬ LÝ DATA SKEW BẰNG SALTING

### Bối cảnh:
Bạn JOIN bảng **GiaoDich (1 tỷ dòng)** với bảng **KhachHang (10 triệu dòng)** theo cột `ma_khach_hang`.
Trong đó, tài khoản của sàn thương mại điện tử (ID = `VIP_001`) chiếm tới **100 triệu giao dịch**. Các khách hàng khác chỉ có 5-10 giao dịch.

### Thảm họa nếu để tự nhiên:
* Khi Shuffle, 100 triệu dòng của `VIP_001` dồn hết về đúng **Executor số 3**.
* Executor 1, 2, 4, 5 xử lý xong trong 10 giây và ngồi chơi xơi nước.
* Executor số 3 chạy miệt mài 45 phút, báo lỗi `java.lang.OutOfMemoryError: Java heap space` $\implies$ Toàn bộ Job bị chết.

```
Dữ liệu tự nhiên (SKEW):
Partition 0: [KH_002, KH_005, ...] (1.000 dòng)
Partition 1: [KH_003, KH_006, ...] (1.200 dòng)
Partition 2 (SẬP): [VIP_001, VIP_001, VIP_001, ... 100 TRIỆU DÒNG] ──> NGHẼN & OOM!
```

---

### Giải pháp Senior: Kỹ thuật Salting (Rắc muối)
Ý tưởng: **Chẻ nhỏ key bị lệch thành nhiều key giả ngẫu nhiên để phân tán đều ra các partition khác nhau.**

```
BƯỚC 1: Rắc muối ngẫu nhiên (1 đến 4) vào bảng lớn (GiaoDich):
  VIP_001  ──(Ghép số random 1-4)──>  VIP_001_1 (25 triệu dòng)
                                      VIP_001_2 (25 triệu dòng)
                                      VIP_001_3 (25 triệu dòng)
                                      VIP_001_4 (25 triệu dòng)

BƯỚC 2: Nhân bản (Replicate/Explode) bảng nhỏ (KhachHang) lên 4 lần tương ứng:
  VIP_001  ──(Nhân bản đủ 4 key)──>   VIP_001_1
                                      VIP_001_2
                                      VIP_001_3
                                      VIP_001_4

BƯỚC 3: Thực hiện JOIN theo key mới (salted_key):
  Bây giờ 100 triệu dòng đã được chia đều cho 4 Executor khác nhau chạy song song cùng lúc!
  Thời gian xử lý giảm từ 45 phút (hoặc sập OOM) xuống chỉ còn 2 phút!
```

---

## 7. BẢNG TRA CỨU CẤU HÌNH VÀNG CỦA SENIOR SPARK ENGINEER

| Tham số cấu hình | Giá trị mặc định | Giá trị thực chiến khuyến nghị | Ý nghĩa sống còn |
|---|---|---|---|
| `spark.sql.shuffle.partitions` | 200 | Cân đối = $2 \times$ tổng số CPU cores của cụm (hoặc chỉnh sao cho mỗi partition ~100MB - 200MB) | 200 là quá nhỏ cho dữ liệu TB (gây OOM partition), nhưng lại quá lớn cho dữ liệu vài trăm MB (gây tạo hàng ngàn task vụn). |
| `spark.sql.autoBroadcastJoinThreshold` | 10485760 (10MB) | Nâng lên 50MB - 100MB (nếu Driver có RAM lớn >16GB) | Tăng ngưỡng để Spark tự động chuyển các phép JOIN sang Broadcast Hash Join, triệt tiêu Shuffling. |
| `spark.sql.adaptive.enabled` | true (Spark 3.x) | `true` (Bắt buộc bật) | **Adaptive Query Execution (AQE)**: Spark tự động đo đạc dữ liệu runtime để tự gộp các partition nhỏ, tự đổi Join Strategy, và tự xử lý Skew Join! |
| `spark.sql.adaptive.skewJoin.enabled` | true (Spark 3.x) | `true` | Spark tự động phát hiện Data Skew và tự động chẻ nhỏ partition bị lệch mà không cần bạn phải viết code Salting bằng tay! |
| `spark.executor.memoryOverhead` | 10% executor memory | 15% - 20% (khi dùng nhiều thư viện C/Python/PyArrow) | Cấp phát bộ nhớ ngoài JVM (Off-heap) cho Container YARN. Tránh bị YARN kill tiến trình với lỗi `Container killed by YARN for exceeding memory limits`. |

---

## 💡 ĐÚC KẾT BÀN GIAO CHO KỸ SƯ

1. **Bộ nhớ:** Đừng bao giờ tin tưởng mù quáng vào `.cache()`. Chỉ cache khi DataFrame được tái sử dụng ít nhất 2 lần bởi các Action khác nhau. Sau khi dùng xong, luôn gọi `.unpersist()` để giải phóng RAM cho Execution Memory.
2. **JOIN:** Luôn tự hỏi: *"Bảng này có broadcast được không?"*. Nếu 1 trong 2 bảng nhỏ hơn 100MB, hãy dùng Broadcast Join ngay lập tức để tiết kiệm 90% thời gian chạy pipeline.
3. **Catalyst & Tungsten:** Tận dụng tối đa Spark SQL / DataFrame API thay vì viết RDD thuần với hàm Python `map()`, bởi vì code Python thuần sẽ **không bao giờ được Catalyst tối ưu hóa hay hưởng lợi từ Project Tungsten**.
