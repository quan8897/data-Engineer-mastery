# TASK 08: NỘI CÔNG TRUYỀN DỮ LIỆU (DSA & DISK I/O FOR BIG DATA)

## 📍 TÌNH TRẠNG HIỆN TẠI
- Cậu đã biết dùng Python để đọc file và xử lý logic (ETL).
- Nhưng hãy tưởng tượng file `raw_sales_data.csv` không phải 11 dòng, mà là **11 tỷ dòng (khoảng 800GB)**.
- Liệu script `etl_mini_pipeline.py` hiện tại có chạy nổi không? (Gợi ý: Nó sẽ nạp toàn bộ vào list `data = []` và hệ thống sẽ báo `Internal Error: Out of Memory` ngay lập tức).

## 🎯 NHIỆM VỤ (MISSION)
Cậu phải hiểu cách một Kỹ sư Dữ liệu thực thụ quản lý tài nguyên hệ thống (RAM/CPU/Disk) khi đối mặt với dữ liệu quy mô lớn. 

## ⚔️ GIAO THỨC HUẤN LUYỆN
Tôi muốn cậu thực hiện nghiên cứu và trả lời các câu hỏi "Sống còn" sau đây vào file `RESEARCH_08_DSA_BIGDATA.md`:

### 1. Trận chiến với RAM (Streaming vs Batch)
- **Câu hỏi:** Trong script `etl_mini_pipeline.py` của cậu, hàm `extract` đang đọc toàn bộ file vào một list. Nếu file lớn hơn RAM của máy chủ, chuyện gì sẽ xảy ra?
- **Yêu cầu:** Hãy mô tả cách dùng `Iterator` hoặc `Generator` trong Python để đọc file theo kiểu "Streaming" (đọc đến đâu xử lý đến đó) thay vì nạp tất cả một lúc.

### 2. Disk I/O: Kẻ thù thầm lặng
- **Câu hỏi:** Tại sao việc ghi log lỗi từng dòng một (`ef.write(...)` trong vòng lặp) khi xử lý hàng triệu dòng lại cực kỳ chậm? 
- **Yêu cầu:** Tìm hiểu về khái niệm **Buffer (Bộ đệm)**. Làm sao để gom các dòng lỗi lại rồi ghi một lần (Batch Write) để tăng tốc độ?

### 3. Cấu trúc dữ liệu: Row-based vs Column-based
- **Câu hỏi:** Tại sao các hệ thống Big Data quốc gia lại dùng định dạng file **Parquet** thay vì **CSV**? 
- **Yêu cầu:** Giải thích sự khác biệt giữa lưu trữ theo dòng (CSV) và theo cột (Parquet) dưới góc độ "Disk Seek Time" (Thời gian tìm kiếm dữ liệu trên ổ cứng).

---
*Ghi nhớ:* "Một Senior DE không chỉ code chạy đúng, mà còn phải code chạy cực nhanh với tài nguyên cực ít!"
