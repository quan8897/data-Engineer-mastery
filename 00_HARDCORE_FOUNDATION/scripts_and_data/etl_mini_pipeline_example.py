import csv

# 1. Mở file thô ĐỂ ĐỌC (mode='r')
with open('raw_sales_data.csv', mode='r') as fin:
    # 2. Mở file sạch ĐỂ GHI (mode='w')
    with open('refined_sales_data.csv', mode='w', newline='') as fout:
        
        reader = csv.DictReader(fin)
        
        # Khai báo các cột cho file sạch
        fieldnames = ['id', 'customer_name', 'amount', 'tax', 'total']
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader() # Ghi dòng tiêu đề
        
        for row in reader:
            try:
                amount = float(row['amount'])
                if len(row['customer_name']) > 0 and amount > 0:
                    # Giai đoạn Transform (Xử lý)
                    tax = amount * 0.1
                    total = amount + tax
                    name = row['customer_name'].upper()
                    
                    # Giai đoạn Load (Ghi từng dòng vào file sạch)
                    writer.writerow({
                        'id': row['id'],
                        'customer_name': name,
                        'amount': amount,
                        'tax': tax,
                        'total': total
                    })
                    print(f"✅ Đã nạp thành công: {name}")
                else:
                    print(f"🗑️ Bỏ qua dòng logic sai: {row['id']}")
            except:
                print(f"❌ Bỏ qua dòng lỗi kỹ thuật: {row['id']}")

print("\n🚀 CHÚC MỪNG! DỮ LIỆU ĐÃ ĐƯỢC LƯU VÀO KHO AN TOÀN.")
