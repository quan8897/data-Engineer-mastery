# ⚡ RESEARCH 03 — APACHE SPARK INTERNALS: TRÁI TIM CỦA BIG DATA

> **Task:** 2.3 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-09
> **Trạng thái:** 🔄 Đang học

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
[Học viên điền vào đây]
```

### Tầng 2 — HOW (Kiến trúc & Cơ chế vận hành)

#### 1. RDD (Resilient Distributed Dataset) là gì?
```
[Học viên mô tả: RDD là gì? Tại sao gọi là Resilient? Tại sao gọi là Distributed?]
```

#### 2. Transformations vs Actions & Lazy Evaluation
```
[Học viên phân biệt:
- Transformation (map, filter, groupBy) khác Action (count, collect, save) thế nào?
- Lazy Evaluation là gì? Tại sao Spark không chạy ngay khi gọi Transformation?]
```

#### 3. Narrow Dependency vs Wide Dependency (Shuffling)
```
[Học viên phân biệt:
- Narrow Dependency (map, filter) là gì? Dữ liệu có phải nhảy qua mạng không?
- Wide Dependency (groupByKey, join) là gì? Shuffling nguy hiểm thế nào?]
```

#### 4. DAG (Directed Acyclic Graph) & Execution Plan
```
[Học viên mô tả: Ai vẽ ra DAG? DAG chia thành các Stage và Task thế nào?]
```

### Tầng 3 — WHY
> *(MapReduce vs Apache Spark: Tại sao Spark nhanh hơn MapReduce gấp 10-100 lần?)*

```
[Học viên điền vào đây]
```

### Tầng 4 — FAILURE
> *(Trong Spark, nguyên nhân phổ biến nhất gây sập OOM (Out Of Memory) của Executor là gì? Data Skew là gì?)*

```
[Học viên điền vào đây]
```

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG nên dùng Spark?)*

```
[Học viên điền vào đây]
```

---

## 🛠️ BÀI TẬP — Thiết Kế Pipeline Spark Dân Số 63 Tỉnh

**Tình huống:**
- Bạn có 1 file Parquet 800GB lưu dữ liệu CCCD của 100 triệu dân trên HDFS.
- Yêu cầu: Đếm số lượng người theo từng Tỉnh/Thành và tìm Top 5 tỉnh đông dân nhất.

**Câu hỏi:**
1. Đoạn pipeline: `df.filter(age > 18).groupBy("province").count().show(5)`:
   - Các hàm nào là **Transformation**? Các hàm nào là **Action**?
   - Tại dòng nào thì Spark thực sự bắt đầu kích hoạt cluster để tính toán?
2. Trong chuỗi lệnh trên, bước nào gây ra **Shuffling (Wide Dependency)** qua mạng giữa các máy?
3. Nếu tỉnh TP.HCM có 15 triệu dân còn tỉnh Bắc Kạn chỉ có 300.000 dân, điều gì sẽ xảy ra với Executor nhận partition của TP.HCM? Khái niệm này gọi là gì?

---

## 📝 Ghi Chú Cá Nhân

```
[Học viên điền vào đây]
```
