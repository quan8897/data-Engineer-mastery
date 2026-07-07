# 🧪 LAB 06: AUTOMATION & BACKGROUND PROCESS - ĐÃ HOÀN THÀNH ✅
		
## 📋 NHIỆM VỤ GIAO:
1. Tạo file log `rsync_pipeline.log`.
2. Lập lịch Cron chạy `cleanup_provinces.sh` lúc 02:00 sáng hàng ngày.
3. Điều hướng toàn bộ kết quả (Success & Error) vào file log.
4. Kiểm tra bằng `crontab -l`.

## 🛠️ KẾT QUẢ THỰC THI (EVIDENCE):

### 1. Phân tích cú pháp Crontab chuẩn:
Để chạy lúc 2h00 sáng và ghi log an toàn, cú pháp đúng là:
`0 2 * * * /home/ACER/data-Engineer-mastery/cleanup_provinces.sh >> /home/ACER/data-Engineer-mastery/rsync_pipeline.log 2>&1`

*Giải thích:*
- `0 2 * * *`: 2 giờ 0 phút, mỗi ngày, mỗi tháng, mỗi thứ.
- `>>`: Ghi thêm (Append) vào cuối file để không làm mất log cũ.
- `2>&1`: Bẻ ống lỗi (stderr) vào chung với ống kết quả (stdout) để không bỏ sót thông tin khi hệ thống gặp sự cố.

### 2. Kiểm chứng kỹ thuật:
- Script `cleanup_provinces.sh`: Đã cấu hình "Fail-safe" (`set -euo pipefail`) và "Trap" xử lý tín hiệu ngắt.
- Trạng thái: **DONE**
- Ngày nghiệm thu: 2026-04-06

---
*Mentor Note: "Cậu đã biết cách bắt máy móc làm việc thay mình khi đang ngủ. Đó là bước tiến lớn của một kỹ sư. Chào mừng tới Task 07!"*