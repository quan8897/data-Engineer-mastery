# 🧭 DASHBOARD — TRỤC XƯƠNG SỐNG
> **Quy tắc vàng:** Đây là file DUY NHẤT cần đọc khi bắt đầu phiên mới.
> AI Mentor BẮT BUỘC đọc file này TRƯỚC TIÊN và KHÔNG làm gì khác trước khi đọc xong.
> Cuối mỗi ngày học → Cập nhật section `📍 VỊ TRÍ HIỆN TẠI` và `📋 NHẬT KÝ`.

---

## 📍 VỊ TRÍ HIỆN TẠI
```
MODULE:     1 — Data Warehousing & SQL Mastery
TASK:       3 — Data Modeling Nâng cao (Snowflake vs Star, SCD)
GIAI ĐOẠN:  RESEARCH (Học viên đang tự nghiên cứu)
TRẠNG THÁI: Vừa hoàn thành phiên ôn tập 3 khái niệm Module 0 (11/08/2026).
             Câu hỏi PENDING về Surrogate Key & SCD Type 2 chưa trả lời.

FILE ĐANG THỰC HIỆN:
  01_DATA_WAREHOUSING_SQL/RESEARCH_03_DATA_MODELING.md

CÂU HỎI ĐANG CHỜ TRẢ LỜI (PENDING):
  1. "Tại sao Kimball khuyên tuyệt đối không dùng số CCCD (Natural Key) làm Khóa chính
     trong bảng Dimension mà bắt buộc phải dùng Surrogate Key tự tăng?
     Surrogate Key giúp giải quyết SCD Type 2 như thế nào?"

  2. [MỚI - 11/08/2026] "Khi một giao dịch đang chạy mà bị treo hoặc thất bại giữa chừng,
     database xử lý như thế nào? ROLLBACK hoạt động ra sao với WAL Log?"
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
├── 🔄 MODULE 1: Data Warehousing & SQL Mastery  ← ĐANG Ở ĐÂY
│   ├── ✅ Task 1: DW Fundamentals (OLTP/OLAP, Star Schema, SQL cơ bản)
│   ├── ✅ Task 2: Window Functions (Ranking, Lag/Lead, Windows)
│   ├── ⏳ Task 3: Data Modeling (Snowflake, SCD Type 1/2/3) ← ĐANG LÀM
│   └── 🔒 Task 4: Query Optimization (Index, EXPLAIN, Partition)
│
├── 🔒 MODULE 2: Distributed Systems & Big Data
│   ├── 🔒 Hadoop Ecosystem (HDFS, YARN)
│   ├── 🔒 Apache Spark Internals (DAG, Shuffling)
│   └── 🔒 Storage Layer (Delta Lake, Iceberg)
│
├── 🔒 MODULE 3: Real-time Streaming
│   ├── 🔒 Apache Kafka (Pub/Sub, Partitioning)
│   └── 🔒 CDC (Change Data Capture)
│
├── 🔒 MODULE 4: Orchestration & Data Quality
│   ├── 🔒 Apache Airflow (DAG, Retry, Backfill)
│   └── 🔒 Great Expectations (Data Quality Gate)
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
| 2026-08-11 | MỚI | Học thêm: WAL Log tuần tự, ROLLBACK pending | 📌 Câu hỏi pending |

---

## 📂 SƠ ĐỒ FILE (Tìm tài liệu nhanh)

```
data-Engineer-mastery/
├── DASHBOARD.md                        ← FILE NÀY (Đọc đầu tiên)
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
