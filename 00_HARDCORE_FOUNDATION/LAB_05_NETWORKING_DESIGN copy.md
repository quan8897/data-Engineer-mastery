📋 ĐỀ BÀI: Thiết kế sơ đồ truyền dữ liệu an toàn từ 63 tỉnh về TTDLQG bằng ASCII art hoặc mô tả luồng. Phải thể hiện rõ:

1. xác thực: SSH Key Auth — Public Key được đặt ở đâu, Private Key ở đâu?
2. Truyền dữ liệu: Dùng rsync hay SCP? Flags nào? Tại sao?
3. Kịch bản tỉnh không có IP Public: Dùng -L hay -R? Ai chạy lệnh?
4. Phòng chống MITM: Cơ chế nào được kích hoạt tự động?

để truyền dữ liệu từ tỉnh về server: chúng ta có mô hình nhiều client->server
1. về xác thực public key sẽ được chuyển từ máy trạm sang máy chủ, máy chủ xác thực, còn private key sẽ đặt ở máy trạm, mỗi trạm là vs chủ là một bộ public/private key khác nhau
2. việc truyền dữ liệu từ 63 tỉnh về trung tâm dùng rsync vì rsync tối ưu hơn, dữ liệu của tỉnh đưa lên rất lớn và rất nhiều đơn vị nên việc dùng rsync hợp lý hơn dùng scp, dùng rsync cũng giúp xử lý sự cố khi truyền file bị các lỗi như mất điện, hay bị ngắt đột ngột.
các flags dùng như và vì:
--partial: Giữ lại phần file đã tải dở (thay vì xóa đi).
--append: Kiểm tra file ở đích và chỉ nối thêm dữ liệu vào cuối.
--append-verify: Nối thêm nhưng có kiểm tra lại mã băm để đảm bảo phần cũ không bị hỏng.
3. kịch bản tỉnh không có ip public: dùng -R
tỉnh sẽ chạy lệnh, dùng -R để mở cổng trên máy của trung tâm, thông qua đường hầm bảo mật ssh, trung tâm sẽ truy cập vào db của tỉnh qua cổng mới mở để lấy dữ liệu. ssh -R 9999:localhost:5432 user@42.1.1.1; tại đầu mỗi tỉnh sẽ thiết lập như trên
4. phòng chống MIMT: cơ chế được kích hoạt tự động 
sử dụng Host Key Verification và file ~/.ssh/known_hosts

ssh chống lại cơ chế này bằng cách xác nhận trước host key được mã hóa, file Known_hosts sẽ chứa các host key này để xác thực chính xác server muốn kết nối, nếu thấy lạ ko trùng khớp sẽ ngắt kết nối, file Known_host sẽ được đặt tại máy client và dùng để xác minh server, để từ client kết nối vào trung tâm thì sẽ biết chính xác server kết nối vào có an toàn hay không