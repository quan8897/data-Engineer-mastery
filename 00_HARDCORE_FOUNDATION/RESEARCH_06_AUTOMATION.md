# NGHIÊN CỨU & BẢO VỆ KIẾN TRÚC: TASK 06 (AUTOMATION & CHẠY NGẦM)

> **Luật chơi:** Trả lời bằng ngôn ngữ kỹ thuật của chính bản thân. Không dùng từ bác học, không tra Google rồi Copy/Paste lại. Feynman Technique yêu cầu cậu giải thích cho Mentor như thể giải thích cho một Kỹ sư tập sự (thử dụng ẩn dụ/so sánh đời sống khi cần).

---

## 1. Cơ Chế Lập Lịch: Cron và Ma Trận 5 Ngôi Sao

- **`cron` là gì? Tại sao phải gõ `crontab -e` thay vì viết thẳng vào file nào đó?**
 - cron là một tiện ích dòng lệnh tích hợp sẵn trong các hệ điều hành tương tự unix như linux, được sử dụng để chạy các tiến trình như lệnh, script vv theo lịch được định sẵn. có thể lên lịch cho các tác vụ như bảo trì hệ thống, tự động chạy sao lưu, hoặc các tác vụ lặp đi lặp lại như tải xuống tệp tin, gửi gmail, truyền file từ 63 tỉnh về trung tâm chẳng hạn, hay kiểm tra log định kì và cảnh báo định kì.
 các thuật ngữ tôi tìm hiểu được:
 - cron tab, cron deamon, anacron, slack, cron job
 - crontab -e là thêm một cron job, gõ lệnh để chạy hàng loạt chứ nếu viết thằng vào file thì rối và khi số lượng file quá lớn thì ko thể chính thủ công được, việc thiết lập dòng lệnh giống như góm nhóm chúng để thực thi vậy.

- **Cho ví dụ: Làm cách nào lập lịch chạy một Tác vụ Dữ liệu (chỉ chạy vào lúc `2h30 sáng mỗi Thứ Ba`) trên ma trận `* * * * *`?**
  *(Điền câu trả lời của cậu: ...)*
* * * * *   <lệnh cần thực thi>
| | | | |
| | | | thiết lập theo thứ trong tuần (0-6)sunday to saturday
| | | thiết lập theo tháng (1-12)
| | thiết lập theo ngày trong tháng (1-31)
| thiết lập theo giờ (0-23)
thiết lập theo phút   (0-59)
30 2 * * 2 <tác vụ cần xử lý>
## 2. Tiếng Mếu Má Đêm của Server (Standard Error - 2>&1)

- **Nếu Cron gọi shell script ra chạy lúc 2h sáng, Terminal không mở thì cái lỗi "File Not Found" ấy sẽ văng vào đâu?**
  *(Điền câu trả lời của cậu: ...)* sẽ văng vào file log hệ thống
 nếu không thực thi được lệnh sẽ ghi vào log
- **Các Sysadmin đời đầu để lại dòng chú thuật lạ lùng: `> /dev/null 2>&1`. Hãy dùng khái niệm Dòng Nước (Luồng Thác Cống) để giải thích 1 là gì, 2 là gì và phép "&1" đóng vai trò bẻ ống cống ra sao?**
  *(Điền câu trả lời của cậu: ...)*
hình dung có 3 đường ống khi thực thi lệnh
0-input đầu vào
1- kết quả output hiển thị trên terminal
2- lỗi nếu có, vd command not found
2>&1: tức là ghi kết quả lỗi vào cùng với đường ống kết quả, &1 là tên đường ống để biểu thị không phải là file tên là 1.

1 đại diện cho kết quả, 2 đại diện cho lỗi, cả 2 sẽ cùng được ghi vào 1 file để kiểm tra truy xuất lại lỗi trong log, dù chạy thành công hay lỗi
- **Bonus:** Nếu không phải đổ xuống hố đen `/dev/null`, một Data Engineer như cậu sẽ nối cái ống nước báo lỗi (`stderr`) này vào phễu nào?
  *(Điền câu trả lời của cậu: ...)*
vào phễu kết quả chạy hàng ngày
## 3. Cái bẫy Môi Trường Sinh Thái của Cron (The Cron Env Trap)

- **Vì sao Data Engineer thường vò đầu bứt tai than vãn: "Script rsync gõ bằng tay chạy băng băng. Đẩy vào Cron thì lăn đùng ra chết và báo Lỗi Command Nền (Command not found)?"**
  *(Điền câu trả lời của cậu: ...)*
cron sẽ chạy lỗi nếu $PATH ko cụ thể hoặc gõ sai
- **Làm thế nào cung cấp oxy (Môi trường/đường dẫn $PATH) chuẩn cho Cron "thở" được lệnh rsync?**
  *(Điền câu trả lời của cậu: ...)*
có 3 cách: đó là gắn đường dẫn trực tiếp, thêm source (nạp oxy, năng lượng) cho cron nó thực thi, khai báo crontab -e sau đó khai báo các $PATH cụ thể trong file bash 

## 4. Ma Cổ Đại `nohup` và `&`

- **Giả lập:** Lúc 9h sáng, có chỉ thị khẩn cấp kéo tay 5 Terabyte dữ liệu từ tỉnh xa bằng lệnh `rsync ...`. Cậu gõ lệnh, sau đó lỡ tay bấm phím X tắt cái cửa sổ Terminal đi. Điều kinh hoàng gì chờ đợi tiến trình `rsync` kia? Vì sao?
  *(Điền câu trả lời của cậu: ...)*
nếu tắt đột ngột như vậy, thì việc đồng bộ sẽ bị dừng đột ngột, điều kinh hoàng là dữ liệu chưa kịp đẩy về trung tâm hoàn thiện đã bị gián đoạn
- **Vậy câu lệnh `nohup rsync ... &` thì cái `nohup` (đứng đầu) và dấu `&` (đứng cuối) cụ thể đã cast (giáng) phép bảo vệ nào cho cục Data Pipeline của cậu?**
  *(Điền câu trả lời của cậu: ...)*
dấu & tượng trưng cho chạy ngầm tại Background, lệnh đồng bộ sẽ chạy ngầm mà ko làm ảnh hưởng đến công việc khác của data engineer, 

nohup (Chặn việc bị giết khi đóng Terminal) + & (Đẩy vào chạy ngầm để mình làm việc khác).
---
*(Sau khi điền xong, báo cáo: "Hoàn tất Research 06". Mentor sẽ chất vấn.)*


----phiên chất vấn---------
1. Lỗi "Thứ Hai hay Thứ Ba"? (Lần cuối)
Cậu vẫn đang để 30 2 * * 1. Nếu tôi là hệ thống, tôi sẽ thức dậy vào Thứ Hai (Monday).

Chất vấn: Sửa lại dòng đó trong file Research cho đúng ngày Thứ Ba (Tuesday). Và hãy nói cho tôi biết: Nếu tôi muốn chạy vào ngày mùng 1 hàng tháng, 5 ngôi sao đó sẽ biến hình thế nào?
nếu chạy vào ngày mùng 1 hàng tháng: * * 1 / * <tác vụ>         ; / là mỗi
2. Phép thuật bẻ ống cống (Redirects)
Cậu bảo 2>&1 là bẻ ống lỗi vào chung với ống kết quả. Chính xác!

Chất vấn: Nếu cậu dùng > /dev/null 2>&1, thì "ống kết quả" đang đổ vào đâu? Cậu có bao giờ tìm lại được log lỗi trong đó không?
ống kết quả đổ vào đường dẫn /dev/null chắc sẽ tạo log trong đường dẫn này
Thử thách: Hãy viết cho tôi cú pháp để gom cả Success và Error vào một file tên là pipeline.log để sau này còn biết đường mà debug. 
> user/log/pipeline.log 2>$1 : giải sử dường dẫn đến file là user/log/pipeline.log
3. Oxy cho Cron ($PATH)
Cậu liệt kê 3 cách: dùng đường dẫn tuyệt đối, source, hoặc khai báo PATH.

Chất vấn: Cách nào là "an toàn và lười biếng nhất" (Best Practice) mà một Senior thường dùng để không phải đi gõ đường dẫn tuyệt đối cho từng lệnh trong script? (Gợi ý: Chỉ cần 1 dòng ở đầu file shell script là đủ). 
cách 2, 3 thường được sử dụng hơn cách 1; cách an toàn và lười nhất là cách 3, khai báo các đường dẫn có thể chứa lệnh cần tìm; bằng cách này sẽ có 1 tập các đường dẫn được sử dụng $PATH=....:....:....: mỗi 2: là một đường dẫn
4. Phân biệt Đối xử (nohup vs Cron)
Chất vấn: Nếu tôi có một tác vụ cần chạy đều đặn vào 3h sáng mỗi ngày, tôi dùng nohup tác_vu & hay dùng Cron? Tại sao? nohup có tự "thức dậy" vào ngày mai được không?
tác vụ cần chạy auto vào 3h sáng mỗi ngày thì dùng cron: * 3 / * * <tác vụ>
nohub <tác vụ> & được thực thi trên terminal tại thời điểm chạy, ko phải là tiến trình auto, chúng chỉ điều phối chạy nền và thực thi tiếp khi thức dậy nếu hệ thống bị tắt đột ngột, giống như theo dõi tiến trình và kiểm tra nếu ko hoàn thành sẽ tiếp tục hoàn thành cho xong