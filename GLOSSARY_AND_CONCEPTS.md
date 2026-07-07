# 🧠 KHO TRI THỨC & TỪ ĐIỂN CHUYÊN NGÀNH (DATA SCIENCE MASTERY)

## 📂 MODULE 0: FOUNDATION & DATA ENGINEERING FUNDAMENTALS

### 1. Thuật ngữ Tiếng Anh (English for Data)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Ingestion** | /ɪnˈdʒes.tʃən/ (n) | Thu nhận/Nạp dữ liệu | Quá trình đưa dữ liệu thô từ nguồn vào hệ thống. |
| **Raw Data** | /rɔː ˈdeɪ.tə/ (n) | Dữ liệu thô | Dữ liệu nguyên bản, chưa qua xử lý hay chỉnh sửa. |
| **Pipeline** | /ˈpaɪp.laɪn/ (n) | Đường ống | Luồng di chuyển dữ liệu tự động qua các giai đoạn. |
| **Immutability** | /ɪˌmjuː.təˈbɪl.ə.ti/ (n) | Tính bất biến | Nguyên tắc dữ liệu đã ghi thì không được thay đổi. |
| **Scalability** | /ˌskeɪ.ləˈbɪl.ə.ti/ (n) | Khả năng mở rộng | Khả năng hệ thống chịu tải khi dữ liệu tăng lên. |
| **Audit Trail** | /ˈɔː.dɪt treɪl/ (n) | Vết tích kiểm toán | Lịch sử ghi lại mọi hành động thay đổi trên dữ liệu. |
| **Overwrite** | /ˌəʊ.vəˈraɪt/ (v) | Ghi đè | Hành động ghi đè dữ liệu mới lên dữ liệu cũ (Nguy hiểm!). |
| **Argument Maximum** |– đây là độ dài tối đa (tính bằng byte) của một chuỗi câu lệnh mà bạn được phép gõ vào.

### 2. Khái niệm cốt lõi (Core Concepts)
#### **Data Life Cycle Stages (Các giai đoạn chu kỳ dữ liệu)**
- **Raw (Landing):** Dữ liệu nguyên bản, dùng làm bằng chứng (Audit trail) và phục vụ tái xử lý (Re-run).
- **Processing (Staging):** Trạng thái trung gian, dữ liệu đang được làm sạch (Cleansing) và chuẩn hóa (Normalizing).
- **Archive (Long-term):** Lưu trữ dữ liệu lịch sử sau khi đã nạp vào kho chính thành công.
- **Error (Quarantine):** Cách ly các file hỏng, sai cấu trúc để không làm hỏng đường ống tự động.

#### **Naming Convention (Quy tắc đặt tên file)**
Một tên file chuẩn quốc gia phải đảm bảo: 
- **Uniqueness:** Không bao giờ trùng lặp (dùng Timestamp + ID).
- **Searchability:** Dễ dàng tìm kiếm bằng lệnh Linux (grep, find).
- **Security:** Không chứa thông tin quá nhạy cảm trực tiếp trên tên file.

#### **SSH Tunneling & Cơ chế mã hóa**
**Định nghĩa:** SSH Tunneling (Port Forwarding) là kỹ thuật sử dụng kết nối bảo mật SSH để tạo một "đường hầm", giúp truyền tải an toàn dữ liệu của các ứng dụng khác vượt qua firewall hoặc mạng không an toàn.

**Cơ chế mã hóa 3 lớp (3 Phases of Encryption):**
1. **Giai đoạn Bắt tay (Asymmetric Encryption - Mã hóa bất đối xứng):** 
   - Dùng để xác thực danh tính (tránh giả mạo) và thỏa thuận một **Session Key** (khóa phiên) bí mật dùng chung.
   - Quá trình này tính toán nặng, chỉ thực hiện một lần lúc đầu.
2. **Giai đoạn Truyền tải dữ liệu (Symmetric Encryption - Mã hóa đối xứng):**
   - Hai bên dùng chung **Session Key** vừa tạo ở bước 1 để vừa mã hóa vừa giải mã toàn bộ dữ liệu (Web, Database...) đi qua hầm.
   - Cực kỳ nhanh, nhẹ, đảm bảo tốc độ cao (ví dụ thuật toán AES).
3. **Giai đoạn Kiểm tra Toàn vẹn & Xác thực (Hashing / HMAC):**
   - Thay vì dùng chữ ký số nặng nề, SSH tận dụng lại **Session Key** trộn với dữ liệu và **Số thứ tự gói tin**, sau đó băm (Hashing) ra một mã MAC độc nhất cho từng gói tin.
   - Giúp phát hiện ngay lập tức nếu gói tin bị hacker sửa đổi hoặc giả mạo giữa đường.

---
*Kỷ luật ôn tập: Hãy dành 5 phút mỗi sáng để đọc lại bảng này trước khi bắt đầu bài tập mới.*
