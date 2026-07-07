# 🛠️ GIẢI PHÁP HỆ THỐNG - MODULE 0

## TASK 1: THIẾT KẾ CẤU TRÚC THƯ MỤC INGESTION (SFTP)
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
### 1. Sơ đồ cây thư mục (Directory Tree)
`[Cậu hãy điền sơ đồ dạng tree ở đây]`
/data
   |---raw(bronze) dữ liệu thô
   |    |---20260314(partition by date)- phân cấp từ lớn xuống bé 
            để tra cứu được nhanh nhất
   |        |---HaNoi   
   |        |   |---20260314_191501_HN_BHYT_001.csv
   |        |   |---20260314_191501_HN_DATDAI_001.csv
   |        |---HoChiMinh
   |
   |---processing (sliver) dữ liệu qua xử lý (chuan hoa, lam sach,
                                         xacthuc)
   |---archive(gold/cold) dữ liệu gốc qua xu ly lưu trữ riêng cho mục
                            đích truy xuất lại, khi bị mất data, kiemtra
   |---error (quanrantine) dữ liệu lỗi ko xu ly đc, dùng để làm căn 
                        cứ trao đổi lỗi với đơn vị chuyển dữ liệu



### 2. Giải thích Logic (Tại sao?)
- **Tại sao phân cấp như vậy?**
tôi phân cấp như vậy để dễ trong quản lý, tìm kiếm dữ liệu, ngăn nắp và gọn gàng, phân cấp để mục đích xử lý được thuận tiện, lwuu trữ dễ quản lý
- **Làm sao để xử lý trường hợp cùng một tỉnh gửi nhiều loại dữ liệu cùng lúc?**sẽ đặt tên theo quy tắc để đảm bảo ko bị thất thoát dữ liệu>> sau đó mới tiến hành phân loại dữ liệu
- **Quy tắc đặt tên (Naming Convention) cho các file dữ liệu là gì?**
đúng vậy phần này tôi đã thiếu yếu tố timestap chúng phải đảm bảo yếu tố thời gian để truy vấn về sau, ko bị thất thoát dữ liệu
ví dụ: yyyymmdd_hhmmss_mã tỉnh_mã ngành_serial(unique)
tôi nghĩ điều này đã đảm bảo tính bất biến immutability, phân từ năm, tháng ngày, rồi h phút s, nhằm mục đích truy xuất dữ liệu được nhanh nhất; giống như co dần phạm vi tìm kiếm vậy 
---
*Mentor Note: Đừng cố vẽ cho đẹp, hãy vẽ cho đúng và giải thích được cái đầu óc của cậu đang nghĩ gì.*
