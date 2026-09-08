# 🧭 DASHBOARD — TRỤC XƯƠNG SỐNG
> **Quy tắc vàng:** Đây là file DUY NHẤT cần đọc khi bắt đầu phiên mới.
> AI Mentor BẮT BUỘC đọc file này TRƯỚC TIÊN và KHÔNG làm gì khác trước khi đọc xong.
> Cuối mỗi ngày học → Cập nhật section `📍 VỊ TRÍ HIỆN TẠI` và `📋 NHẬT KÝ`.

---

## 📍 VỊ TRÍ HIỆN TẠI
```
MODULE:     2 — Distributed Systems & Big Data
TASK:       🔄 Task 2.3: Apache Spark Internals — RDD, Lazy Evaluation & DAG
GIAI ĐOẠN:  Đang học cơ chế Resilient của RDD và triết lý Lazy Evaluation.
TRẠNG THÁI: Học viên đã nắm bản chất In-Memory Computing của Spark vs MapReduce. Đang đào sâu cơ chế chịu lỗi của RDD và phân biệt Transformation vs Action.

FILE ĐANG THỰC HIỆN:
  02_DISTRIBUTED_SYSTEMS/RESEARCH_03_SPARK_INTERNALS.md

CÂU HỎI ĐANG CHỜ TRẢ LỜI (PENDING) - BẮT ĐẦU PHIÊN SAU TỪ ĐÂY:
  "1. RAM mất điện là mất dữ liệu, vậy chữ 'Resilient' (kiên cường) của RDD hoạt động thế nào để tự hồi phục dữ liệu khi 1 máy bị sập?
   2. Tại sao khi bạn gọi liên tục 10 lệnh Transformation (map, filter), Spark lại 'lười biếng' không chạy ngay mà chờ đến khi gặp Action (count, show) mới thực thi?"
```

---

## 🔁 LỊCH ÔN TẬP NGẮT QUÃNG
| Khái niệm | Nguồn | Lần ôn cuối | Ôn tiếp theo | Streak | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Idempotency & ETL fail-safe | [RESEARCH_07](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_07_ETL_FOUNDATION.md) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| Read Replica & CDC (OLTP→OLAP sync) | [MODULE_01_SUMMARY](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/01_DATA_WAREHOUSING_SQL/MODULE_01_SUMMARY.md#L53) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| Compute vs Storage (Spark vs SQL) | [RESEARCH_07](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_07_ETL_FOUNDATION.md) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| SSH Tunneling (-L vs -R) | [RESEARCH_05](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_05_NETWORKING.md) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| Cú pháp cron | [PROGRESS.md](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/PROGRESS.md#L25) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| HAVING vs WHERE & Execution Order | [MODULE_01_SUMMARY](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/01_DATA_WAREHOUSING_SQL/MODULE_01_SUMMARY.md#L30) | 2026-08-11 | 2026-08-18 | 1 | 🟡 Ôn lại sau 7 ngày |
| Window Functions (Ranking, Lag/Lead) | [RESEARCH_02_WINDOW_FUNCTIONS.md](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/01_DATA_WAREHOUSING_SQL/RESEARCH_02_WINDOW_FUNCTIONS.md) | 2026-08-11 | 2026-08-18 | 3 | 🟡 Ôn lại sau 7 ngày |
| WAL Log & Transaction Isolation | [RESEARCH_07](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_07_ETL_FOUNDATION.md) | 2026-08-11 | 2026-08-25 | 1 | 🟢 Mới học — ôn sau 14 ngày |

---

## 🗺️ CÂY LỘ TRÌNH (TOÀN BỘ HÀNH TRÌNH)

```
DATA ENGINEERING MASTERY — Trung tâm Dữ liệu Quốc gia
│
├── ✅ MODULE 0: The Hardcore Foundation
│   ├── ✅ Task 1: Linux & CLI / Storage Layout
│   ├── ✅ Task 2: Permissions & PoLP
│   ├── ✅ Task 3: Disk & LVM
│   ├── ✅ Task 4: Automation Cleanup Pipeline (Bash, 4 lớp bảo vệ)
│   ├── ✅ Task 5: Networking & SSH Tunneling (rsync, MITM)
│   ├── ✅ Task 6: Cron & Background Processes
│   ├── ✅ Task 7: ETL Foundation (Python pipeline, Idempotency)
│   └── ✅ Task 8: DSA & Disk I/O (Generator/yield, Buffering, Parquet)
│
├── ✅ MODULE 1: Data Warehousing & SQL Mastery  (HOÀN THÀNH)
│   ├── ✅ Task 1: DW Fundamentals (OLTP/OLAP, Star Schema, SQL cơ bản)
│   ├── ✅ Task 2: Window Functions (Ranking, Lag/Lead, Windows)
│   ├── ✅ Task 3: Data Modeling (Snowflake, SCD Type 1/2/3, Surrogate Key)
│   └── ✅ Task 4: Query Optimization (Index, EXPLAIN, Partition)
│
├── 🔄 MODULE 2: Distributed Systems & Big Data  ← ĐANG Ở ĐÂY
│   ├── ✅ Task 2.0: Medallion Architecture & Cloud Storage
│   ├── 🔄 Task 2.1: Hadoop Ecosystem (HDFS, YARN)  ← TIẾP THEO
│   ├── 🔒 Apache Spark Internals (DAG, Shuffling)
│   └── 🔒 Storage Layer (Delta Lake, Iceberg)
│
├── 🔒 MODULE 3: Real-time Streaming
│   ├── 🔒 Apache Kafka (Pub/Sub, Partitioning)
│   └── 🔒 CDC (Change Data Capture)
│
├── 🔒 MODULE 4: Orchestration & Data Quality
│   ├── 🔒 Apache Airflow (DAG, Retry, Backfill)
│   ├── 🔒 Great Expectations (Data Quality Gate)
│   └── 🔒 Task 4.6: dbt - Transform bằng SQL thuần (MỚI)
│
└── 🔒 MODULE 5: Security & Data Governance (Xuyên suốt)
    ├── 🔒 Encryption (At-rest & In-transit)
    ├── 🔒 Data Privacy (Anonymization, Masking)
    └── 🔒 Access Control (RBAC, ABAC)
```

---

## ⚙️ QUY TRÌNH MỖI PHIÊN (AI Mentor làm theo đúng thứ tự này)

### Khi bắt đầu phiên mới:
1. Đọc `VỊ TRÍ HIỆN TẠI` ở trên
2. Nếu **chưa có bài nộp** → Đọc lại `CÂU HỎI ĐANG CHỜ`. Dừng lại.
3. Nếu **có bài nộp mới** → Chạy: **Acknowledge → Attack → Direct → Wait**
4. Kết thúc bằng đúng **một câu hỏi** → Ghi vào `PENDING`

### 🧠 Framework 5 Tầng Hiểu Sâu (BẮTBUỘC áp dụng khi dạy BẤT KỂ khái niệm nào):
```
Tầng 1 — WHAT     : Nó là gì? (Định nghĩa 1 câu + ví dụ thực tế)
Tầng 2 — HOW      : Dùng nó thế nào? (Cú pháp / cơ chế / code)
Tầng 3 — WHY      : Tại sao cần nó? (Vấn đề giải quyết, so sánh không có nó)
Tầng 4 — FAILURE  : Nó fail như thế nào? (Điều kiện sụp đổ, ví dụ thất bại thực tế)
Tầng 5 — TRADE-OFF : Khi nào KHÔNG dùng? (Chi phí ẩn, giải pháp thay thế)
```
> Chi tiết → xem `STUDY_SCHEDULE.md` phần **FRAMEWORK 5 TẦNG HIỂU SÂU**
> Câu hỏi kiểm tra PHẢI cover ít nhất Tầng 3 (WHY) và Tầng 4 (FAILURE)

### Cuối mỗi ngày học (học viên tự cập nhật hoặc yêu cầu Mentor cập nhật):
- Cập nhật `TRẠNG THÁI` trong `VỊ TRÍ HIỆN TẠI`
- Cập nhật `CÂU HỎI ĐANG CHỜ`
- Thêm một dòng vào `NHẬT KÝ` bên dưới

---

## 📋 NHẬT KÝ (CẬP NHẬT CUỐI NGÀY)

| Ngày | Module/Task | Việc đã làm | Trạng thái |
|------|-------------|-------------|------------|
| 2026-03-14 | M0/T1 | Storage Layout, Data Life Cycle | ✅ Hoàn thành |
| 2026-03-15 | M0/T2 | Permissions, PoLP (chmod 711/700) | ✅ Hoàn thành |
| 2026-03-15 | M0/T3 | Disk, LVM, Zero Downtime Expansion | ✅ Hoàn thành |
| 2026-03-21 | M0/T4 | Bash cleanup script, 4-layer protection | ✅ Hoàn thành |
| 2026-04-01 | M0/T5 | SSH Tunneling, rsync, MITM, Lab 63 tỉnh | ✅ Hoàn thành |
| 2026-04-05 | M0/T6 | Cron, PATH env, nohup, background process | ✅ Hoàn thành |
| 2026-04-07 | M0/T7 | Python ETL pipeline, Idempotency | ✅ Hoàn thành |
| 2026-?? | M0/T8 | Generator/yield, Buffering, Parquet vs CSV | ✅ Hoàn thành |
| 2026-06-30 | M1/T1 | Ôn tập OLTP/OLAP, Star Schema, Execution Order | ✅ Hoàn thành |
| 2026-07-02 | M1/T2 | Hoàn thành thực hành Lab 3 Challenges Window Functions | ✅ Hoàn thành |
| 2026-07-02 | M1/T3 | Giao bài nghiên cứu Snowflake/Star Schema & SCD | ⏳ Đang nghiên cứu |
| 2026-08-11 | ÔN TẬP | Phiên ôn tập kích hoạt lại 6 khái niệm bị quên (83 ngày gap) | ✅ Hoàn thành |
| 2026-08-11 | ÔN TẬP | Sửa 3 câu trả lời sai trong RESEARCH_07 & MODULE_01_SUMMARY | ✅ Hoàn thành |
| 2026-08-11 | MỚI | Học thêm: WAL Log tuần tự, ROLLBACK pending | ✅ Đã giải đáp qua Audit |
| 2026-08-11 | AUDIT | Kích hoạt Chế độ Hiệu trưởng. Học viên phân biệt được WAL (Write-optimized) vs SCD (Read-optimized) | ✅ PASS |
| 2026-08-12 | M1/T3-A | Sửa lỗi tư duy Fact/Dimension. Đang học lý thuyết SCD Type 1, 2 | ⏳ Đang làm |
| 2026-08-16 | M1/T3-A | Vượt qua bài kiểm tra thảm họa kiểm toán SCD Type 1. Hoàn thành Task 1.3-A | ✅ Hoàn thành |
| 2026-08-19 | M1/T3-B | Bắt đầu Task 1.3-B. Phân tích kiến trúc Medallion (OLTP -> CDC -> OLAP). Chờ làm bài tập Star Schema | ⏳ Đang làm |
| 2026-08-20 | M1/T3-B | Thiết kế bảng Fact. Vượt qua câu hỏi JOIN Star vs Snowflake (4 vs 6 joins). Hoàn thành Task 1.3-B | ✅ Hoàn thành |
| 2026-08-21 | M1/T3-C | Viết SQL tạo SCD Type 2. Vượt qua bài kiểm tra Surrogate Key bảo vệ tính đúng đắn của lịch sử. Hoàn thành Task 3 | ✅ Hoàn thành |
| 2026-08-23 | M1/T4-A | Giải thích B-Tree Index, EXPLAIN QUERY PLAN. Phân tích O(log n) vs O(n). Hoàn thành Task 1.4-A | ✅ Hoàn thành |
| 2026-08-24 | M1/T4-B | Học Range/List Partition và Partition Pruning. Khai báo SQL PostgreSQL. Trả lời đúng cơ chế cắt giảm I/O. Hoàn thành Task 1.4-B | ✅ Hoàn thành |
| 2026-08-25 | M1/T4-C | EXPLAIN vs EXPLAIN ANALYZE. BEGIN/ROLLBACK để X-quang DELETE an toàn. Đọc output Seq Scan, phát hiện ảo tưởng Statistics, kê đơn ANALYZE + INDEX. Hoàn thành Task 1.4-C & toàn bộ Module 1 | ✅ Hoàn thành |
| 2026-09-02 | M2/T2.0 | Medallion Architecture: Bronze/Silver/Gold. Parquet open format. Storage-compute separation. Thiết kế 3 layer cho Bộ Nội Vụ 63 tỉnh. Validation rules Silver layer. | ✅ Hoàn thành |
| 2026-09-07 | M2/T2.1 | HDFS: NameNode/DataNode, Block size, Replication Factor. Tính toán dung lượng cho 800GB dân số. Phân tích Small Files Problem & cạn kiệt RAM NameNode. Hoàn thành Task 2.1 | ✅ Hoàn thành |
| 2026-09-08 | M2/T2.2 | YARN: RM, NM, AM, Container. Phân bổ tài nguyên 5 node, so sánh FIFO vs Fair Scheduler, luồng thu hồi Container. Hoàn thành Task 2.2 | ✅ Hoàn thành |
---

## 📂 SƠ ĐỒ FILE (Tìm tài liệu nhanh)

```
data-Engineer-mastery/
├── DASHBOARD.md                        ← FILE NÀY (Đọc đầu tiên)
├── HABIT_TRACKER.md                    ← BẢNG KỶ LUẬT THÉP & CHECK-IN HÀNG NGÀY
├── .MENTOR_CONTEXT.md                  ← Luật & vai trò của Mentor
├── MASTERY_PLAN.md                     ← Lộ trình tổng thể & cam kết
├── GLOSSARY_AND_CONCEPTS.md           ← Từ điển thuật ngữ
├── PROGRESS.md                         ← Nhật ký chi tiết từng Task
│
├── 00_HARDCORE_FOUNDATION/
│   ├── MODULE_00_SUMMARY.md            ← Mục lục Module 0
│   ├── RESEARCH_05_NETWORKING.md
│   ├── RESEARCH_07_ETL_FOUNDATION.md
│   ├── RESEARCH_08_DSA_BIGDATA.md
│   └── scripts_and_data/               ← Code & dữ liệu thực hành
│
├── 01_DATA_WAREHOUSING_SQL/
│   ├── MODULE_01_SUMMARY.md            ← Mục lục Module 1
│   └── RESEARCH_02_WINDOW_FUNCTIONS.md ← (Chưa tồn tại - cần tạo)
│
└── Data-Engineer-Books-main/           ← Sách tham khảo
```
