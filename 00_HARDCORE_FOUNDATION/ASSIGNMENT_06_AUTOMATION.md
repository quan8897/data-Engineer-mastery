# TASK: 06 - DATA PIPELINE AUTOMATION (CRON & BACKGROUND PROCESSES)

## Bối cảnh (Context)
Tại Trung tâm Dữ liệu Quốc gia, cậu đã thiết lập thành công đường hầm bảo mật SSH an toàn từ 63 tỉnh về trung tâm (Task 5), đồng thời sở hữu kịch bản `cleanup_provinces.sh` có khả năng dọn dẹp dữ liệu an toàn (Task 4). 

Tuy nhiên, mọi thứ vẫn đang được kích hoạt BẰNG TAY. Nếu cậu xin nghỉ ốm, dữ liệu sẽ bị dồn đọng và rác sẽ chất đống làm đầy ở nhớ. Ở cấp độ của một Kỹ sư Dữ liệu hệ thống cốt lõi, bắt con người làm những việc lặp đi lặp lại có tính chu kỳ là một sự sỉ nhục với công nghệ. 

## Nhiệm vụ (Mission)
Auto-Pilot: Cậu phải tự động hóa toàn bộ Data Pipeline. 
Hệ thống phải tự thức dậy dọn rác lúc 2:00 sáng, tự động mở cổng kéo dữ liệu lúc 3:00 sáng. Mọi lệnh thực thi phải chạy ngầm trong im lặng (background execution). Đổi lại, vì nó chạy ngầm, cậu phải hiểu sâu sắc về luồng dữ liệu lỗi (Standard Errors) để không bị mù tịt khi có đứt gãy.

## Giao thức: The Flipped Classroom (Lớp học đảo ngược)

Để bảo vệ hệ thống không bị biến thành một cỗ máy tự động văng lỗi tung tóe, cậu phải chứng minh sự hiểu biết về cơ chế lõi trước khi gõ lệnh.

Mở file `RESEARCH_06_AUTOMATION.md` (tôi đã tạo sẵn) và trả lời 4 vấn đề sau bằng Kỹ thuật Feynman (sử dụng ngôn ngữ của chính cậu, cấm học vẹt, cấm copy-paste định nghĩa Wikipedia):

1. **Cron & 5 Ngôi sao Định mệnh:** `cron` daemon là gì? Cấu hình `* * * * *` hoạt động như thế nào? (Thử giải đố: Để chạy job lúc `2:30 sáng vào mỗi Thứ Ba`, cậu sẽ ghi như thế nào?).
2. **Dòng đời của Log (stdout vs stderr):** Khi chạy ngầm, script lấy đâu ra màn hình để in lỗi? Câu nói chú thuật `> /dev/null 2>&1` mà các lão đại hay dùng thực chất nghĩa là gì? (Gợi ý: giải nghĩa con số 1 và 2). Đối với đường ống dữ liệu, tống lỗi vào hố đen `/dev/null` có phải là ý hay không?
3. **Ảo ảnh Môi trường (The Cron Environment Trap):** Một script Bash chạy trên terminal của cậu thì thành công, lên Cron thì chết ngắc với lỗi "command not found". Vì sao Cron lại "ngu" hơn terminal bình thường, và kiến trúc sư cấu hình thế nào để khắc phục?
4. **Bóng Ma Tiến Trình (nohup & ngầm hóa):** Một Job chạy rsync dữ liệu tốn 10 tiếng đồng hồ. Chạy terminal được nửa tiếng thì cậu lỡ tay bấm `X` tắt cửa sổ. Tiến trình bị gì? Kỹ thuật dùng `nohup` kết hợp với `&` (ví dụ `nohup script.sh &`) cứu mạng hệ thống như thế nào?

---
*Hoàn thành file Research và báo cáo lại. Tôi sẽ tiến hành Tấn Công (Attack) ngay khi cậu nộp bài.*
