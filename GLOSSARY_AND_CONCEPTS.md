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

## 📂 MODULE 1: DATA WAREHOUSING & SQL MASTERY

### 1. Thuật ngữ Tiếng Anh (English for Data Modeling)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Fact** | /fækt/ (n) | Sự kiện / Giao dịch | Dữ liệu định lượng (tiền, số lượng) và bất biến. Chứa trong Fact Table. |
| **Dimension** | /daɪˈmen.ʃən/ (n) | Ngữ cảnh / Chiều | Thông tin miêu tả (ai, ở đâu, khi nào). Dùng để cắt lớp, phân tích Fact. |
| **Normalize** | /ˈnɔː.mə.laɪz/ (v) | Chuẩn hóa | Quá trình chia nhỏ bảng để loại bỏ sự lặp lại dữ liệu (Snowflake dùng cách này). |
| **Denormalize** | /diːˈnɔː.mə.laɪz/ (v) | Phi chuẩn hóa | Cố tình gộp bảng, chấp nhận lặp dữ liệu để giảm lệnh JOIN, tăng tốc query (Star dùng cách này). |
| **Surrogate Key** | /ˈsʌr.ə.ɡət kiː/ (n) | Khóa thay thế | Khóa chính tự sinh (1,2,3...) của DWH, độc lập với hệ thống gốc, dùng để quản lý lịch sử. |
| **Slowly Changing Dimension (SCD)** | /.../ (n) | Chiều thay đổi chậm | Kỹ thuật quản lý sự thay đổi của bảng Dimension theo thời gian (VD: đổi địa chỉ). |

---

## 📂 MODULE 2: DISTRIBUTED SYSTEMS & BIG DATA

### 1. Thuật ngữ Tiếng Anh HDFS (Distributed Storage)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Distributed Storage** | /dɪˈstrɪb.juː.tɪd ˈstɔː.rɪdʒ/ (n) | Lưu trữ phân tán | Lưu một file lớn trên nhiều máy tính khác nhau thay vì 1 ổ cứng đơn. |
| **Metadata** | /ˈmet.əˌdeɪ.tə/ (n) | Siêu dữ liệu | Dữ liệu mô tả dữ liệu (tên file, quyền, ánh xạ file → block → DataNode). |
| **Replication Factor** | /ˌrep.lɪˈkeɪ.ʃən ˈfæk.tər/ (n) | Hệ số nhân bản | Số lượng bản sao lưu của mỗi block (mặc định là 3). |
| **Fault Tolerance** | /ˈfɒlt ˌtɒl.ər.əns/ (n) | Khả năng chịu lỗi | Hệ thống vẫn chạy bình thường khi có máy bay màu/hỏng hóc phần cứng. |
| **Single Point of Failure (SPOF)** | /ˌsɪŋ.ɡəl pɔɪnt əv ˈfeɪ.ljər/ (n) | Điểm hỏng duy nhất | Thành phần nếu chết thì kéo sập cả hệ thống (như NameNode đơn lẻ). |
| **Heartbeat** | /ˈhɑːt.biːt/ (n) | Tín hiệu nhịp tim | Bản tin định kỳ (3s) DataNode gửi NameNode để báo "tôi vẫn còn sống". |
| **Self-healing** | /ˌselfˈhiː.lɪŋ/ (adj/n) | Tự phục hồi / Tự chữa lành | Khả năng tự động nhân bản lại các block bị thiếu khi 1 node chết. |
| **Small Files Problem** | /smɔːl faɪlz ˈprɒb.ləm/ (n) | Vấn nạn file nhỏ | Quá nhiều file nhỏ gây cạn kiệt RAM NameNode dù đĩa cứng còn trống. |
| **Compaction** | /kəmˈpæk.ʃən/ (n) | Gom nén file | Kỹ thuật gộp hàng nghìn file nhỏ thành file lớn (128MB-512MB) để cứu RAM. |
| **Commodity Hardware** | /kəˈmɒd.ə.ti ˈhɑːd.weər/ (n) | Phần cứng phổ thông | Các máy tính tiêu chuẩn giá rẻ được dùng để ghép thành cluster (Scale-out). |

### 2. Thuật ngữ Tiếng Anh YARN (Resource Management)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Resource Negotiator** | /ˈriː.zɔːs nɪˈɡəʊ.ʃi.eɪ.tər/ (n) | Người điều phối tài nguyên | Hệ thống đứng ra thương lượng và cấp phát CPU/RAM giữa các ứng dụng. |
| **Multi-tenancy** | /ˈmʌl.ti ˈten.ən.si/ (n) | Đa người thuê / Dùng chung | Nhiều đội nhóm/ứng dụng (Spark, Flink, SQL) cùng chạy trên 1 cluster. |
| **Resource Allocation** | /ˈriː.zɔːs ˌæl.əˈkeɪ.ʃən/ (n) | Cấp phát tài nguyên | Hành động RM và NM chia một lượng vCPU và RAM cụ thể cho Job. |
| **Starvation** | /stɑːˈveɪ.ʃən/ (n) | Hiện tượng "chết đói" | Tình trạng Job nhỏ bị nghẽn vô thời hạn do Job lớn chiếm hết tài nguyên (FIFO). |
| **Fair Scheduling** | /feər ˈskedʒ.uː.lɪŋ/ (n) | Điều phối công bằng | Thuật toán chia đều tài nguyên để mọi job đều có tài nguyên chạy song song. |
| **Preemption** | /priˈemp.ʃən/ (n) | Thu hồi cưỡng chế | YARN tịch thu bớt tài nguyên từ job thừa để cứu job đang thiếu. |
| **Load Balancing** | /ˈləʊd ˌbæl.ən.sɪŋ/ (n) | Cân bằng tải | Rải đều công việc lên các node, tránh node làm không hết, node ngồi chơi. |
| **Throughput** | /ˈθruː.pʊt/ (n) | Băng thông / Khối lượng xử lý | Lượng dữ liệu hệ thống xử lý được trong 1 giây/1 phút (HDFS thiên về throughput). |
| **Latency** | /ˈleɪ.tən.si/ (n) | Độ trễ phản hồi | Thời gian từ lúc gửi yêu cầu đến khi có kết quả (OLTP cần low-latency). |

---
*Kỷ luật ôn tập: Dành 5 phút mỗi ngày đọc to phát âm và giải thích nghĩa để biến từ vựng chuyên ngành thành phản xạ tự nhiên.*
