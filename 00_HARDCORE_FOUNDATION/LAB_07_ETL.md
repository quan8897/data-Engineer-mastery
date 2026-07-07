# 🧪 LAB 07: XÂY DỰNG LÒ LUYỆN DỮ LIỆU ETL MINI
		
## 🎯 MỤC TIÊU
Thực thi quy trình ETL cơ bản bằng Python để hiểu cách kiểm soát luồng dữ liệu, xử lý lỗi và đảm bảo tính nhất quán (Consistency).

## 🛠️ ĐỀ BÀI (MISSION)
Cậu có một file `raw_sales_data.csv` chứa dữ liệu thô. Hãy viết script `etl_mini_pipeline.py` để:

1. **Extract:** Đọc dữ liệu từ file csv thô.
2. **Transform:**
   - Chuyển `customer_name` thành CHỮ HOA.
   - Kiểm tra `amount`: Nếu số âm, coi là dữ liệu lỗi và ghi vào một file log riêng (`error_rows.log`), không nạp vào kết quả cuối.
   - Thêm cột `tax_amount` (10% của `amount`).
   - Chuyển định dạng ngày tháng về chuẩn `YYYY-MM-DD`.
3. **Load:** Lưu kết quả đã làm sạch vào file `refined_sales_data.csv`.

## 📜 YÊU CẦU KỸ THUẬT
- Sử dụng thư viện `csv` và `datetime` (Không dùng Pandas ở bài này để luyện tư duy logic).
- Phải có cơ chế xử lý lỗi (Try-Except) nếu dòng dữ liệu bị thiếu cột hoặc sai định dạng.
- In ra báo cáo tổng kết khi kết thúc:
  - Tổng số dòng đã đọc.
  - Số dòng xử lý thành công.
  - Số dòng bị loại bỏ do lỗi.

---
**Dữ liệu mẫu để chuẩn bị (Mentor đã tạo):** `raw_sales_data.csv`
