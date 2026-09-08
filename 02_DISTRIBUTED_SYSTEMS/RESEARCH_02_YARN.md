# ⚙️ RESEARCH 02 — YARN: NGƯỜI ĐIỀU PHỐI TÀI NGUYÊN CLUSTER

> **Task:** 2.2 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-08
> **Trạng thái:** 🔒 Chưa bắt đầu

---

## 🔗 Kết nối kiến thức cũ

```
Task 2.1 (HDFS): Cluster có 10 DataNode lưu dữ liệu
                 → Nhưng AI quyết định JOB chạy trên NODE NÀO?
                 → Đó là việc của YARN

Module 0 Task 6: Cron chạy job đơn lẻ theo lịch
                 → YARN = "Cron thông minh" cho distributed cluster
                 → Có retry, có resource allocation, có nhiều job đồng thời
```

---

## 🧠 Framework 5 Tầng — YARN

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1 câu)*

```
[Học viên điền vào đây]
```

### Tầng 2 — HOW (4 thành phần)

#### ResourceManager (RM)
```
[Học viên mô tả: RM là gì? Biết gì? Làm gì? Bao nhiêu cái?]
```

#### NodeManager (NM)
```
[Học viên mô tả: NM là gì? Khác RM thế nào? Chạy ở đâu?]
```

#### ApplicationMaster (AM)
```
[Học viên mô tả: AM là gì? Ai tạo ra AM? AM làm gì?]
```

#### Container
```
[Học viên mô tả: Container là gì? Chứa gì? Đơn vị tài nguyên thế nào?]
```

### Tầng 3 — WHY
> *(Tại sao cần YARN? Không có YARN thì Spark submit job thế nào?)*

```
[Học viên điền vào đây]
```

### Tầng 4 — FAILURE
> *(ResourceManager chết thì sao? ApplicationMaster chết thì sao?)*

```
[Học viên điền vào đây]
```

### Tầng 5 — TRADE-OFF
> *(FIFO Scheduler vs Fair Scheduler: khi nào dùng cái nào?)*

```
[Học viên điền vào đây]
```

---

## 🛠️ BÀI TẬP — YARN Resource Allocation cho Bộ Nội Vụ

**Tình huống:**
- Cluster: **5 NodeManager**, mỗi NM có **16 core + 64GB RAM**
- Mỗi đêm 2am: **3 Spark ETL jobs** chạy đồng thời (1 job/vùng kinh tế)

**Yêu cầu:** Vẽ sơ đồ text và trả lời:

```
Câu 1: Khi Job A submit — ResourceManager làm gì từng bước?
        NodeManager nào được chọn để chạy?

Câu 2: Job A cần 8 executors × (2 core + 8GB RAM)
        YARN cấp phát tổng bao nhiêu tài nguyên?
        Trên bao nhiêu NodeManager (nếu phân đều)?

Câu 3: Cluster đang chạy 80% tài nguyên, Job B submit đồng thời.
        FIFO Scheduler → Job B làm gì?
        Fair Scheduler → Job B làm gì?

Câu 4: Job A xong — tài nguyên được giải phóng thế nào?
        Ai thông báo cho ResourceManager?
```

### Câu 1
```
[Học viên vẽ sơ đồ + giải thích]
```

### Câu 2
```
[Học viên tính toán]
```

### Câu 3
```
[Học viên so sánh 2 scheduler]
```

### Câu 4
```
[Học viên giải thích cơ chế giải phóng tài nguyên]
```

---

## 📝 Ghi Chú Cá Nhân

```
[Học viên điền vào đây]
```
