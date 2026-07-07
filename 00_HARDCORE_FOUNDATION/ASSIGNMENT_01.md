# 🚩 BÀI TẬP 01: TƯ DUY KIẾN TRÚC LƯU TRỮ VÀ QUẢN TRỊ LINUX

## 🏢 BỐI CẢNH (SCENARIO)
Cậu được giao nhiệm vụ thiết lập một Server Trung chuyển (Ingestion Server) tại Trung tâm Dữ liệu Quốc gia. Server này có nhiệm vụ nhận dữ liệu thô (Raw Data) từ **63 tỉnh thành** gửi về hàng ngày thông qua giao thức SFTP. 

Dữ liệu bao gồm:
1. Thông tin định danh cá nhân (PII - Rất nhạy cảm).
2. Dữ liệu biến động đất đai (Dung lượng rất lớn).
3. Dữ liệu bảo hiểm y tế (Tần suất gửi liên tục).

## 🛠️ YÊU CẦU (TASKS)

### Task 1: Thiết kế cấu trúc thư mục (Storage Layout)
Cậu không được phép ném tất cả vào một thư mục `/data`. Hãy thiết kế một cấu trúc thư mục trên Linux để:
- Phân tách dữ liệu theo Tỉnh/Thành.
- Phân tách theo Loại dữ liệu.
- Phân tách theo Trạng thái xử lý (Raw, Processing, Archive, Error).
*Yêu cầu:* Viết cấu trúc đó dưới dạng cây thư mục (Tree structure).

### Task 2: Quản trị người dùng & Quyền hạn (User Management & Permissions)
Có 3 nhóm nhân sự sẽ truy cập vào Server này:
1. **data_collector:** Chỉ có quyền ghi dữ liệu vào thư mục `Raw`, không được xem dữ liệu của tỉnh khác.
2. **data_analyst:** Chỉ được đọc dữ liệu trong thư mục `Processing`, không được xóa hay sửa.
3. **sys_admin:** Toàn quyền.
*Yêu cầu:* Cậu hãy liệt kê các câu lệnh Linux (`groupadd`, `useradd`, `chmod`, `chown`) để thực hiện việc này. Làm sao để đảm bảo `data_collector` của tỉnh Hà Nội không nhìn thấy dữ liệu của tỉnh TP.HCM?

### Task 3: Tư duy Tối ưu hóa (Optimization thinking)
Nếu một ngày dữ liệu đổ về quá lớn làm đầy phân vùng thư mục chứa dữ liệu `Raw`, hệ điều hành (chứa phân vùng `/`) bị treo, TTDLQG sẽ tê liệt. 
*Câu hỏi:* Để ngăn chặn thảm họa này, cậu sẽ tư vấn việc phân chia phân vùng (Partitioning) như thế nào khi cài đặt Linux Server? (Gợi ý: LVM - Logical Volume Manager).

## 📤 Nộp bài:
Cậu hãy viết câu trả lời vào file `SOLUTION_01.md` trong thư mục này. 
**Lưu ý:** Tôi sẽ chất vấn "Tại sao?" cho từng lựa chọn của cậu. Đừng trả lời hời hợt.
