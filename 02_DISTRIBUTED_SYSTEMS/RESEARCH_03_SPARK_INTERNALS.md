# ⚡ RESEARCH 03 — APACHE SPARK INTERNALS: TRÁI TIM CỦA BIG DATA

> **Task:** 2.3 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-09
> **Trạng thái:** ✅ Đã hoàn thành — 2026-09-18

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Hoàn thành bài này, bạn phải đạt được các năng lực cốt lõi:
1. **Bản chất RDD & In-Memory:** Giải thích được vì sao Spark nhanh hơn MapReduce gấp 10–100 lần; phân tích được cơ chế **Resilient** (Lineage Graph tự tái tạo dữ liệu khi node sập mà không cần lưu đĩa liên tục).
2. **Cơ chế Lazy Evaluation & DAG:** Phân biệt rạch ròi **Transformation** (lười biếng, chỉ ghi nhận kế hoạch) vs **Action** (kích hoạt tính toán); hiểu cách Spark biên dịch code thành DAG, phân thành các **Stages** và **Tasks**.
3. **Nút thắt Shuffling:** Phân biệt được **Narrow Dependency** (xử lý cục bộ tại worker) vs **Wide Dependency** (kích hoạt **Shuffling** - dữ liệu chia lại qua mạng và đĩa).
4. **Xử lý sự cố (Failure Modes):** Nhận diện và biết cách debug 2 lỗi kinh điển trong hệ thống phân tán: **OOM** (Out of Memory trên Driver/Executor) và **Data Skew** (lệch dữ liệu giữa các partition).
5. **Năng lực ứng dụng:** Phân tích một pipeline Spark thực tế (hàng trăm GB/TB), chỉ ra điểm kích hoạt cluster, thao tác gây tắc nghẽn mạng và đề xuất phương án tối ưu.

---

## 🔗 Kết nối kiến thức cũ

```
Task 2.1 (HDFS): Nơi lưu trữ dữ liệu phân tán (Storage)
Task 2.2 (YARN): Nơi cấp phát tài nguyên CPU/RAM (Resource Management)
Task 2.3 (SPARK): CỖ MÁY TÍNH TOÁN (Compute Engine) chạy trên YARN và đọc dữ liệu từ HDFS/S3

Module 0 Task 8: Python Generator / yield (Lazy Evaluation O(1) RAM)
                → Apache Spark xây dựng toàn bộ triết lý cốt lõi trên Lazy Evaluation!
```

---

## 🧠 Framework 5 Tầng — Apache Spark

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu, không copy)*

```
Apache Spark là framework xử lý và tính toán dữ liệu phân tán (Unified Analytics Engine), tận dụng bộ nhớ RAM (In-Memory Computing) để xử lý dữ liệu trung gian thay vì liên tục đọc/ghi xuống ổ đĩa vật lý như MapReduce, giúp tăng tốc độ xử lý từ 10 đến 100 lần.
```

### Tầng 2 — HOW (Kiến trúc & Cơ chế vận hành)

#### 1. RDD (Resilient Distributed Dataset) là gì?
```
RDD là cấu trúc dữ liệu nền tảng của Spark, hội tụ 3 đặc tính cốt tử:
1. Resilient (Tự phục hồi): Khi một partition dữ liệu trên một node bị mất, Spark không cần chạy lại từ đầu toàn bộ job mà dùng "Lineage Graph" (cây phả hệ tính toán truy xuất ngược) để chỉ tính toán và tái tạo lại đúng partition bị mất đó.
2. Distributed (Phân tán): Dữ liệu được chia thành nhiều Partition nằm rải rác trên RAM của nhiều Worker/Executor trong cụm máy để tính toán song song.
3. Immutable (Bất biến): Một khi RDD được tạo ra thì không thể bị sửa đổi (read-only). Mọi phép biến đổi đều tạo ra một RDD mới, giúp đảm bảo tính nhất quán tuyệt đối cho Lineage Graph khi phục hồi lỗi.

Ví dụ Lineage:
RDD_0 (đọc file) -> RDD_1 (filter) -> RDD_2 (map) -> RDD_3 (groupBy)
Nếu RDD_3 bị mất 1 partition, Spark lần ngược Lineage: RDD_2 -> RDD_3 để tính lại partition đó.
```

#### 2. Transformations vs Actions & Lazy Evaluation
```
- Transformation (map, filter, select, groupBy): Là các phép toán biến đổi dữ liệu. Mang tính "Lười biếng" (Lazy) — Spark không thực thi ngay mà chỉ ghi nhận vào Kế hoạch thực thi logic (Logical Plan/Lineage).
- Action (show, count, collect, save, write): Là các hành động kích hoạt Spark thực sự khởi động cluster để tính toán và trả về kết quả cho Driver hoặc ghi xuống Storage.
- Bản chất tối ưu của Lazy Evaluation:
  Thay vì chạy từng dòng lệnh một cách máy móc, tính lười biếng cho phép bộ tối ưu hóa (Catalyst Optimizer) nhìn thấy "toàn bộ bức tranh" của chuỗi xử lý. Từ đó, Spark có thể:
  + Predicate Pushdown: Đẩy bộ lọc (filter) xuống tầng đọc dữ liệu sớm nhất có thể để chỉ tải dữ liệu cần thiết.
  + Operator Pipelining: Gộp nhiều phép biến đổi hẹp (map, filter) thành 1 lượt duyệt dữ liệu duy nhất trong RAM.
```

#### 3. Narrow Dependency vs Wide Dependency (Shuffling)
```
- Narrow Dependency (map, filter, union):
  Mỗi partition của RDD cha chỉ được sử dụng bởi tối đa một partition của RDD con (quan hệ 1-1). Dữ liệu được xử lý cục bộ ngay trên RAM của worker đó, KHÔNG phải nhảy qua mạng, KHÔNG có Shuffling. Tốc độ cực nhanh.
- Wide Dependency (groupBy, join, distinct, repartition):
  Một partition của RDD cha được sử dụng bởi nhiều partition của RDD con (quan hệ 1-n hoặc n-n). Để gom nhóm dữ liệu cùng key, Spark bắt buộc phải thực hiện SHUFFLE: chia lại dữ liệu, ghi tạm xuống đĩa và bắn qua mạng giữa các máy trong cụm.
  => Shuffling là "kẻ thù số 1" của hiệu năng trong hệ thống phân tán vì tốn Disk I/O, Network I/O và dễ gây OOM.
```

#### 4. DAG (Directed Acyclic Graph) & Execution Plan
```
- Ai vẽ ra DAG?
  Chính là DAGScheduler (chạy trên máy Driver). Khi gặp một Action, DAGScheduler dịch chuỗi Transformation thành một đồ thị có hướng không chu trình (DAG).
- Phân chia Stage và Task:
  + Cắt Stage: Cứ mỗi khi gặp một ranh giới Wide Dependency (Shuffle boundary), DAGScheduler sẽ cắt thành một Stage mới. Do đó, một Job gồm nhiều Stages nối tiếp nhau qua các bước Shuffle.
  + Tạo Task: Trong mỗi Stage, Spark chia thành nhiều Task chạy hoàn toàn song song. Số lượng Task trong một Stage bằng đúng số lượng Partition của dữ liệu tại Stage đó.
```

### Tầng 3 — WHY
> *(MapReduce vs Apache Spark: Tại sao Spark nhanh hơn MapReduce gấp 10-100 lần?)*

```
1. In-Memory Computing: Spark giữ dữ liệu trung gian trên RAM giữa các bước tính toán, trong khi MapReduce bắt buộc phải ghi dữ liệu trung gian xuống đĩa cứng HDFS sau mỗi pha Map và nạp lại ở pha Reduce.
2. DAG Execution Engine: Spark xây dựng đồ thị thực thi hoàn chỉnh và tối ưu hóa trước khi chạy (pipelining nhiều phép toán vào 1 task), loại bỏ việc đồng bộ hóa đĩa không cần thiết.
3. Thread-based Execution: Spark chạy các task dưới dạng multi-threading trong cùng 1 tiến trình Executor JVM (khởi động micro-giây), trong khi MapReduce phải fork process JVM mới cho từng task (tốn tài nguyên và độ trễ lớn).
```

### Tầng 4 — FAILURE
> *(Trong Spark, nguyên nhân phổ biến nhất gây sập OOM (Out Of Memory) của Executor là gì? Data Skew là gì?)*

```
1. OOM (Out of Memory) Executor:
   - Nguyên nhân chính: Kích thước của 1 Partition dữ liệu quá lớn vượt quá dung lượng Heap RAM của Executor.
   - Thường xảy ra khi Shuffle: Các key gom về 1 partition quá nhiều, hoặc buffer bộ nhớ shuffle bị tràn khi spill xuống đĩa không kịp.
   - OOM Driver: Thường do lập trình viên gọi lệnh `.collect()` kéo toàn bộ dataset hàng trăm triệu bản ghi từ worker về máy Driver.

2. Data Skew (Lệch dữ liệu):
   - Là hiện tượng dữ liệu phân bổ không đồng đều giữa các partition sau khi Shuffle (ví dụ: key "TP.HCM" có 15 triệu dòng, còn 62 tỉnh khác mỗi tỉnh chỉ có vài trăm nghìn dòng).
   - Hậu quả: 62 task xử lý các tỉnh nhỏ hoàn thành chỉ trong vài giây, nhưng riêng 1 task ôm trọn partition TP.HCM chạy lê thê hàng chục phút (hiện tượng Straggler Task), làm toàn bộ pipeline bị nghẽn và có nguy cơ cao làm sập OOM Executor đó.
```

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG nên dùng Spark?)*

```
1. Dữ liệu quy mô nhỏ (< vài chục GB): Không nên dùng Spark vì chi phí overhead (khởi tạo cluster, kết nối mạng giữa driver-executor, serialization dữ liệu) lớn hơn nhiều thời gian tính toán. Dùng DuckDB, Polars, Pandas hoặc PostgreSQL trên máy đơn sẽ nhanh và tiết kiệm hơn gấp nhiều lần.
2. Ứng dụng OLTP / Truy vấn độ trễ cực thấp (Sub-millisecond): Spark thiết kế cho Batch processing & Big Data Analytics (OLAP). Không phù hợp làm cơ sở dữ liệu giao dịch real-time phục vụ người dùng cuối.
3. Tài nguyên phần cứng hạn hẹp: Cụm máy không đủ RAM sẽ khiến Spark liên tục spill dữ liệu xuống đĩa, làm mất đi ưu thế in-memory và chạy thậm chí chậm hơn các công cụ tối ưu đĩa.
```

---

## 🛠️ BÀI TẬP — Thiết Kế Pipeline Spark Dân Số 63 Tỉnh

**Tình huống:**
- Bạn có 1 file Parquet 800GB lưu dữ liệu CCCD của 100 triệu dân trên HDFS.
- Yêu cầu: Đếm số lượng người theo từng Tỉnh/Thành và tìm Top 5 tỉnh đông dân nhất.

**Câu hỏi & Lời giải chuẩn Senior:**

### 1. Đoạn pipeline: `df.filter(age > 18).groupBy("province").count().show(5)`:
- **Phân loại Transformation vs Action:**
  + `filter(age > 18)`: **Transformation** (Narrow Dependency — lọc cục bộ trên từng partition).
  + `groupBy("province").count()`: **Transformation** (Wide Dependency — gom nhóm và đếm trả về DataFrame mới gồm cột `province` và `count`, chưa phải là Action!).
  + `show(5)`: **Action** (Hành động yêu cầu lấy 5 dòng kết quả in ra console).
- **Điểm kích hoạt:**
  + Spark **chỉ thực sự kích hoạt cluster** để đọc file 800GB và tính toán khi gặp lệnh **`show(5)`**. Các dòng trước đó chỉ được ghi nhận vào kế hoạch thực thi (Logical Plan).

### 2. Trong chuỗi lệnh trên, bước nào gây ra Shuffling (Wide Dependency) qua mạng giữa các máy?
- Bước **`groupBy("province")`** (đi kèm hàm tổng hợp `count`) là bước gây ra **Shuffling**.
- **Giải thích:** Ban đầu 100 triệu dân nằm rải rác ngẫu nhiên trên hàng ngàn block HDFS của 10 máy DataNode. Để gom nhóm và đếm chính xác số dân của từng tỉnh, Spark bắt buộc phải băm (Hash Partition theo cột `province`) và chuyển các bản ghi có cùng tên tỉnh về chung một Executor qua mạng nội bộ. Đây là ranh giới phân tách giữa Stage 1 (Đọc + Lọc) và Stage 2 (Gom nhóm + Đếm).

### 3. Nếu tỉnh TP.HCM có 15 triệu dân còn tỉnh Bắc Kạn chỉ có 300.000 dân, điều gì sẽ xảy ra với Executor nhận partition của TP.HCM? Khái niệm này gọi là gì?
- **Khái niệm:** Hiện tượng **Data Skew (Lệch dữ liệu)**.
- **Hậu quả:** 
  + Executor nhận partition Bắc Kạn xử lý 300.000 dòng mất 1 giây.
  + Executor nhận partition TP.HCM phải gánh 15 triệu dòng $\rightarrow$ Task chạy cực lâu (**Straggler Task**), chiếm dụng CPU/RAM, làm toàn bộ Stage bị nghẽn chờ đợi dù các máy khác đã nhàn rỗi. Nếu RAM của Executor đó không đủ chứa buffer dữ liệu của TP.HCM, nó sẽ bị tràn bộ nhớ và chết vì **OOM (Out Of Memory)**.
- **Giải pháp thực tế:** Kỹ thuật **Salting** (thêm tiền tố ngẫu nhiên từ 1 đến N vào key "TP.HCM" để chẻ nhỏ 15 triệu dòng ra N partition con, tính tổng từng phần rồi mới gom lại lần cuối).

---

## 📝 Ghi Chú Cá Nhân & Đúc Kết

```
- Spark = In-Memory + Lazy Evaluation + DAG Execution Engine.
- RDD mang 3 tính chất cốt tử: Resilient (Lineage), Distributed (Partitions), Immutable (Bất biến).
- Transformation chỉ vẽ kế hoạch; Action mới thực sự bấm nút chạy cluster.
- Narrow = Cục bộ trong node (nhanh); Wide = Shuffle qua mạng (nút thắt cổ chai, tốn kém).
- DAGScheduler (Driver) chia DAG thành các Stage tại điểm Shuffle; mỗi Stage chia thành nhiều Task theo số Partition.
- Luôn cảnh giác với Data Skew (Straggler task) và OOM (tránh dùng df.collect() trên dữ liệu lớn).
```

