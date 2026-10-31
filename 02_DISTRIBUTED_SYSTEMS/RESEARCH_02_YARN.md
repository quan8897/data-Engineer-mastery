# ⚙️ RESEARCH 02 — YARN: NGƯỜI ĐIỀU PHỐI TÀI NGUYÊN CLUSTER

> **Task:** 2.2 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-09-08
> **Trạng thái:** 🔄 Đang Audit bài tập — 2026-09-08

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Hoàn thành bài này, bạn phải đạt được các năng lực cốt lõi:
1. **Bản chất điều phối tài nguyên:** Hiểu sâu vai trò của YARN như một "Hệ điều hành cụm" (Cluster OS), tách biệt hoàn toàn giữa lưu trữ (HDFS) và tính toán (Compute), hỗ trợ đa ứng dụng cùng lúc (Multi-tenancy).
2. **Mental Model & Vòng đời Job:** Thuộc lòng 4 thành phần (RM, NM, AM, Container) qua hình ảnh "Bất động sản"; vẽ và giải thích được 6 bước trong Job Lifecycle từ submit đến thu hồi Container.
3. **Cơ chế chịu lỗi (Fault-Tolerance):** Phân tích được các kịch bản hỏng hóc (NodeManager sập, AM sập, RM sập) và cách hệ thống tự khôi phục mà không làm mất trạng thái cả cụm.
4. **Tính toán & Tối ưu Container:** Hiểu cách cấu hình CPU/RAM (vCPU, yarn.nodemanager.resource.memory-mb) để tối ưu công suất phần cứng, tránh lãng phí hoặc gây OOM container.

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
YARN (Yet Another Resource Negotiator) là framework quản lý và điều phối tài nguyên (RAM, CPU) tập trung cho toàn bộ các ứng dụng chạy trên Hadoop cluster.
```

### Tầng 2 — HOW (4 thành phần & Mental Model)

```
Mental Model "Bất Động Sản":
- ResourceManager (RM) : Ông chủ đất / Tổng tư lệnh — Nắm toàn quyền phân phối tài nguyên cluster.
- NodeManager (NM)     : Người trông đất / Cai ngục — Quản lý trực tiếp RAM/CPU trên từng Worker Node.
- ApplicationMaster(AM): Người thuê đất — Đại diện cho 1 Job cụ thể, đi đàm phán xin tài nguyên từ RM.
- Container            : Mảnh đất đóng gói — Gói tài nguyên cô lập (VD: 2 vCPU + 8GB RAM) do NM cấp để chạy task.
```

#### Quy trình vòng đời 1 Job (Job Lifecycle):
1. **Submit:** Client gửi yêu cầu chạy Job lên **ResourceManager (RM)**.
2. **Khởi tạo AM:** RM chọn 1 NodeManager còn trống, ra lệnh mở **Container đầu tiên** để khởi chạy **ApplicationMaster (AM)** của Job.
3. **Đàm phán (Negotiate):** AM tính toán khối lượng công việc, trực tiếp liên hệ RM xin danh sách Container (kèm yêu cầu CPU, RAM, ưu tiên Data Locality).
4. **Thực thi (Execute):** AM cầm phiếu cấp phát từ RM đến từng NodeManager tương ứng để mở Container chạy các Spark Executor/Task.
5. **Giám sát:** NM giám sát mức tiêu thụ CPU/RAM của Container; AM theo dõi tiến độ các Task.
6. **Hoàn tất (Clean up):** Khi job xong, AM gửi tín hiệu hủy đăng ký (Unregister) trực tiếp cho RM. RM thông báo các NM thu hồi toàn bộ Container về kho tài nguyên chung.

### Tầng 3 — WHY
> *(Tại sao cần YARN? Không có YARN thì Spark submit job thế nào?)*

```
Nếu không có YARN: Hệ thống sẽ như "rắn mất đầu", các job tự do chiếm dụng tài nguyên dẫn đến tranh chấp, deadlock, sập OOM, và phân bổ không đều (máy quá tải, máy nhàn rỗi). YARN đem lại: Multi-tenancy (nhiều job/framework cùng chạy chung phần cứng), Load Balancing và Quản trị tài nguyên tập trung.
```

### Tầng 4 — FAILURE
> *(ResourceManager chết thì sao? ApplicationMaster chết thì sao?)*

```
- Nếu ResourceManager (RM) chết: Không còn ai phân bổ tài nguyên, cluster tê liệt (SPOF). Giải pháp: Bật YARN High Availability (HA) với 1 Active RM + 1 Standby RM (đồng bộ qua Zookeeper).
- Nếu ApplicationMaster (AM) chết: RM phát hiện qua timeout (không nhận được heartbeat của AM) → RM tự động khởi tạo lại AM mới trên một container khác và tiếp tục quản lý job (Retry fail-safe).
```

### Tầng 5 — TRADE-OFF
> *(FIFO Scheduler vs Fair Scheduler: khi nào dùng cái nào?)*

```
- FIFO Scheduler: Đến trước phục vụ trước theo thứ tự hàng đợi. Đơn giản, nhưng nhược điểm chí mạng là Job lớn đến trước sẽ chiếm sạch cluster làm các Job nhỏ đến sau bị "chết đói" (Starvation).
- Fair Scheduler: Chia sẻ tài nguyên linh hoạt và công bằng. Khi nhiều job chạy đồng thời, tài nguyên cluster được chia đều cho các job để job nào cũng được tiến triển, tránh tắc nghẽn.
```

---

## 🛠️ BÀI TẬP — YARN Resource Allocation cho Bộ Nội Vụ

**Tình huống:**
- Cluster: **5 NodeManager**, mỗi NM có **16 core + 64GB RAM**
  $\implies$ Tổng tài nguyên Cluster: **80 cores + 320GB RAM**.
- Mỗi đêm 2am: **3 Spark ETL jobs** chạy đồng thời (1 job/vùng kinh tế).

**Câu hỏi & Lời giải chuẩn:**

### Câu 1: Khi Job A submit — ResourceManager làm gì từng bước? NodeManager nào được chọn để chạy?
```
- Bước 1: RM tiếp nhận request từ Client, kiểm tra quyền và hạn mức tài nguyên (Queue).
- Bước 2: RM tìm 1 NodeManager có đủ tài nguyên nhàn rỗi (ví dụ NM1).
- Bước 3: RM ra lệnh cho NM1 cấp phát Container 01 để khởi chạy ApplicationMaster (AM) cho Job A.
- NodeManager được chọn: Là NodeManager thỏa mãn điều kiện còn đủ tài nguyên và có tải thấp nhất ở thời điểm đó.
```

### Câu 2: Job A cần 8 executors × (2 core + 8GB RAM). YARN cấp phát tổng bao nhiêu tài nguyên? Trên bao nhiêu NodeManager (nếu phân đều)?
```
- Tổng tài nguyên cấp cho 8 Executors:
    + CPU: 8 * 2 = 16 cores.
    + RAM: 8 * 8 = 64 GB RAM.
- Phân bổ đều trên Cluster 5 Node:
    + 8 executors phân đều cho 5 NodeManager (hoặc 4 NodeManager):
      Mỗi NodeManager nhận từ 1 đến 2 executors (chiếm 2-4 cores và 8-16GB RAM mỗi máy).
    + Tuyệt đối KHÔNG dồn cả 8 executors vào 1 Node duy nhất vì sẽ chiếm 100% tài nguyên của Node đó, vi phạm nguyên tắc cân bằng tải (Load Balancing) và mất tính chịu lỗi phân tán (Fault Tolerance).
```

### Câu 3: Cluster đang chạy 80% tài nguyên, Job B submit đồng thời. FIFO vs Fair Scheduler sẽ xử lý thế nào?
```
- FIFO Scheduler: Job B BẮT BUỘC PHẢI CHỜ (Queue). Do Job A đang chiếm quyền ưu tiên, 20% tài nguyên còn lại không đủ hoặc chính sách FIFO không cho phép Job B chạy xen ngang → Job B bị nghẽn (Block) cho đến khi Job A nhả tài nguyên.
- Fair Scheduler: Không để Job B chết đói. Fair Scheduler sẽ cấp ngay 20% tài nguyên rảnh rỗi cho Job B chạy trước các task đầu tiên, đồng thời điều tiết/thu hồi dần một phần tài nguyên của Job A để cân bằng lại tỷ trọng (Dynamic Re-balancing) cho cả 2 Job cùng chạy.
```

### Câu 4: Job A xong — tài nguyên được giải phóng thế nào? Ai thông báo cho ResourceManager?
```
- Khi các task cuối cùng hoàn thành, ApplicationMaster (AM) trực tiếp gửi bản tin "Finish/Success" lên ResourceManager (RM).
- RM ghi nhận và gửi lệnh tới các NodeManager đang chạy Executor của Job A yêu cầu tiêu hủy (kill/release) các Container.
- Tài nguyên (16 core + 64GB RAM) lập tức được trả lại vào Resource Pool của Cluster để phục vụ Job khác.
- Cuối cùng, Container chứa chính AM cũng được giải phóng.
```

---

## 📝 Ghi Chú Cá Nhân & Đúc Kết

```
- RM quản lý vĩ mô toàn cluster; NM quản lý vi mô từng máy worker.
- Mỗi Job có đúng 1 ApplicationMaster riêng — AM sinh ra trước rồi mới đi xin Executor sau.
- FIFO gây Starvation; Fair Scheduler chia đều tài nguyên chống nghẽn.
- AM là người trực tiếp báo công việc hoàn thành cho RM để thu hồi Container.
```
