# 📅 LỊCH TRÌNH HỌC TẬP — DATA ENGINEERING MASTERY
> **Mục tiêu cuối:** Professional Data Engineer — Trung tâm Dữ liệu Quốc gia
> **Bắt đầu:** 14/03/2026 | **Nhịp:** 7 ngày/tuần | **Hoàn thành:** ~02/2027

---

## ⚡ GIAO THỨC AI MENTOR — ĐỌC TRƯỚC KHI BẮT ĐẦU PHIÊN

> File này là **hợp đồng học tập** giữa học viên và bất kỳ AI Mentor nào.
> Học viên chỉ cần báo: **"Hôm nay tôi học Task X.Y"** → AI đọc đúng task đó.

### Cấu trúc mỗi phiên học (BẮTBUỘC theo thứ tự):
```
[1] ÔN TẬP 5 PHÚT  → AI hỏi 1 câu về bài cũ. Học viên trả lời không cần tra.
[2] MỤC TIÊU       → Đọc to phần "Sau bài này tôi CÓ THỂ..."
[3] HỌC (5 TẦNG)   → Áp dụng Framework 5 Tầng Hiểu Sâu (xem bên dưới)
[4] BÀI TẬP        → Học viên làm, AI không gợi ý trước khi học viên thử
[5] KIỂM TRA       → AI hỏi câu kiểm tra cuối. Phải trả lời KHÔNG tra cứu.
[6] CẬP NHẬT       → Ghi vào DASHBOARD.md
```

### 🧠 FRAMEWORK 5 TẦNG HIỂU SÂU (Áp dụng cho MỌI khái niệm — học mới VÀ ôn tập)

> **Quy tắc:** AI Mentor PHẢI dạy theo đúng thứ tự 5 tầng này. Không được bỏ tầng nào.
> Khi ôn tập: AI bắt đầu từ tầng mà học viên đang yếu nhất.

```
┌─────────────────────────────────────────────────────────────┐
│  Tầng 1 — WHAT   : Nó là gì?                                │
│  → Định nghĩa 1 câu. Ví dụ thực tế. Không dùng thuật ngữ.  │
│                                                              │
│  Tầng 2 — HOW    : Dùng nó thế nào?                         │
│  → Cú pháp / Cơ chế hoạt động. Code minh họa.               │
│                                                              │
│  Tầng 3 — WHY    : Tại sao cần nó?                          │
│  → Vấn đề nó giải quyết. So sánh với cách làm không có nó.  │
│                                                              │
│  Tầng 4 — FAILURE: Nó fail như thế nào?                     │
│  → Điều kiện nào làm nó sụp đổ. Ví dụ thực tế về thất bại. │
│                                                              │
│  Tầng 5 — TRADE-OFF: Khi nào KHÔNG nên dùng nó?            │
│  → Chi phí ẩn. Giải pháp thay thế tốt hơn trong ngữ cảnh X. │
└─────────────────────────────────────────────────────────────┘
```

**Ví dụ áp dụng với B-Tree Index:**
```
Tầng 1 — WHAT    : Cấu trúc cây nhị phân giúp tìm kiếm dữ liệu O(log n)
Tầng 2 — HOW     : CREATE INDEX idx_cccd ON fact_chi_tra(cccd);
Tầng 3 — WHY     : Không có Index → Full Scan 1 tỷ dòng. Có Index → 30 bước
Tầng 4 — FAILURE : Cardinality thấp (cột gender 2 giá trị) → Index vô dụng
Tầng 5 — TRADE-OFF: Bảng ghi nhiều hơn đọc → Index làm chậm INSERT, nên bỏ
```

### Vai trò mở rộng của AI Mentor (Học viên có thể yêu cầu bất cứ lúc nào):
1. **🧠 Giải thích khái niệm phức tạp:** Dùng phép ẩn dụ, ví dụ thực tế hoặc chia nhỏ vấn đề (EL5 - Explain Like I'm 5).
2. **💡 Gợi ý Best Practices:** Đưa ra các phương pháp tiếp cận tốt nhất, tiêu chuẩn ngành hiện tại (VD: năm 2026 người ta làm thế nào).
3. **🛠️ Sửa lỗi tư duy:** Phát hiện lỗ hổng logic, những hiểu lầm cốt lõi và thẳng thắn chỉ ra để học viên sửa ngay.

### 🎓 Chế độ "Hiệu trưởng" (Principal Mode - Kích hoạt khi cần):
Học viên có thể yêu cầu AI đổi vai trò bằng câu: *"Hãy đóng vai Hiệu trưởng kiểm tra tôi"*.
Ở chế độ này, AI **không dạy kiến thức mới**, mà làm nhiệm vụ Audit (Kiểm duyệt hệ thống):
1. **Kiểm duyệt AI Mentor:** Đọc `DASHBOARD.md` và các file bài tập xem AI Mentor những ngày trước có làm đúng Giao thức không (VD: có dễ dãi cho qua khi chưa hiểu sâu không? có bỏ quên bước ôn tập không?).
2. **Kiểm duyệt Học viên:** Bắn 1-2 câu hỏi "chéo" ngẫu nhiên kết hợp kiến thức nhiều Task/Module để xem học viên có thực sự hiểu bản chất hay chỉ học vẹt.
3. **Phán quyết & Điều chỉnh:** Đưa ra đánh giá lạnh lùng, khách quan về thái độ/tiến độ, cảnh báo rủi ro (VD: ảo giác hiểu) và ép học viên/Mentor phải quay lại sửa nếu phát hiện hổng kiến thức.
### Nguyên tắc "Dòng chảy kiến thức" (Knowledge Flow):
- Mỗi task có **Xây dựng từ** → biết cần ôn gì trước
- Mỗi task có **Kết nối tương lai** → biết học cái này để làm gì sau
- Câu hỏi kiểm tra LUÔN yêu cầu kết hợp kiến thức CŨ + MỚI
- Câu hỏi kiểm tra PHẢI bao phủ ít nhất Tầng 3 (WHY) và Tầng 4 (FAILURE) trong Framework 5 Tầng

---

## 📋 NHẬT KÝ LỖI CỦA AI MENTOR

> Mục này ghi lại các **sai lầm trong thiết kế curriculum** do AI Mentor mắc phải.
> AI Mentor mới đọc phần này TRƯỚC để không lặp lại.

| # | Ngày | Lỗi | Tư duy sai | Đúng phải là |
|---|---|---|---|---|
| 1 | 11/08/2026 | Bỏ Module 0 khỏi lịch trình | *"Module 0 xong rồi, chỉ cần ghi những gì chưa làm"* | Lịch trình phải ghi **toàn bộ hành trình** — đã qua + đang làm + sắp làm. Module đã hoàn thành vẫn cần có mặt để: (1) AI Mentor mới hiểu nền tảng học viên, (2) học viên thấy được tiến bộ, (3) spaced repetition ôn lại đúng chỗ |

### Quy tắc rút ra từ lỗi #1:
> **Khi thiết kế hoặc cập nhật bất kỳ tài liệu học tập nào — luôn hỏi:**
> *"Người đọc file này lần đầu, không biết lịch sử — họ có đủ ngữ cảnh để hiểu không?"*
> Nếu không → bổ sung, dù nội dung đó "đã xong".

---

## 📐 TEMPLATE MỖI BÀI HỌC

```
### Task X.Y — Tên Task
> ⏱️ Ước tính: N ngày | 📁 File: tên_file.md

🔗 XÂY DỰNG TỪ: [Task cũ] — [concept cụ thể đã học]
🔗 KẾT NỐI TƯƠNG LAI: Sẽ dùng lại ở [Task sau]

🎯 MỤC TIÊU — Sau bài này tôi CÓ THỂ:
  [ ] Mục tiêu 1 (đo được bằng hành động)
  [ ] Mục tiêu 2
  [ ] Mục tiêu 3

📖 NỘI DUNG HỌC: Các khái niệm cần nắm

🔄 ÔN TẬP 5 PHÚT ĐẦU PHIÊN: Câu hỏi về bài cũ liên quan

🛠️ BÀI TẬP:
  Input: [Dữ liệu/tình huống cụ thể]
  Yêu cầu: [Làm gì]
  Output mong đợi: [Kết quả như thế nào mới đạt]
  File lưu: [tên_file.sql / .py / .md]

✅ CÂU HỎI KIỂM TRA CUỐI BÀI:
  [Câu hỏi buộc kết hợp kiến thức cũ + mới, không thể trả lời bằng học vẹt]
```

---

## 🗺️ TỔNG QUAN HÀNH TRÌNH

| Module | Tên | Tasks | Thời gian | Trạng thái |
|---|---|---|---|---|
| **1** | Data Warehousing & SQL | 4 | ~2 tuần | 🔄 Task 3 |
| **2** | Distributed Systems & Big Data | **9** *(+Task 2.0)* | ~6 tuần | 🔒 |
| **3** | Real-time Streaming | 6 | ~4 tuần | 🔒 |
| **4** | Orchestration & Data Quality | **6** *(+Task 4.6 dbt)* | ~4 tuần | 🔒 |
| **5** | Security & Governance | 4 | ~2 tuần | 🔒 |
| **6** | Cloud & Certification | 5 | ~4 tuần | 🔒 |

> [!IMPORTANT]
> **🔒 SECURITY-BY-DESIGN (Threading xuyên suốt):** Security KHÔNG phải module học một lần rồi thôi.
> Mỗi task từ Module 1 trở đi đều có câu hỏi bắt buộc: *"Nếu dữ liệu này chứa PII, cậu sẽ làm gì khác?"*
> - **Module 1:** Ai được phép query bảng nào? (RBAC cơ bản, Row-Level Security)
> - **Module 2:** File Parquet trên S3 — encrypt at-rest, IAM policy, bucket policy
> - **Module 3:** Kafka topic — authentication, TLS in-transit, access control
> - **Module 4:** Airflow DAG — secret management, không hardcode password
> - **Module 5:** Tổng hợp + audit trail, compliance, data masking PII

> [!WARNING]
> **📊 GAP — OBSERVABILITY CHƯA CÓ TRONG ROADMAP:**
> Alerting, logging tập trung, SLA tracking, data freshness monitoring — chưa được cover.
> Tạm thời bổ sung vào Task 4.1 (Airflow): học thêm DAG alerting + SLA miss callback.
> Task 4.2 (Great Expectations): thêm phần data freshness check.
> Roadmap update đầy đủ sau khi hoàn thành Module 4.

---

# ✅ MODULE 0: THE HARDCORE FOUNDATION
> **Trạng thái:** HOÀN THÀNH | **Thời gian thực tế:** 14/03/2026 → 07/04/2026 (25 ngày)
> **Tài liệu:** [`00_HARDCORE_FOUNDATION/`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/)
> **Tóm tắt:** [`MODULE_00_SUMMARY.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/MODULE_00_SUMMARY.md)

> [!NOTE]
> Module 0 đã hoàn thành. Mục này lưu lại để **AI Mentor mới** hiểu nền tảng của học viên và biết "Xây dựng từ" các Task sau đang chỉ đến điều gì.

---

| Task | Tên | Kiến thức cốt lõi | File tham khảo | Trạng thái |
|---|---|---|---|---|
| **0.1** | Linux cơ bản | Filesystem, permission, user/group, process management | [`SOLUTION_TASK_01.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/SOLUTION_TASK_01.md) | ✅ |
| **0.2** | Bash Scripting | Variables, loops, conditionals, `set -euo pipefail` | [`SOLUTION_TASK_02.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/SOLUTION_TASK_02.md) | ✅ |
| **0.3** | Storage & LVM | LVM Thin Provisioning, Disk I/O, mở rộng đĩa | [`SOLUTION_TASK_03.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/SOLUTION_TASK_03.md) | ✅ |
| **0.5** | Networking & SSH | TCP/IP, SSH Tunneling (-L vs -R), `rsync`, firewall | [`RESEARCH_05_NETWORKING.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_05_NETWORKING.md) | ✅ |
| **0.6** | Automation & Cron | Cron syntax, `at`, idempotency bằng script, PoLP | [`RESEARCH_06_AUTOMATION.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_06_AUTOMATION.md) | ✅ |
| **0.7** | ETL Foundation | Staging Table, Atomic SWAP, Read Replica, CDC, Off-peak | [`RESEARCH_07_ETL_FOUNDATION.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_07_ETL_FOUNDATION.md) | ✅ |
| **0.8A** | DSA cho Big Data | Generator/`yield`, O(1) memory, OOM Killer | [`RESEARCH_08_DSA_BIGDATA.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_08_DSA_BIGDATA.md) | ✅ |
| **0.8B** | Buffering & Parquet | Batch Write, Write Amplification, CSV vs Parquet | [`RESEARCH_08_DSA_BIGDATA.md`](file:///c:/Users/ACER/.gemini/antigravity/scratch/data-Engineer-mastery/00_HARDCORE_FOUNDATION/RESEARCH_08_DSA_BIGDATA.md) | ✅ |

### Kiến thức nền tảng từ Module 0 — các Task sau xây dựng trực tiếp trên đây:

```
Task 0.2 (set -euo pipefail)   →  Task 1.4 (EXPLAIN ANALYZE: kiểm tra query fail sớm)
Task 0.5 (SSH Tunneling)       →  Task 5.1 (Encryption in-transit: TLS là phiên bản hiện đại của SSH)
Task 0.6 (Cron + Idempotency)  →  Task 4.1 (Airflow là Cron thông minh + retry + lineage)
Task 0.7 (Staging SWAP + CDC)  →  Task 2.0 (Medallion Bronze layer) + Task 3.4 (Debezium CDC)
Task 0.8 (Generator + Parquet) →  Task 2.3 (Spark Lazy Evaluation) + Task 2.6 (Parquet columnar)

[SECURITY THREAD — hỏi ở MỌI task từ đây trở đi]
Task 1.x (SQL/DWH)             →  Ai được phép đọc bảng này? Row-Level Security?
Task 2.x (HDFS/Spark/S3)       →  File này có PII không? S3 bucket policy? Encrypt at-rest?
Task 3.x (Kafka/CDC)           →  Topic có sensitive data? TLS? Authentication?
Task 4.x (Airflow/dbt)         →  Password/key lưu ở đâu? Secret manager? Alerting khi fail?
Task 5.x (Security)            →  Audit trail, RBAC toàn hệ thống, PII masking, compliance

[OBSERVABILITY — bổ sung vào Task 4.1 + 4.2]
Task 4.1 (Airflow)             →  +DAG alerting, SLA miss callback, on_failure_callback
Task 4.2 (Great Expectations)  →  +Data freshness check, schema drift detection
```

---

# 📚 MODULE 1: DATA WAREHOUSING & SQL MASTERY

---

## Task 1.3-A — SCD: Bản chất 3 loại Slowly Changing Dimensions
> ⏱️ 1 ngày | 📁 `01_DATA_WAREHOUSING_SQL/RESEARCH_03_DATA_MODELING.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.1: Star Schema (Fact Table + Dimension Tables)
- Task 1.2: Window Functions (hiểu bảng dữ liệu có nhiều dòng theo thời gian)

🔗 **KẾT NỐI TƯƠNG LAI:** Task 1.3-B (Surrogate Key giải quyết bài toán SCD Type 2) → Task 2.6 (Delta Lake có Time Travel — giải pháp hiện đại thay SCD)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Phân biệt SCD Type 1, 2, 3 bằng 1 câu mỗi loại, không cần tra cứu
- [ ] Điền đầy đủ bảng so sánh trong `RESEARCH_03_DATA_MODELING.md` Phần 2
- [ ] Chỉ ra được: với hệ thống quốc gia cần lưu lịch sử, Type nào bắt buộc phải dùng và tại sao

📖 **NỘI DUNG HỌC:**
- SCD Type 1: Ghi đè (Overwrite) — dữ liệu cũ mất vĩnh viễn
- SCD Type 2: Thêm dòng mới + đánh dấu dòng cũ hết hiệu lực — lưu toàn bộ lịch sử
- SCD Type 3: Thêm cột "giá trị cũ" — chỉ lưu được 1 lần thay đổi

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Fact Table và Dimension Table khác nhau ở điểm gì? Bảng nào lưu 'sự kiện', bảng nào lưu 'ngữ cảnh'?"*

🛠️ **BÀI TẬP:**
```
Input: Công dân Nguyễn Văn A (CCCD: 012345678901)
  - Ngày 01/01/2020: Thường trú tại Hải Dương
  - Ngày 01/07/2026: Chuyển về Hà Nội

Yêu cầu: Điền vào bảng trong RESEARCH_03_DATA_MODELING.md —
  Với mỗi loại SCD, bảng dim_citizen trông như thế nào TRƯỚC và SAU khi A chuyển nhà?

Output mong đợi: Bảng có đủ dữ liệu 3 type, cột đúng, giải thích được dòng nào bị mất/giữ lại
File lưu: RESEARCH_03_DATA_MODELING.md (Phần 2)
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Hệ thống BHXH dùng SCD Type 1 cho địa chỉ thường trú. Đến năm 2027, Kiểm toán Nhà nước yêu cầu báo cáo: 'Năm 2024, tỉnh Hải Dương đã chi trả bao nhiêu tiền trợ cấp cho người thường trú tại đây?'. Kết quả báo cáo sẽ SAI như thế nào? Con số sẽ cao hơn hay thấp hơn thực tế?"*

---

## Task 1.3-B — Star vs Snowflake Schema: Tại sao Star luôn thắng trong Analytics
> ⏱️ 1 ngày | 📁 `01_DATA_WAREHOUSING_SQL/RESEARCH_03_DATA_MODELING.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.1: Star Schema cơ bản (đã biết khái niệm)
- Task 1.3-A: Dimension Table có thể có nhiều phiên bản theo thời gian (SCD)

🔗 **KẾT NỐI TƯƠNG LAI:** Task 1.4 (Partition trên Fact Table lớn) → Module 2 (Delta Lake Lakehouse thay thế DWH truyền thống)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Vẽ được sơ đồ Star Schema cho hệ thống BHXH (Fact + 4 Dimension)
- [ ] Giải thích tại sao Star Schema nhanh hơn Snowflake khi query Analytics
- [ ] Quyết định được khi nào dùng Snowflake (OLTP) và khi nào dùng Star (OLAP)

📖 **NỘI DUNG HỌC:**
- Star Schema: Fact Table ở trung tâm, Dimension denormalized xung quanh — ít JOIN, query nhanh
- Snowflake Schema: Dimension được normalize thêm — tiết kiệm dung lượng nhưng nhiều JOIN hơn
- Lý do Star thắng: Với ổ cứng cloud giá rẻ, tiết kiệm dung lượng không còn là ưu tiên. Tốc độ query mới quan trọng.

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"SCD Type 2 lưu lịch sử bằng cách nào? Khi Nguyễn Văn A đổi địa chỉ, bảng dim_citizen thay đổi như thế nào?"*

🛠️ **BÀI TẬP:**
```
Input: Hệ thống BHXH cần báo cáo: "Tổng tiền chi trả theo tỉnh, theo quý, theo loại trợ cấp"

Yêu cầu: Thiết kế Star Schema — vẽ bằng text theo format:
  fact_chi_tra (cột nào? khóa ngoại nào?)
  dim_thoi_gian (năm, quý, tháng, ngày)
  dim_dia_phuong (tỉnh, huyện, xã)
  dim_cong_dan (CCCD, tên, ngày sinh)
  dim_loai_tro_cap (tên loại, mức tối đa)

Output mong đợi: Sơ đồ text rõ ràng, tên cột hợp lý, FK đúng chỗ
File lưu: RESEARCH_03_DATA_MODELING.md (Phần 1)
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Analyst viết câu query join fact_chi_tra với 4 bảng Dimension. Trên Star Schema cần mấy lần JOIN? Nếu thiết kế Snowflake và dim_dia_phuong được tách thành dim_tinh → dim_huyen → dim_xa, query đó cần mấy lần JOIN? Với 1 tỷ dòng trong fact table, sự khác biệt đó ảnh hưởng thế nào đến thời gian chạy?"*

---

## Task 1.3-C — Surrogate Key: Tại sao CCCD không thể làm Primary Key
> ⏱️ 1 ngày | 📁 `01_DATA_WAREHOUSING_SQL/RESEARCH_03_DATA_MODELING.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.3-A: SCD Type 2 cần lưu nhiều dòng cho cùng 1 người
- Task 1.3-B: dim_citizen trong Star Schema cần PK không bao giờ thay đổi

🔗 **KẾT NỐI TƯƠNG LAI:** Task 1.4 (Index trên Surrogate Key integer nhanh hơn string) → Module 4 (dbt dùng Surrogate Key để xác định thay đổi trong Incremental models)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích 3 lý do không dùng Natural Key (CCCD) làm PK trong DWH
- [ ] Viết được SQL tạo bảng `dim_citizen` chuẩn SCD Type 2 với Surrogate Key
- [ ] Mô tả được toàn bộ quy trình: khi A chuyển nhà → INSERT dòng mới → UPDATE dòng cũ → Fact Table vẫn trỏ đúng lịch sử

📖 **NỘI DUNG HỌC:**
- Natural Key (Số CCCD): có thể thay đổi (đổi CCCD 9 số sang 12 số), null với người nước ngoài, chậm khi JOIN (string vs integer)
- Surrogate Key: số tự tăng (1, 2, 3...) do hệ thống tạo, không bao giờ thay đổi, nhanh khi JOIN
- Cơ chế SCD Type 2 với Surrogate Key: cùng 1 CCCD có thể có surrogate_key = 101 (địa chỉ cũ) và surrogate_key = 205 (địa chỉ mới)

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Star Schema có bao nhiêu lần JOIN ít hơn Snowflake Schema nếu có 3 cấp Dimension? Tại sao điều đó quan trọng với bảng Fact 1 tỷ dòng?"*

🛠️ **BÀI TẬP:**
```sql
-- Yêu cầu: Viết SQL hoàn chỉnh tạo bảng dim_citizen chuẩn SCD Type 2
-- Phải có đủ các cột cần thiết để:
--   1. Phân biệt dòng HIỆN TẠI và dòng LỊCH SỬ của cùng 1 công dân
--   2. JOIN với fact_chi_tra lấy đúng địa chỉ TẠI THỜI ĐIỂM giao dịch (không phải hiện tại)
--   3. Tìm nhanh tất cả giao dịch của CCCD = '012345678901' dù có nhiều surrogate_key

-- Viết vào RESEARCH_03_DATA_MODELING.md Phần 3
-- Output mong đợi: SQL chạy được trên SQLite/PostgreSQL, có comment giải thích từng cột
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Năm 2024, A thường trú tại Hải Dương — surrogate_key = 101. Năm 2026, A chuyển về Hà Nội — surrogate_key = 205. Bảng fact_chi_tra có cột dim_citizen_key. Giao dịch năm 2024 lưu dim_citizen_key = 101 hay 205? Tại sao điều này đảm bảo báo cáo lịch sử luôn chính xác dù A đã chuyển địa chỉ?"*

---

## Task 1.4-A — Index: Tại sao thiếu là "án tử" cho Data Warehouse
> ⏱️ 1 ngày | 📁 Tạo mới `01_DATA_WAREHOUSING_SQL/RESEARCH_04_QUERY_OPTIMIZATION.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.3-C: Surrogate Key integer — tại sao JOIN nhanh hơn string (liên quan đến B-Tree)
- Module 0 Task 8: Disk I/O — Random Write tốn kém hơn Sequential Read

🔗 **KẾT NỐI TƯƠNG LAI:** Task 1.4-B (Partition là Index ở cấp độ file) → Task 2.6 (Parquet columnar = Index tự nhiên cho từng cột)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích B-Tree Index hoạt động như thế nào (tương tự mục lục sách)
- [ ] So sánh Full Table Scan O(n) vs Index Scan O(log n) bằng ví dụ số cụ thể
- [ ] Chỉ ra được: Index giúp SELECT nhanh nhưng làm INSERT/UPDATE chậm hơn — trade-off này ảnh hưởng thế nào đến thiết kế DWH

📖 **NỘI DUNG HỌC:**
- B-Tree Index: cấu trúc cây nhị phân — tìm kiếm O(log n) thay vì O(n)
- Full Table Scan: đọc toàn bộ bảng từ đầu đến cuối
- Index Scan: nhảy thẳng đến vị trí cần tìm qua B-Tree
- Trade-off: Index tốn thêm dung lượng + làm chậm INSERT/UPDATE (phải cập nhật B-Tree)

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Giải thích Surrogate Key + SCD Type 2: khi Nguyễn Văn A chuyển nhà, bảng dim_citizen thay đổi như thế nào? Bảng fact_chi_tra có cần UPDATE không?"*

🛠️ **BÀI TẬP:**
```python
# Yêu cầu: Chạy 2 query sau trên practice.db và đo thời gian

# Query 1: Không có Index
SELECT * FROM fact_sales WHERE tinh_id = 'Tinh_A';

# Query 2: Tạo Index rồi chạy lại
CREATE INDEX idx_tinh ON fact_sales(tinh_id);
SELECT * FROM fact_sales WHERE tinh_id = 'Tinh_A';

# Sau đó chạy EXPLAIN QUERY PLAN cho cả 2 query
EXPLAIN QUERY PLAN SELECT * FROM fact_sales WHERE tinh_id = 'Tinh_A';

# Output mong đợi: Screenshot/text kết quả EXPLAIN, ghi chú sự khác biệt
# "SCAN TABLE" (full scan) vs "SEARCH TABLE USING INDEX" (index scan)
# File lưu: RESEARCH_04_QUERY_OPTIMIZATION.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Bảng fact_chi_tra có 1 tỷ dòng, không có Index. Query WHERE cccd = '012345678901' cần đọc bao nhiêu dòng trong trường hợp xấu nhất? Nếu có B-Tree Index trên cột cccd, cần đọc bao nhiêu dòng (log₂ của 1 tỷ ≈ bao nhiêu)? Vì sao DWH thường đặt Index trên FK (khóa ngoại) thay vì toàn bộ các cột?"*

---

## Task 1.4-B — Partitioning: Chia nhỏ bảng 1 tỷ dòng
> ⏱️ 1 ngày | 📁 `RESEARCH_04_QUERY_OPTIMIZATION.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.4-A: Index giúp database nhảy đến đúng dòng cần tìm
- Task 1.3-B: dim_thoi_gian trong Star Schema — dữ liệu thường truy vấn theo khoảng thời gian

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.6 (Parquet Partition hoạt động tương tự nhưng ở cấp độ file) → Task 6.1 (BigQuery Partition là tính năng cốt lõi để tiết kiệm chi phí)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Phân biệt Range Partition (theo ngày/năm) và List Partition (theo tỉnh)
- [ ] Giải thích Partition Pruning: tại sao query theo năm không cần đọc file các năm khác
- [ ] Viết SQL tạo bảng partitioned theo năm trên PostgreSQL

📖 **NỘI DUNG HỌC:**
- Partition: chia bảng vật lý thành nhiều "ngăn" riêng biệt trên ổ cứng
- Range Partition: theo khoảng (năm 2024 → file/ngăn riêng, năm 2025 → file/ngăn riêng)
- List Partition: theo danh sách (tỉnh Hà Nội → ngăn riêng, HCM → ngăn riêng)
- Partition Pruning: database chỉ mở đúng ngăn cần thiết, bỏ qua toàn bộ các ngăn còn lại

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Tại sao Index làm INSERT chậm hơn? Với DWH thường batch load 1 lần/ngày, điều này có phải vấn đề lớn không?"*

🛠️ **BÀI TẬP:**
```sql
-- Yêu cầu: Viết SQL tạo bảng fact_giao_dich_partitioned trên PostgreSQL
-- Partition theo năm (Range Partition trên cột ngay_giao_dich)
-- Tạo partitions cho năm 2023, 2024, 2025, 2026

-- Sau đó viết EXPLAIN cho câu query sau và giải thích tại sao nó nhanh:
EXPLAIN SELECT SUM(so_tien) FROM fact_giao_dich_partitioned
WHERE ngay_giao_dich BETWEEN '2024-01-01' AND '2024-12-31';

-- Output mong đợi: SQL tạo bảng + output EXPLAIN cho thấy "Partitions: 2024 only"
-- File lưu: RESEARCH_04_QUERY_OPTIMIZATION.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Bảng fact_giao_dich có 5 năm dữ liệu (2022-2026), mỗi năm 200 triệu dòng = 1 tỷ dòng tổng. Query 'Tổng chi trả Q1/2024' trên bảng Partition theo năm — database mở bao nhiêu ngăn? Đọc tối đa bao nhiêu dòng? So với bảng không Partition phải đọc bao nhiêu dòng? Tại sao kết hợp Partition (cấp file) + Index (cấp dòng) lại là combo hoàn hảo?"*

---

## Task 1.4-C — EXPLAIN ANALYZE: Đọc bản đồ tư duy của Database
> ⏱️ 1 ngày | 📁 `RESEARCH_04_QUERY_OPTIMIZATION.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.4-A: Biết sự khác biệt Seq Scan vs Index Scan
- Task 1.4-B: Biết Partition Pruning tồn tại

🔗 **KẾT NỐI TƯƠNG LAI:** Module 2 (Spark EXPLAIN cho thấy DAG execution plan tương tự) → Task 6.1 (BigQuery Execution Plan cùng triết lý)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Đọc output EXPLAIN ANALYZE và chỉ ra được: query chậm ở bước nào
- [ ] Nhận biết 3 dấu hiệu nguy hiểm: Seq Scan trên bảng lớn, Hash Join tốn RAM, Sort tốn I/O
- [ ] Tối ưu được ít nhất 1 query chậm trong practice.db bằng Index phù hợp

📖 **NỘI DUNG HỌC:**
- EXPLAIN: cho biết database *dự kiến* làm gì
- EXPLAIN ANALYZE: chạy thật và cho biết *thực tế* đã làm gì (cost, rows, time)
- Seq Scan: đọc toàn bộ → nguy hiểm với bảng lớn
- Index Scan: dùng B-Tree → nhanh
- Hash Join: build hash table trong RAM → cẩn thận với bảng rất lớn
- Nested Loop: O(n×m) → nguy hiểm khi cả 2 bảng đều lớn

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Partition Pruning hoạt động thế nào? Nếu query không có điều kiện WHERE trên cột partition, database có pruning được không? Hậu quả là gì?"*

🛠️ **BÀI TẬP:**
```python
# Yêu cầu: Chạy các query sau trên practice.db, đọc EXPLAIN QUERY PLAN
# Tìm và sửa ít nhất 1 query chậm bằng cách tạo Index phù hợp

# Query A (chậm): JOIN 2 bảng không có Index
# Query B (chậm): Filter trên cột không có Index
# Query C (bạn viết): 1 câu query từ Challenge Window Functions cũ
#   → EXPLAIN xem nó đang dùng Seq Scan hay Index Scan?

# Output mong đợi:
# - Before: output EXPLAIN với Seq Scan
# - After: CREATE INDEX + output EXPLAIN mới với Index Scan
# - Ghi chú: thời gian trước và sau (ms)
# File lưu: RESEARCH_04_QUERY_OPTIMIZATION.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Đọc output EXPLAIN ANALYZE sau và chẩn đoán vấn đề: 'Seq Scan on fact_giao_dich (cost=0.00..85432.00 rows=1000000) (actual time=0.043..3421.823 rows=1 loops=1)'. Dòng này nói gì? Database dự kiến tìm bao nhiêu dòng? Thực tế trả về bao nhiêu? Tại sao actual time cao đến vậy? Giải pháp là gì?"*

---

## Task 2.0 — Medallion Architecture & Cloud-native Storage: Kiến trúc hiện đại thay HDFS
> ⏱️ 1 ngày | 📁 Tạo `02_DISTRIBUTED_SYSTEMS/RESEARCH_00_MODERN_ARCHITECTURE.md`

🔗 **XÂY DỰNG TỪ:**
- Task 1.3-B: Star Schema (DWH truyền thống) → Lakehouse thay thế cả DWH + Data Lake
- Module 0 Task 7: ETL pipeline — Medallion tổ chức lại các tầng ETL

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.1-2.8 (HDFS/Spark chạy trên nền này) → Task 4.6 (dbt xây dựng Silver/Gold layer bằng SQL) → Task 6.1 (BigQuery dùng Medallion natively)

> [!IMPORTANT]
> **Tại sao Task này quan trọng hơn HDFS?** Năm 2026, 90% dự án DE mới không dùng HDFS. Họ dùng S3/GCS + Parquet/Iceberg. Hiểu Medallion Architecture trước để không bị lạc lối khi học các công cụ tiếp theo.

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích Medallion Architecture: Bronze → Silver → Gold layer làm gì
- [ ] So sánh: Cloud Object Storage (S3/GCS) vs HDFS — khi nào dùng cái nào
- [ ] Mô tả tại sao Lakehouse (Delta Lake/Iceberg trên S3) đang thay thế DWH + Data Lake riêng biệt

📖 **NỘI DUNG HỌC:**
- **Bronze (Raw):** Dữ liệu thô 1-1 từ nguồn — bất biến, không xóa, audit trail (giống Raw Zone Module 0)
- **Silver (Cleansed):** Đã làm sạch, chuẩn hóa schema, join các nguồn — ready for analysis
- **Gold (Business):** Aggregated, business logic applied — báo cáo, dashboard, ML features
- **Cloud Storage thay HDFS:** S3/GCS lưu file Parquet/Iceberg — không cần NameNode/DataNode, trả tiền theo GB
- **Lakehouse:** Một hệ thống duy nhất thay vì DWH (OLAP) + Data Lake riêng biệt

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"EXPLAIN ANALYZE báo 'Seq Scan on fact_giao_dich rows=1000000000' — bạn sẽ làm gì? Index hay Partition trước? Tại sao?"*

🛠️ **BÀI TẬP:**
```
Tình huống: Bộ Nội vụ cần xây Data Platform cho 63 tỉnh thành.
Hiện tại: Oracle DB tại mỗi tỉnh (Legacy, on-premise)
Mục tiêu: Báo cáo thống nhất toàn quốc + khả năng phân tích lịch sử 10 năm

Yêu cầu: Thiết kế Medallion Architecture cho hệ thống này:

  BRONZE layer:
  - Dữ liệu đến từ đâu? Lưu định dạng gì? Tổ chức thư mục thế nào?
  - Ví dụ: s3://bucket/bronze/noi_vu/ho_so/year=2026/month=08/tinh=HN/

  SILVER layer:
  - Transform những gì từ Bronze? Schema chuẩn hóa như thế nào?
  - Join với bảng nào? Validation rules nào?

  GOLD layer:
  - Bảng nào phục vụ báo cáo Bộ trưởng?
  - Bảng nào phục vụ tra cứu công dân?
  - Bảng nào phục vụ ML (nếu có)?

Output mong đợi: Sơ đồ text 3 layer với tên bảng/file cụ thể
File lưu: RESEARCH_00_MODERN_ARCHITECTURE.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Trước đây kiến trúc cổ điển: ETL đẩy dữ liệu vào Data Warehouse (Star Schema) để analyst query. Lakehouse thay đổi điều này thế nào? Tại sao cùng 1 file Parquet trên S3 vừa có thể query bằng Spark (DE), vừa query bằng SQL (Analyst), vừa đọc bằng Python Pandas (Data Scientist) — mà không cần copy dữ liệu sang 3 hệ thống khác nhau?"*

---

## Task 2.1 — HDFS: Khi ổ cứng đơn không còn đủ
> ⏱️ 1 ngày | 📁 Tạo `02_DISTRIBUTED_SYSTEMS/RESEARCH_01_HDFS.md`

🔗 **XÂY DỰNG TỪ:**
- Module 0 Task 3: LVM mở rộng đĩa — nhưng vẫn giới hạn 1 máy vật lý
- Module 0 Task 5: SSH — cách máy tính giao tiếp an toàn qua mạng

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.2 (YARN quản lý tài nguyên cluster trên cùng các node này) → Task 2.3 (Spark đọc dữ liệu từ HDFS, xử lý tại chỗ — data locality)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Vẽ được sơ đồ HDFS: NameNode, DataNode, Block 128MB, Replication Factor 3
- [ ] Giải thích tại sao NameNode là SPOF (Single Point of Failure) và cách khắc phục
- [ ] Mô tả được: khi đọc file 1GB, HDFS làm gì — bao nhiêu block, trên bao nhiêu máy

📖 **NỘI DUNG HỌC:**
- NameNode: "thư mục" lưu metadata (file nào ở block nào, trên DataNode nào)
- DataNode: máy thật lưu dữ liệu thô theo từng block 128MB
- Block: đơn vị lưu trữ tối thiểu. File 1GB = 8 blocks × 128MB
- Replication Factor 3: mỗi block được copy sang 3 DataNode khác nhau
- SPOF: nếu NameNode chết → không biết dữ liệu ở đâu → cluster tê liệt

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"EXPLAIN ANALYZE của bạn cho thấy Seq Scan trên 1 tỷ dòng mất 3421ms. Bạn tạo Index. Theo lý thuyết B-Tree, tìm kiếm trong 1 tỷ dòng cần tối đa bao nhiêu bước so sánh (log₂ của 1 tỷ)?"*

🛠️ **BÀI TẬP:**
```
Input: File dữ liệu dân số 63 tỉnh = 800GB
Cluster: 10 DataNode, mỗi máy có 1TB ổ cứng
Replication Factor: 3

Yêu cầu: Tính toán và vẽ sơ đồ text:
  1. File 800GB chia thành bao nhiêu block?
  2. Tổng dung lượng thực tế chiếm trên cluster (vì replication)?
  3. Nếu DataNode số 3 chết, HDFS mất dữ liệu không? Tự phục hồi thế nào?
  4. Vẽ: NameNode lưu metadata file "/data/dan_so.csv" trông như thế nào?

Output mong đợi: Sơ đồ text + tính toán đúng + giải thích cơ chế self-healing
File lưu: RESEARCH_01_HDFS.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Cơ sở dữ liệu quốc gia cần lưu 800GB dữ liệu. Phương án A: 1 máy chủ 4TB SSD (scale-up). Phương án B: 10 máy mỗi 500GB HDD + HDFS (scale-out). Về chi phí, khả năng mở rộng, và fault tolerance — phương án nào phù hợp hơn cho hệ thống cần 99.99% uptime? Điểm yếu của HDFS là gì mà phương án A không có?"*

---

## Task 2.2 — YARN: Người điều phối tài nguyên cluster
> ⏱️ 1 ngày | 📁 `02_DISTRIBUTED_SYSTEMS/RESEARCH_02_YARN.md`

🔗 **XÂY DỰNG TỪ:**
- Task 2.1: HDFS có nhiều DataNode — nhưng ai quyết định job chạy trên node nào?
- Module 0 Task 6: Cron chạy job — YARN là "Cron" nhưng cho distributed cluster

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.3 (Spark submit lên YARN — YARN cấp resource cho Spark executors) → Module 4 (Airflow submit job lên YARN qua SparkSubmitOperator)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích vai trò của ResourceManager, NodeManager, ApplicationMaster, Container
- [ ] Mô tả luồng: Submit Spark job → YARN phân bổ → chạy → kết thúc
- [ ] Giải thích Fair Scheduler vs FIFO Scheduler — khi nào dùng cái nào

📖 **NỘI DUNG HỌC:**
- ResourceManager (RM): "Bộ tư lệnh" — biết toàn bộ cluster có bao nhiêu CPU/RAM còn trống
- NodeManager (NM): "Trưởng ca" trên mỗi máy — báo cáo tài nguyên khả dụng lên RM
- ApplicationMaster (AM): "Project Manager" của từng job — xin tài nguyên từ RM, phân công cho các task
- Container: đơn vị tài nguyên tối thiểu (VD: 1 core + 4GB RAM)

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"File 800GB trên HDFS với Replication Factor 3 — 1 DataNode chết. HDFS làm gì ngay sau đó? NameNode biết chuyện này qua cơ chế nào (Heartbeat)?"*

🛠️ **BÀI TẬP:**
```
Tình huống: Cluster có 5 NodeManager, mỗi NM có 16 core + 64GB RAM
Đang chạy: 3 Spark jobs đồng thời

Yêu cầu: Vẽ sơ đồ text mô tả:
  1. Khi Job A submit: ResourceManager làm gì? NodeManager nào được chọn?
  2. Job A cần 8 executors × (2 core + 8GB RAM) — YARN cấp phát như thế nào?
  3. Nếu Job B submit đồng thời và cluster đang 80% tài nguyên, Job B phải chờ không?
  4. Job A xong, tài nguyên được giải phóng như thế nào?

Output mong đợi: Sơ đồ text rõ ràng + giải thích từng bước
File lưu: RESEARCH_02_YARN.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Mỗi đêm 2h sáng có 5 Spark ETL jobs chạy cùng lúc (1 job cho mỗi vùng kinh tế). Cluster có tổng 100 core + 400GB RAM. Nếu dùng FIFO Scheduler, job nào submit trước chạy trước — hậu quả khi job đầu tiên nặng là gì? Fair Scheduler giải quyết vấn đề này thế nào? Liên hệ với Module 0: tại sao cần chạy lúc 2h sáng thay vì ban ngày?"*

---

## Task 2.3 — Spark Internals: Tại sao Spark nhanh hơn MapReduce 100 lần
> ⏱️ 2 ngày | 📁 `02_DISTRIBUTED_SYSTEMS/RESEARCH_03_SPARK.md`

🔗 **XÂY DỰNG TỪ:**
- Task 2.1-2.2: Cluster có HDFS (lưu trữ) + YARN (quản lý tài nguyên)
- Module 0 Task 8: Generator — lazy evaluation. Spark áp dụng cùng triết lý ở quy mô cluster

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.4 (Shuffle là bước tốn kém nhất trong DAG) → Task 2.5 (Optimization để giảm Shuffle) → Module 3 (Spark Streaming = Spark Batch + micro-batch loop)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích DAG (Directed Acyclic Graph) và tại sao Spark không chạy ngay (Lazy Evaluation)
- [ ] Phân biệt Transformation (lười) vs Action (chạy thật)
- [ ] Đọc Spark UI và chỉ ra: Stage nào chậm nhất, tại sao

📖 **NỘI DUNG HỌC:**
- Lazy Evaluation: `df.filter().groupBy()` chỉ là *kế hoạch*, chưa chạy gì
- Action trigger execution: `.show()`, `.count()`, `.write` → Spark mới build DAG và chạy
- Stage: tập hợp các Transformation có thể chạy cùng nhau mà không cần Shuffle
- Task: đơn vị nhỏ nhất, chạy trên 1 partition của 1 executor

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"YARN ResourceManager và ApplicationMaster khác nhau thế nào? Khi Job A fail, AM làm gì trước tiên?"*

🛠️ **BÀI TẬP:**
```python
# Yêu cầu: Viết Spark job hoàn chỉnh (PySpark)
# Đọc file raw_sales_data.csv từ Module 0
# Transform: lọc dòng lỗi, chuẩn hóa ngày, tính tổng theo tháng
# Load: ghi ra file Parquet

from pyspark.sql import SparkSession
# Viết code tại đây

# Sau khi chạy:
# 1. Xem Spark UI tại localhost:4040
# 2. Chụp màn hình DAG visualization
# 3. Ghi chú: có bao nhiêu Stage? Stage nào có Shuffle?

# Output mong đợi: Code chạy được + screenshot DAG + giải thích
# File lưu: RESEARCH_03_SPARK.md + spark_etl.py
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Code Spark: `df = spark.read.csv(...).filter(...).groupBy(...).agg(...).orderBy(...)`. Spark thực sự chạy bao nhiêu lần quét dữ liệu? Tại sao MapReduce cũ phải đọc/ghi HDFS sau mỗi bước (làm chậm gấp 100 lần), còn Spark thì không? Điều gì xảy ra nếu cluster hết RAM và Spark phải Spill to Disk?"*

---

## Task 2.4 — Spark Shuffle: Kẻ thù số 1 của hiệu năng
> ⏱️ 1 ngày | 📁 `RESEARCH_03_SPARK.md`

🔗 **XÂY DỰNG TỪ:**
- Task 2.3: DAG có nhiều Stage — Shuffle xảy ra giữa các Stage
- Task 1.4-B: Partition trong SQL DB — Spark cũng có Partition nhưng ở RAM/disk

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.5 (Optimization để tránh/giảm Shuffle) → Task 3.4 (CDC Debezium giúp tránh Full Scan — tương tự tránh Shuffle trong Spark)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Phân biệt Narrow Transformation (không Shuffle) vs Wide Transformation (có Shuffle)
- [ ] Giải thích Data Skew là gì và tại sao 1 node xử lý 90% dữ liệu là thảm họa
- [ ] Nhận biết được: câu lệnh nào trong code Spark sẽ gây Shuffle

📖 **NỘI DUNG HỌC:**
- Narrow: `filter`, `map` — mỗi output partition chỉ cần 1 input partition → không cần network
- Wide: `groupBy`, `join`, `orderBy` — dữ liệu phải di chuyển qua network → Shuffle
- Shuffle: mạng tắc nghẽn + disk I/O + RAM → bước tốn kém nhất trong pipeline
- Data Skew: Hà Nội có 10x dữ liệu → 1 task chạy mãi trong khi 62 task kia đã xong

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Spark DAG có 3 Stage. Stage 2 có dấu hiệu gì trong Spark UI cho thấy nó cần Shuffle? Shuffle ghi tạm dữ liệu ở đâu?"*

🛠️ **BÀI TẬP:**
```python
# Tình huống: Dataset 63 tỉnh, Hà Nội có 10 triệu dòng, các tỉnh còn lại 100k dòng
# Yêu cầu: Viết 2 phiên bản code, giải thích sự khác biệt:

# Phiên bản CHẬM (groupByKey - gây skew):
rdd.groupByKey().mapValues(list)

# Phiên bản NHANH (reduceByKey - pre-aggregate trước shuffle):
rdd.reduceByKey(lambda a, b: a + b)

# Câu hỏi: Trong Spark UI, Phiên bản CHẬM sẽ hiện gì bất thường ở Stage thực hiện groupByKey?
# Output mong đợi: Giải thích tại sao reduceByKey ít Shuffle hơn + diagram minh họa
# File lưu: RESEARCH_03_SPARK.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Pipeline Spark join bảng fact_giao_dich (1 tỷ dòng) với dim_tinh (63 dòng). Nếu dùng Hash Join thông thường, Spark phải Shuffle bảng 1 tỷ dòng qua network — mất bao nhiêu băng thông? Có kỹ thuật nào tránh hoàn toàn Shuffle cho bảng nhỏ (63 dòng) không? Gợi ý: broadcast"*

---

## Task 2.5 — Spark Optimization: Broadcast Join & Salting
> ⏱️ 1 ngày | 📁 `RESEARCH_03_SPARK.md`

🔗 **XÂY DỰNG TỪ:**
- Task 2.4: Shuffle là kẻ thù, Data Skew từ Hà Nội làm 1 task chạy mãi
- Task 1.4-A: Index tránh Full Scan — Broadcast tránh Shuffle (cùng triết lý: đưa dữ liệu nhỏ đến dữ liệu lớn)

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.8 (Mini Project — áp dụng tất cả optimization) → Task 4.1 (Airflow monitor Spark job — biết khi nào cần tune)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Viết Broadcast Join trong PySpark và giải thích khi nào nên/không nên dùng
- [ ] Giải thích kỹ thuật Salting để giải quyết Data Skew của Hà Nội
- [ ] Sử dụng `.cache()` đúng chỗ — biết khi nào cache có hại (tốn RAM vô ích)

📖 **NỘI DUNG HỌC:**
- Broadcast Join: copy bảng nhỏ sang mọi executor → join tại chỗ, không Shuffle
- Salting: thêm random prefix vào key của Hà Nội (HN_1, HN_2...) → chia đều 10M dòng sang nhiều task
- Cache/Persist: lưu DataFrame vào RAM để tái sử dụng — lãng phí nếu chỉ dùng 1 lần
- Partition tuning: `spark.sql.shuffle.partitions = 200` (default) — có thể quá nhiều hoặc quá ít

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Data Skew với Hà Nội 10M dòng — trong Spark UI, dấu hiệu nào cho thấy 1 task đang bị skew? Thời gian stage = max(task times) hay avg(task times)?"*

🛠️ **BÀI TẬP:**
```python
# Yêu cầu: Viết 2 phiên bản join, đo thời gian thực tế

# Phiên bản 1: Shuffle Join thông thường
fact_df.join(dim_tinh_df, "tinh_id")

# Phiên bản 2: Broadcast Join
from pyspark.sql.functions import broadcast
fact_df.join(broadcast(dim_tinh_df), "tinh_id")

# Giải thích: Tại sao Phiên bản 2 không cần Shuffle?
# Vẽ diagram: Phiên bản 1 vs Phiên bản 2 — dữ liệu di chuyển qua network như thế nào?

# Bonus: Giải thích kỹ thuật Salting cho Data Skew Hà Nội (text, không cần code)
# File lưu: RESEARCH_03_SPARK.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Kết hợp kiến thức từ Task 2.1 đến 2.5: Spark job đọc 800GB từ HDFS, join với bảng 63 tỉnh (10KB), groupBy tỉnh, ghi ra Parquet. Liệt kê các quyết định optimization bạn sẽ làm TRƯỚC KHI chạy: (1) HDFS? (2) YARN resource? (3) Join strategy? (4) Partition sau groupBy? (5) Output format?"*

---

## Task 2.6 — Parquet & Delta Lake: Định dạng lưu trữ của Big Data
> ⏱️ 1 ngày | 📁 `02_DISTRIBUTED_SYSTEMS/RESEARCH_04_STORAGE.md`

🔗 **XÂY DỰNG TỪ:**
- Module 0 Task 8: CSV vs Parquet — đã học cơ bản về columnar
- Task 1.4-A: Index trên cột → Parquet lưu theo cột = Index tự nhiên
- Task 1.4-B: SQL Partition theo năm → Parquet Partition theo thư mục `/year=2024/month=01/`

🔗 **KẾT NỐI TƯƠNG LAI:** Task 2.7 (Iceberg = Parquet + ACID + Time Travel) → Task 6.1 (BigQuery nội bộ dùng Colossus — tương tự Parquet columnar)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích tại sao `SELECT SUM(so_tien)` trên Parquet nhanh hơn CSV 100x
- [ ] Mô tả Delta Lake = Parquet + Transaction Log (JSON) — cơ chế ACID hoạt động thế nào
- [ ] Quyết định được: bài toán nào dùng Parquet thuần, bài toán nào cần Delta Lake

📖 **NỘI DUNG HỌC:**
- Row Storage (CSV): lưu hàng ngang — tốt cho INSERT/UPDATE, tệ cho analytical query
- Columnar (Parquet): lưu theo cột — chỉ đọc cột cần thiết, tỉ lệ nén cao, tốt cho Analytics
- Delta Lake: Parquet + `_delta_log/` JSON → biết file nào hợp lệ, file nào đã bị DELETE
- ACID trên Delta Lake: Atomicity (write thành công hay rollback), Isolation (đọc không bị ảnh hưởng bởi write đang chạy)

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Broadcast Join không có Shuffle — điều đó có nghĩa là gì với network I/O? Giới hạn của Broadcast Join là gì — bảng bao lớn thì không nên broadcast?"*

🛠️ **BÀI TẬP:**
```python
# Yêu cầu: Tạo 2 file cùng dữ liệu (CSV và Parquet) và so sánh

import pandas as pd
# Tạo DataFrame 1 triệu dòng với 10 cột
# Ghi ra CSV và Parquet
# Đo thời gian đọc chỉ cột "so_tien" từ mỗi file
# Đo dung lượng file

# Điền kết quả vào bảng:
# | Metric       | CSV    | Parquet |
# | Dung lượng   | ?MB    | ?MB     |
# | Thời gian đọc 1 cột | ?ms | ?ms |
# | Thời gian đọc toàn bộ | ?ms | ?ms |

# Giải thích: Tại sao Parquet đọc 1 cột nhanh hơn đọc toàn bộ không nhiều,
# còn CSV đọc 1 cột gần bằng đọc toàn bộ?

# File lưu: RESEARCH_04_STORAGE.md + parquet_vs_csv_test.py
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Kết hợp Module 0 (Idempotency) + Task 2.6 (Delta Lake): Spark job ghi 1 tỷ dòng ra Delta Lake, xong 50% thì server mất điện. Nếu dùng Parquet thuần — dữ liệu trông như thế nào? Nếu dùng Delta Lake — cơ chế Transaction Log bảo vệ dữ liệu thế nào? Tại sao Delta Lake mới đảm bảo Idempotency thật sự?"*

---

## Task 2.7 — Apache Iceberg: Time Travel & Schema Evolution
> ⏱️ 1 ngày | 📁 `RESEARCH_04_STORAGE.md`

🔗 **XÂY DỰNG TỪ:**
- Task 2.6: Delta Lake = Parquet + Transaction Log
- Task 1.3-A: SCD Type 2 lưu lịch sử thay đổi — Iceberg Time Travel làm điều tương tự ở cấp file

🔗 **KẾT NỐI TƯƠNG LAI:** Task 4.3 (Great Expectations validate dữ liệu trong Iceberg table) → Task 4.4 (Data Lineage trace lại từng snapshot)

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Giải thích Time Travel: xem lại bảng ở thời điểm bất kỳ trong quá khứ
- [ ] Mô tả Schema Evolution: thêm cột mới mà không làm hỏng data cũ
- [ ] So sánh Iceberg vs Delta Lake — khi nào chọn cái nào

📖 **NỘI DUNG HỌC:**
- Snapshot: mỗi lần write tạo 1 snapshot mới — có thể rollback về bất kỳ snapshot nào
- Time Travel: `SELECT * FROM table FOR TIMESTAMP AS OF '2026-08-01'`
- Schema Evolution: thêm cột mới → dòng cũ tự động hiển thị NULL cho cột mới
- Hidden Partitioning: Iceberg tự quản lý partition, không lộ ra trong query

🔄 **ÔN TẬP 5 PHÚT ĐẦU PHIÊN:**
> AI hỏi: *"Delta Lake Transaction Log bảo vệ Atomicity thế nào? Nếu Spark job fail sau khi write 50% file Parquet — Delta Lake xử lý thế nào khi đọc?"*

🛠️ **BÀI TẬP:**
```
Tình huống: ETL chạy ngày 10/08 và ghi sai dữ liệu vào Iceberg table
Ngày 11/08 mới phát hiện ra

Yêu cầu: Mô tả (text) quy trình recovery:
  1. Làm sao xem dữ liệu table tại thời điểm 09/08 (trước khi ETL sai)?
  2. Làm sao so sánh dữ liệu 09/08 vs 10/08 để tìm điểm sai?
  3. Làm sao rollback về snapshot 09/08?
  4. Sau khi rollback, snapshot 10/08 có còn không? Chi phí lưu trữ?

Thêm: Tại sao SCD Type 2 (Task 1.3-A) và Iceberg Time Travel đều giải quyết
cùng một vấn đề nhưng ở 2 tầng khác nhau (application layer vs storage layer)?

File lưu: RESEARCH_04_STORAGE.md
```

✅ **CÂU HỎI KIỂM TRA CUỐI BÀI:**
> *"Cơ sở dữ liệu quốc gia: Team A bổ sung cột 'ma_so_thue' vào bảng dim_citizen. Team B đang chạy pipeline đọc bảng đó. Nếu dùng Hive Metastore truyền thống — Team B's pipeline fail không? Nếu dùng Iceberg Schema Evolution — điều gì xảy ra với pipeline của Team B? Cột mới hiện ra giá trị gì với dữ liệu cũ?"*

---

## Task 2.8 — Mini Project: Spark Pipeline End-to-End
> ⏱️ 2 ngày | 📁 `02_DISTRIBUTED_SYSTEMS/mini_project_spark/`

🔗 **XÂY DỰNG TỪ:** Toàn bộ Task 2.1 → 2.7

---

🎯 **MỤC TIÊU — Sau bài này tôi CÓ THỂ:**
- [ ] Xây dựng pipeline Spark hoàn chỉnh từ raw data đến analytical store
- [ ] Áp dụng ít nhất 3 optimization đã học (Broadcast Join, Partition, Cache)
- [ ] Giải thích từng dòng code cho người không biết Spark

🛠️ **BÀI TẬP — Capstone Module 2:**
```
Input: File CSV 63 tỉnh (tạo fake data 10 triệu dòng bằng Python)
  - Cột: tinh_id, ngay_giao_dich, loai_tro_cap, so_cccd, so_tien, trang_thai

Yêu cầu xây dựng pipeline Spark với các bước:
  [E] Extract: Đọc CSV từ "HDFS" (dùng thư mục local thay thế)
  [V] Validate: Lọc dòng null, so_tien <= 0, định dạng ngày sai
  [T] Transform:
    - Join với dim_tinh (63 dòng) → Broadcast Join
    - Tính tổng chi trả theo (tinh_id, nam, quy, loai_tro_cap)
    - Tính tỷ lệ tăng trưởng so với quý trước (Window Function LAG từ Task 1.2)
  [L] Load: Ghi ra Delta Lake, partition theo nam/quy

Tiêu chí đạt:
  ✅ Code chạy được, không crash
  ✅ Có comment giải thích logic từng bước
  ✅ Áp dụng Broadcast Join cho dim_tinh
  ✅ Xử lý lỗi: nếu file không tồn tại, pipeline báo lỗi rõ ràng (không crash im lặng)
  ✅ Output Parquet/Delta có thể đọc lại và verify kết quả
```

---

# 📚 MODULE 3-6: REAL-TIME STREAMING → CLOUD & CERT

*(Cấu trúc tương tự — AI sẽ xây dựng chi tiết khi học đến)*

## Tóm tắt nhanh các Task còn lại:

| Task | Tên | Ngày | Xây dựng từ |
|---|---|---|---|
| **2.0** | **Medallion Architecture & Cloud Storage** *(MỚI)* | **7** | **Task 1.3 + Module 0 ETL** |
| 2.1 | HDFS | 8 | Module 0 Task 3+5 |
| 2.2 | YARN | 9 | Task 2.1 |
| 2.3 | Spark Internals + DAG | 10-11 | Task 2.1+2.2 |
| 2.4 | Spark Shuffle | 12 | Task 2.3 |
| 2.5 | Spark Optimization | 13 | Task 2.4 |
| 2.6 | Parquet & Delta Lake | 14 | Task 2.0 + Module 0 T8 |
| 2.7 | Apache Iceberg | 15 | Task 2.6 |
| 2.8 | Mini Project Spark | 16-17 | Task 2.1-2.7 |
| 3.1 | Kafka Pub/Sub | 18 | Module 0 Networking |
| 3.2 | Kafka Replication | 19 | Task 3.1 |
| 3.3 | Kafka Design | 20 | Task 3.1-3.2 |
| 3.4 | CDC Debezium | 21-22 | Module 0 ETL + Task 3.1 |
| 3.5 | Spark Streaming | 23-24 | Task 2.3 + Task 3.1 |
| 3.6 | Lambda Architecture | 25-26 | Task 2.8 + Task 3.5 |
| 4.1 | Airflow DAG | 27-28 | Module 0 Cron + Task 2.8 |
| 4.2 | Airflow Retry/Backfill | 29 | Task 4.1 |
| 4.3 | Great Expectations | 30-31 | Module 0 ETL Validation |
| 4.4 | Data Lineage | 32 | Task 4.3 |
| 4.5 | Automated Pipeline | 33-34 | Task 4.1-4.4 |
| **4.6** | **dbt: Transform bằng SQL thuần** *(MỚI)* | **35-36** | **Task 1.4 + Task 4.1 + Task 2.6** |
| 5.1 | Encryption | 37 | Module 0 SSH |
| 5.2 | Data Privacy | 38 | Task 5.1 |
| 5.3 | RBAC/ABAC | 39 | Module 0 PoLP |
| 5.4 | Compliance VN | 40 | Task 5.1-5.3 |
| 6.1 | BigQuery | 41-42 | Task 1.4 + Task 2.6 |
| 6.2 | Dataflow/Beam | 43-44 | Task 2.3 + Task 3.5 |
| 6.3 | Vertex AI | 45 | Task 2.6 + Task 4.3 |
| 6.4 | Mock Test | 46-48 | All modules |
| 6.5 | Capstone Project | 49-53 | All modules |

---

## 📊 MILESTONE VÀNG

| Cột mốc | Ngày | Dấu hiệu kiểm chứng |
|---|---|---|
| Module 1 xong | 17/08/2026 | Viết SQL SCD Type 2 + EXPLAIN ANALYZE không cần tra |
| Module 2 xong | 21/09/2026 | Spark pipeline 10M dòng chạy < 5 phút |
| Module 3 xong | 19/10/2026 | Thiết kế Kafka + CDC cho 63 tỉnh trên giấy |
| Module 4 xong | 09/11/2026 | Airflow DAG + GE tự chạy và alert khi lỗi |
| Module 5-6 xong | 07/12/2026 | Mock test 80%+ |
| **🎓 Thi thật** | **01/2027** | **Professional Data Engineer Certified** |

---

## 🔄 CƠ CHẾ ÔN TẬP TÍCH LŨY

### Spaced Repetition tự động (AI thực hiện đầu mỗi phiên):
```
Ngày 1-7:   Ôn bài ngày hôm qua
Ngày 8-14:  Ôn bài ngày hôm qua + 1 câu từ tuần trước
Ngày 15+:   Ôn bài hôm qua + 1 câu từ tuần trước + 1 câu từ module trước
```

### Review cuối Module (bắt buộc trước khi sang Module mới):
```
Câu hỏi tích hợp: Kết hợp 3-5 khái niệm của module vừa học
Phải trả lời được không tra cứu
Nếu không qua → ôn lại task đó, chưa được sang module mới
```

### Dòng chảy kiến thức — Sợi chỉ đỏ xuyên suốt:
```
Module 0 → Module 1: ETL Pipeline (Bash/Python) → SQL Analytics
Module 1 → Module 2: SQL Partition → Spark Partition; Index → Columnar Storage
Module 2 → Module 3: Spark Batch → Spark Streaming; HDFS → Kafka Topic
Module 3 → Module 4: Pipeline → Airflow Orchestration; Validation → Great Expectations
Module 4 → Module 5: Pipeline Security tích hợp vào mọi bước
Module 5 → Module 6: On-premise → Cloud (cùng concept, khác nền tảng)
```

---

## 📌 QUY TẮC VÀNG

1. **Không học nhảy cóc** — task sau chỉ mở khi đạt Câu hỏi Kiểm tra cuối bài
2. **Không copy-paste code** — mọi code phải gõ tay, giải thích được từng dòng
3. **Không bỏ ngày** — nếu bận, tối thiểu đọc lại Câu hỏi Kiểm tra của bài cũ
4. **Ghi log sai lầm** — format: `[❌ Câu cũ sai] → [✅ Đã hiểu lại — ngày]`
5. **Cập nhật DASHBOARD** — cuối mỗi phiên, bắt buộc

---
*Phiên bản: 2.0 — Cập nhật 11/08/2026 — Thêm Mục tiêu, Bài tập có cấu trúc, Cơ chế Ôn tập, Dòng chảy kiến thức*
