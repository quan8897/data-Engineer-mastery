# 📈 NHẬT KÝ CHIẾN THẮNG (DATA ENGINEERING JOURNEY)

## ✅ MODULE 0: THE HARDCORE FOUNDATION
### Giai đoạn 1: Architecture Thinking
- [x] **Task 1: Thiết kế Ingestion Storage Layout.**
    - *Thành tựu:* Hiểu về Data Life Cycle (Raw, Processing, Archive, Error), tính bất biến (Immutability), và kỹ thuật phân đoạn dữ liệu theo thời gian (Date Partitioning).
    - *Ngày hoàn thành:* 2026-03-14

- [x] **Task 2: Quản trị Đặc quyền & PoLP.**
    - *Thành tựu:* Thành thạo logic phân quyền `711/700`, hiểu sâu về nguyên tắc đặc quyền tối thiểu (**Principle of Least Privilege**) để bảo mật dữ liệu nhạy cảm.
    - *Ngày hoàn thành:* 2026-03-15

- [x] **Task 3: Tối ưu phân vùng & LVM.**
    - *Thành tựu:* Hiểu về cách cô lập phân vùng dữ liệu để tránh sập hệ thống (System Isolation) và kỹ thuật mở rộng đĩa không dừng máy (**Zero Downtime Expansion**).
    - *Ngày hoàn thành:* 2026-03-15

- [x] **Task 4: Tự động hóa dọn dẹp dữ liệu (Cleanup Pipeline).**
    - *Thành tựu:* Xây dựng hoàn chỉnh `cleanup_provinces.sh` với 4 lớp bảo vệ: **Fail-safe** (`set -euo pipefail`), **Trap** (SIGINT/SIGTERM), **Dry-run** (biến môi trường), **Audit Logging** (ISO-8601 + `tee`). Hiểu sâu về `-exec ... +` (batch processing), `-type f` (tránh xóa thư mục), và vai trò của Visual Separator trong log vận hành.
    - *Ngày hoàn thành:* 2026-03-21

- [x] **Task 5: Kỹ nghệ Mạng & SSH Tunneling (Networking & SSH Tunneling).**
    - *Thành tựu:* Hoàn thành cả lý thuyết lẫn Lab Terminal thực chiến. Hiểu bản chất xác thực bất đối xứng SSH Key (Public/Private, Passphrase vs Password). Cấu hình WSL, rủi ro bảo mật NOPASSWD qua sudo/su. Mô phỏng luồng truyền tải Data Center 63 tỉnh. Xử lý triệt để bài toán đứt cáp mạng với `rsync` kết hợp cờ bảo toàn (`-avz`, `--partial`, `--append-verify`) thông qua mô phỏng gián đoạn `Ctrl+C` khi truyền file 1GB (`fallocate`).
    - *Ngày hoàn thành:* 2026-04-01

- [x] **Task 6: Tự động hóa & Chạy ngầm (Cron & Background Processes).**
    - *Thành tựu:* Làm chủ cơ chế lập lịch `Cron` (5 ngôi sao), giải quyết triệt để lỗi môi trường `$PATH` trong automation. Thành thạo kỹ thuật điều hướng luồng dữ liệu (`2>&1`, `/dev/null`) để quản lý log hệ thống. Hiểu và áp dụng `nohup` kết hợp `&` để duy trì tiến trình truyền tải dữ liệu lớn bền bỉ ngay cả khi ngắt kết nối Terminal.
    - *Ngày hoàn thành:* 2026-04-05

- [x] **Task 7: Xây dựng Lò luyện dữ liệu (ETL Foundation).**
    - *Thành tựu:* Tự tay thiết kế pipeline ETL mini bằng Python (không dùng thư viện ngoài). Hiểu về tính bất biến của dữ liệu Raw, cơ chế lọc lỗi (Validation) và ghi log audit (`error_rows.log`). Bước đầu chạm tay vào khái niệm **Idempotency** (Tính khả dĩ) - yếu tố sống còn của một hệ thống dữ liệu tin cậy.
    - *Ngày hoàn thành:* 2026-04-07

---
*Mentor Note: "Từ một người bốc vác dữ liệu (Data Mover), cậu đã bắt đầu trở thành một người thợ tinh chế dữ liệu (Data Refiner). Đừng dừng lại ở file CSV, thế giới SQL và Big Data đang chờ phía trước!"*
