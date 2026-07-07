import csv
from datetime import datetime
import os

# --- CẤU HÌNH ĐƯỜNG DẪN ---
INPUT_FILE = "raw_sales_data.csv"
OUTPUT_FILE = "refined_sales_data.csv"
ERROR_FILE = "error_rows.log"

def extract(file_path):
    """Bước 1: Trích xuất dữ liệu từ file CSV dưới dạng Streaming (Generator)
    Đọc đến đâu trả về đến đó để giữ lượng chiếm dụng RAM là O(1).
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} không tồn tại!")
        return
    
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def transform(raw_generator, error_file, stats, buffer_size=2):
    """Bước 2: 'Luyện' dữ liệu (Làm sạch & Biến đổi) dưới dạng Streaming
    - Nhận vào một Generator thô.
    - Yield ra từng dòng sạch (Generator sạch).
    - Gom lỗi vào bộ đệm (Buffer) và thực hiện ghi hàng loạt (Batch Write) 
      để giảm thiểu System Calls và bảo vệ Disk I/O.
    """
    error_buffer = []
    
    # Làm mới file log lỗi từ đầu quy trình
    if os.path.exists(error_file):
        try:
            os.remove(error_file)
        except OSError:
            pass
        
    for row in raw_generator:
        # Bỏ qua các dòng trống hoàn toàn trong file
        if not row or all(v is None or v.strip() == '' for v in row.values()):
            continue
            
        try:
            # 1. Kiểm tra dữ liệu bị thiếu cột quan trọng
            if not row.get('customer_name') or not row.get('amount') or not row.get('sale_date'):
                raise ValueError("Thiếu dữ liệu bắt buộc")

            # 2. Xử lý tên khách hàng (Upper case)
            customer_name = row['customer_name'].strip().upper()

            # 3. Xử lý số tiền (Amount) và lọc giá âm
            try:
                amount = float(row['amount'])
            except ValueError:
                raise ValueError(f"Giá tiền không hợp lệ: {row['amount']}")
            
            if amount < 0:
                raise ValueError(f"Số tiền âm: {amount}")

            # 4. Tính thuế (Tax 10%)
            tax_amount = amount * 0.1

            # 5. Xử lý định dạng ngày tháng (Normalize Date)
            date_str = row['sale_date'].replace('/', '-')
            dt = None
            
            # Thử nghiệm các định dạng ngày khác nhau
            for fmt in ('%Y-%m-%d', '%d-%m-%Y'):
                try:
                    dt = datetime.strptime(date_str, fmt)
                    break
                except ValueError:
                    continue
            
            if not dt:
                raise ValueError(f"Định dạng ngày không hợp lệ: {row['sale_date']}")

            # 6. Gom vào dictionary kết quả hoàn chỉnh
            refined_row = {
                'id': row['id'],
                'customer_name': customer_name,
                'amount': amount,
                'tax_amount': round(tax_amount, 2),
                'total_price': round(amount + tax_amount, 2),
                'sale_date': dt.strftime('%Y-%m-%d')
            }
            stats['clean_count'] += 1
            yield refined_row

        except Exception as e:
            # Thu thập lỗi vào Buffer (Nghệ thuật Trì hoãn)
            error_msg = f"Lỗi tại dòng ID {row.get('id', 'N/A')}: {str(e)}\n"
            error_buffer.append(error_msg)
            stats['error_count'] += 1
            
            # Khi bộ đệm đầy (đạt buffer_size), ta ghi 1 lần xuống ổ cứng
            if len(error_buffer) >= buffer_size:
                with open(error_file, mode='a', encoding='utf-8') as ef:
                    ef.writelines(error_buffer)
                print(f"[DISK I/O] 💾 BUFFER FULL: Đã ghi hàng loạt (Batch Write) {len(error_buffer)} dòng lỗi xuống {error_file}")
                error_buffer.clear()
                
    # Dọn nốt bộ đệm cuối cùng (Flush Buffer) trước khi kết thúc quy trình
    if error_buffer:
        with open(error_file, mode='a', encoding='utf-8') as ef:
            ef.writelines(error_buffer)
        print(f"[DISK I/O] 💾 FLUSH BUFFER: Ghi đợt cuối cùng {len(error_buffer)} dòng lỗi xuống {error_file}")
        error_buffer.clear()

def load(clean_generator, output_path):
    """Bước 3: Nạp dữ liệu sạch vào kho (Streaming Load)
    Ghi trực tiếp từng dòng lấy được từ Generator sạch vào đĩa,
    đảm bảo RAM không cần lưu trữ toàn bộ tập dữ liệu thành phẩm.
    """
    fieldnames = ['id', 'customer_name', 'amount', 'tax_amount', 'total_price', 'sale_date']
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in clean_generator:
            writer.writerow(row)

# --- CHẠY PIPELINE ---
def main():
    print("🚀 BẮT ĐẦU PIPELINE ETL TỐI ƯU HÓA (BIG DATA COMPLIANT - TASK 08)...")
    
    # Khởi tạo đối tượng theo dõi hiệu năng và kết quả
    stats = {
        'clean_count': 0,
        'error_count': 0
    }
    
    # E - Extract (Dạng Generator)
    raw_generator = extract(INPUT_FILE)
    print("📦 Đã khởi tạo luồng Streaming trích xuất (Extract Generator).")
    
    # T - Transform (Dạng Generator lồng nhau, sử dụng Buffer kích thước = 2 cho tập dữ liệu mẫu)
    clean_generator = transform(raw_generator, ERROR_FILE, stats, buffer_size=2)
    print("💎 Đã thiết lập bộ lọc biến đổi dữ liệu (Transform Filter).")
    
    # L - Load (Chạy toàn bộ luồng bằng cách rút dữ liệu từ Generator sạch và ghi xuống file)
    load(clean_generator, OUTPUT_FILE)
    
    print("\n=======================================================")
    print("✅ HOÀN TẤT PIPELINE ETL STREAMING!")
    print(f"📊 Dòng sạch đã nạp (Clean Rows Loaded): {stats['clean_count']}")
    print(f"⚠️ Dòng lỗi phát hiện & ghi theo Batch: {stats['error_count']}")
    print(f"📂 Xem nhật ký lỗi tại: {ERROR_FILE}")
    print("=======================================================")

if __name__ == "__main__":
    main()
