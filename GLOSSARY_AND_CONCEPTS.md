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
| **ARG_MAX (Argument Maximum)** | /ɑːɡ mæks/ (n) | Giới hạn độ dài tham số lệnh | Giới hạn độ dài tối đa (bytes) của tham số dòng lệnh cho một lệnh thực thi (xargs, find, rm) trong Linux. |

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
| **Resource Negotiator** | /ˈriː.zɔːs nɪˈɡəʊ.ʃi.eɪ.tər/ (n) | Bộ điều phối tài nguyên | Hệ thống đứng ra thương lượng và cấp phát CPU/RAM giữa các ứng dụng. |
| **Multi-tenancy** | /ˈmʌl.ti ˈten.ən.si/ (n) | Kiến trúc đa người dùng / Đa tenant | Nhiều đội nhóm/ứng dụng (Spark, Flink, SQL) cùng chia sẻ và chạy chung trên 1 cluster. |
| **Resource Allocation** | /ˈriː.zɔːs ˌæl.əˈkeɪ.ʃən/ (n) | Cấp phát tài nguyên | Hành động RM và NM chia một lượng vCPU và RAM cụ thể cho Job. |
| **Starvation** | /stɑːˈveɪ.ʃən/ (n) | Hiện tượng "chết đói" | Tình trạng Job nhỏ bị nghẽn vô thời hạn do Job lớn chiếm hết tài nguyên (FIFO). |
| **Fair Scheduling** | /feər ˈskedʒ.uː.lɪŋ/ (n) | Điều phối công bằng | Thuật toán chia đều tài nguyên để mọi job đều có tài nguyên chạy song song. |
| **Preemption** | /priˈemp.ʃən/ (n) | Đoạt quyền / Thu hồi tài nguyên ưu tiên | YARN thu hồi bớt tài nguyên từ job có độ ưu tiên thấp hoặc vượt quota để cấp cho job ưu tiên cao hơn. |
| **Load Balancing** | /ˈləʊd ˌbæl.ən.sɪŋ/ (n) | Cân bằng tải | Rải đều công việc lên các node, tránh node làm không hết, node ngồi chơi. |
| **Throughput** | /ˈθruː.pʊt/ (n) | Băng thông / Khối lượng xử lý | Lượng dữ liệu hệ thống xử lý được trong 1 giây/1 phút (HDFS thiên về throughput). |
| **Latency** | /ˈleɪ.tən.si/ (n) | Độ trễ phản hồi | Thời gian từ lúc gửi yêu cầu đến khi có kết quả (OLTP cần low-latency). |

### 3. Thuật ngữ Tiếng Anh Apache Spark Internals (Compute Engine & Execution Plan)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Resilient Distributed Dataset (RDD)** | /rɪˈzɪl.jənt dɪˈstrɪb.juː.tɪd ˈdeɪ.tə.set/ (n) | Tập dữ liệu phân tán có khả năng phục hồi | Cấu trúc dữ liệu trừu tượng nền tảng của Spark, chia nhỏ trên RAM các node và tự hồi phục khi node sập. |
| **In-Memory Computing** | /ɪn ˈmem.ər.i kəmˈpjuː.tɪŋ/ (n) | Tính toán trên bộ nhớ RAM | Giữ dữ liệu trung gian trên RAM giữa các bước tính toán thay vì liên tục đọc/ghi ổ cứng như MapReduce. |
| **Lazy Evaluation** | /ˈleɪ.zi ɪˌvæl.juˈeɪ.ʃən/ (n) | Đánh giá lười biếng / Trì hoãn thực thi | Triết lý chỉ ghi nhận kế hoạch biến đổi (chưa tính toán ngay), đợi đến khi gặp Action mới kích hoạt cluster. |
| **Transformation** | /ˌtræns.fəˈmeɪ.ʃən/ (n) | Phép biến đổi dữ liệu | Lệnh tạo RDD mới từ RDD cũ (`map`, `filter`, `groupBy`). Không sinh ra dữ liệu ngay (Lazy). |
| **Action** | /ˈæk.ʃən/ (n) | Hành động kích hoạt thực thi | Lệnh kích hoạt Spark biên dịch DAG và chạy thật sự để trả kết quả về Driver hoặc ghi đĩa (`count`, `collect`, `save`). |
| **Directed Acyclic Graph (DAG)** | /daɪˈrek.tɪd eɪˈsaɪ.klɪk ɡrɑːf/ (n) | Đồ thị có hướng không chu trình | Bản vẽ lộ trình tính toán tối ưu mà DAG Scheduler vạch ra trước khi phân rã thành các Stage. |
| **Lineage Graph** | /ˈlɪn.i.ɪdʒ ɡrɑːf/ (n) | Đồ thị gia phả / Phả hệ dữ liệu | Chuỗi lịch sử các phép biến đổi đã tạo ra RDD. Khi 1 partition bị mất trong RAM, Spark dựa vào phả hệ để tính lại đúng partition đó. |
| **Narrow Dependency** | /ˈnær.əʊ dɪˈpen.dən.si/ (n) | Phụ thuộc hẹp | Mỗi partition của RDD cha chỉ dùng bởi 1 partition của RDD con (`map`, `filter`). Xử lý cục bộ tại máy, không tốn mạng. |
| **Wide Dependency** | /waɪd dɪˈpen.dən.si/ (n) | Phụ thuộc rộng | 1 partition cha phải chia cho nhiều partition con (`groupByKey`, `join`). Buộc phải kích hoạt Shuffling qua mạng. |
| **Shuffling** | /ˈʃʌf.lɪŋ/ (n) | Xáo trộn / Phân phối lại dữ liệu | Quá trình gom, băm nhỏ và truyền dữ liệu qua mạng giữa các node. Đây là nút thắt cổ chai đắt đỏ nhất về mạng và đĩa I/O. |
| **Stage** | /steɪdʒ/ (n) | Giai đoạn thực thi | Nhóm các Task có thể chạy song song (Narrow) mà không cần chuyển dữ liệu qua mạng. Các Stage bị ngăn cách bởi bước Shuffle. |
| **Task** | /tɑːsk/ (n) | Đơn vị tính toán nhỏ nhất | Đoạn mã thực thi trên 1 partition dữ liệu duy nhất, do 1 thread trong Executor đảm nhận. |
| **Driver Program** | /ˈdraɪ.vər ˈprəʊ.ɡræm/ (n) | Tiến trình điều khiển chính | Bộ não điều hành: Chứa `SparkSession`, phân tích code thành DAG, giao tiếp với YARN để xin Container và giám sát tiến độ. |
| **Executor** | /ɪɡˈzek.jə.tər/ (n) | Tiến trình công nhân | Chạy trong Container do YARN cấp trên Worker Node: Nhận Task từ Driver, giữ dữ liệu trong RAM và trực tiếp tính toán. |
| **Data Skew** | /ˈdeɪ.tə skjuː/ (n) | Lệch dữ liệu | Tình trạng dữ liệu phân bổ không đều sau Shuffling (1 partition gánh 80% dữ liệu), làm 1 Task chạy mãi không xong kéo chậm cả Job. |
| **Out Of Memory (OOM)** | /aʊt əv ˈmem.ər.i/ (n/adj) | Tràn bộ nhớ | Lỗi sập Executor hoặc Driver do không đủ RAM chứa dữ liệu (thường do `collect()` dữ liệu lớn về Driver hoặc join bị Data Skew). |
| **Data Locality** | /ˈdeɪ.tə ləʊˈkæl.ə.ti/ (n) | Tính cục bộ của dữ liệu | Nguyên tắc vàng: Đẩy code xử lý (vài KB) đến máy đang chứa dữ liệu thay vì kéo dữ liệu (vài GB) qua mạng về máy chạy code. |
| **Broadcast Hash Join (BHJ)** | /ˈbrɔːd.kɑːst hæʃ dʒɔɪn/ (n) | Nối băm phát tán | Thuật toán JOIN siêu tốc: Driver sao chép bảng nhỏ (<10MB) gửi tới mọi Executor, triệt tiêu 100% Shuffling qua mạng. |
| **Sort Merge Join (SMJ)** | /sɔːt mɜːdʒ dʒɔɪn/ (n) | Nối sắp xếp trộn | Thuật toán JOIN mặc định cho 2 bảng lớn: Shuffle theo key -> Sort từng partition -> Merge tuần tự bằng con trỏ chống OOM. |
| **Predicate Pushdown** | /ˈpred.ɪ.kət ˈpʊʃ.daʊn/ (n) | Đẩy điều kiện lọc xuống tầng lưu trữ | Kỹ thuật của Catalyst: Đẩy lệnh `filter()` xuống sát file Parquet để bỏ qua các block không cần đọc, tiết kiệm 90% I/O đĩa. |
| **Column Pruning** | /ˈkɒl.əm ˈpruː.nɪŋ/ (n) | Cắt tỉa cột thừa | Kỹ thuật chỉ đọc các cột cần thiết trong câu truy vấn từ file Parquet thay vì nạp toàn bộ các cột lên RAM. |
| **Spill to Disk** | /spɪl tuː dɪsk/ (v/n) | Tràn xuống ổ cứng | Thảm họa khi Execution Memory bị đầy, Spark buộc phải ghi dữ liệu Shuffle/Sort tạm xuống đĩa, làm tốc độ tụt 20-50 lần. |
| **Off-Heap Memory** | /ɒf hiːp ˈmem.ər.i/ (n) | Bộ nhớ ngoài JVM Heap | Vùng nhớ RAM do Project Tungsten tự quản lý trực tiếp (UnsafeRow) nhằm loại bỏ Java Object Overhead và xóa sổ lỗi đơ do GC. |
| **Garbage Collection (GC Pause)** | /ˈɡɑː.bɪdʒ kəˈlek.ʃən pɔːz/ (n) | Tạm dừng để thu gom rác | Thời điểm máy ảo Java JVM dừng toàn bộ chương trình để giải phóng object chết, gây trễ và nghẽn job Spark. |
| **Whole-Stage Code Generation** | /həʊl steɪdʒ kəʊd ˌdʒen.əˈreɪ.ʃən/ (n) | Sinh mã toàn giai đoạn | Tính năng của Tungsten: Biên dịch toàn bộ chuỗi tính toán thành 1 hàm bytecode Java duy nhất chạy trực tiếp trong CPU Cache. |
| **Salting** | /ˈsɒl.tɪŋ/ (n) | Kỹ thuật thêm tiền tố ngẫu nhiên vào khóa (Salting key) | Kỹ thuật diệt Data Skew: Ghép thêm tiền tố/hậu tố ngẫu nhiên vào key bị lệch để chia nhỏ 1 partition khổng lồ ra nhiều partition con. |
| **Adaptive Query Execution (AQE)** | /əˈdæp.tɪv ˈkwɪə.ri ˌek.sɪˈkjuː.ʃən/ (n) | Tối ưu hóa truy vấn thích ứng | Cơ chế thông minh từ Spark 3.x: Tự động đo đạc dữ liệu lúc đang chạy để tự đổi Join, tự gộp partition nhỏ và tự chữa Data Skew. |

### 4. Thuật ngữ Tiếng Anh Modern Storage Layer: Delta Lake & Apache Iceberg (Lakehouse Architecture)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Lakehouse Architecture** | /ˈleɪk.haʊs ˈɑː.kɪ.tek.tʃər/ (n) | Kiến trúc Lakehouse | Kiến trúc lai ghép: Lưu trữ rẻ trên Cloud Object Storage (Data Lake) kết hợp quản trị ACID và hiệu năng cao (Data Warehouse). |
| **ACID Transactions** | /ˈæs.ɪd trænˈzæk.ʃənz/ (n) | Giao dịch chuẩn ACID | 4 thuộc tính vàng: Atomicity (Nguyên tử), Consistency (Nhất quán), Isolation (Cô lập), Durability (Bền vững) đưa lên Data Lake. |
| **Transaction Log** | trænˈzæk.ʃən lɒɡ/ (n) | Nhật ký giao dịch | Thư mục `_delta_log` hoặc metadata tree ghi lại tuần tự từng commit (file nào thêm, file nào xóa). Quyết định "chân lý" của bảng. |
| **Optimistic Concurrency Control (OCC)** | /ˌɒp.tɪˈmɪs.tɪk kənˈkʌr.ən.si kənˈtrəʊl/ (n) | Kiểm soát tương tranh lạc quan | Cơ chế cho phép nhiều job cùng ghi dữ liệu, chỉ kiểm tra xung đột lúc commit; nếu trùng file thì retry an toàn. |
| **Time Travel** | /ˈtaɪm ˌtræv.əl/ (n) | Quay ngược thời gian | Khả năng truy vấn, đối soát hoặc rollback dữ liệu về một version hoặc timestamp trong quá khứ (`VERSION AS OF` / `TIMESTAMP AS OF`). |
| **Snapshot Isolation** | /ˈsnæp.ʃɒt ˌaɪ.səˈleɪ.ʃən/ (n) | Cô lập ảnh chụp | Cơ chế đảm bảo người đọc (reader) luôn nhìn thấy bản dữ liệu nhất quán tại thời điểm bắt đầu query, không bị ảnh hưởng bởi writer. |
| **Copy-on-Write (CoW)** | /ˈkɒp.i ɒn raɪt/ (n/adj) | Sao chép khi ghi | Khi UPDATE/DELETE, đọc file Parquet cũ, sửa dòng cần sửa và ghi ra file Parquet mới hoàn toàn, rồi cập nhật metadata tráo đổi file. |
| **Merge-on-Read (MoR)** | /mɜːdʒ ɒn riːd/ (n/adj) | Hợp nhất khi đọc | Khi UPDATE/DELETE, chỉ ghi dòng thay đổi vào file delta riêng biệt; khi reader đọc mới gộp lại. Tối ưu cho ghi nhanh real-time. |
| **Compaction (`OPTIMIZE`)** | /kəmˈpæk.ʃən/ (n) | Gom nén dữ liệu | Lệnh gộp hàng nghìn file Parquet nhỏ (vài KB-MB) thành các file lớn chuẩn (~128MB - 1GB) để giải quyết dứt điểm Small Files Problem. |
| **Z-Ordering** | /zed ˈɔː.dər.ɪŋ/ (n) | Sắp xếp đường cong chữ Z | Kỹ thuật gom cụm dữ liệu đa chiều (Multi-dimensional Clustering) trên nhiều cột, giúp tăng tối đa số file bị bỏ qua khi tìm kiếm. |
| **Data Skipping** | /ˈdeɪ.tə ˈskɪp.ɪŋ/ (n) | Bỏ qua dữ liệu | Cơ chế dùng thống kê Min/Max trong metadata để không đọc 80-95% các file Parquet không chứa dữ liệu cần tìm. |
| **Schema Enforcement** | /ˈskiː.mə ɪnˈfɔːs.mənt/ (n) | Bắt buộc đúng cấu trúc | Cơ chế tự động chặn đứng (ném lỗi) nếu dữ liệu ghi vào không khớp với cấu trúc cột/kiểu dữ liệu đã khai báo của bảng. |
| **Schema Evolution** | /ˈskiː.mə ˌev.əˈluː.ʃən/ (n) | Tiến hóa cấu trúc | Khả năng tự động và an toàn bổ sung các cột mới vào bảng (`mergeSchema = true`) mà không làm hỏng dữ liệu cũ. |
| **VACUUM** | /ˈvæk.juːm/ (v/n) | Dọn dẹp tệp mồ côi | Lệnh xóa vĩnh viễn các file Parquet vật lý đã bị remove khỏi transaction log vượt quá thời gian lưu giữ (retention period). |

---

## 📂 MODULE 3: REAL-TIME STREAMING & INTEGRATION

### 1. Thuật ngữ Tiếng Anh Apache Kafka (Core Architecture & Distributed Pub/Sub)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Real-time Streaming** | /ˈrɪəl.taɪm ˈstriː.mɪŋ/ (n) | Luồng dữ liệu thời gian thực | Xử lý dữ liệu liên tục theo từng sự kiện (Event-by-Event) với độ trễ mili-giây, đối lập với Batch Processing theo lô. |
| **Streaming Ingestion** | /ˈstriː.mɪŋ ɪnˈdʒes.tʃən/ (n) | Thu nhận luồng dữ liệu | Quá trình tiếp nhận và đệm hàng triệu sự kiện/giây từ các nguồn phân tán (IoT, ứng dụng web, ngân hàng) vào hệ thống. |
| **Publish/Subscribe (Pub/Sub)** | /ˈpʌb.lɪʃ səbˈskraɪb/ (n) | Mô hình xuất bản / Đăng ký | Mô hình truyền thông phân tán: Bên phát tin (Producer) và bên nhận tin (Consumer) hoàn toàn không biết nhau, chỉ giao tiếp qua Topic. |
| **Decoupling** | /diːˈkʌp.lɪŋ/ (n) | Tách rời phụ thuộc | Tách các hệ sinh thái dịch vụ ra khỏi nhau: Producer cứ việc gửi tin, Consumer chết hoặc chậm cũng không làm treo Producer. |
| **Backpressure** | /ˈbækˌpreʃ.ər/ (n) | Áp lực dội ngược | Cơ chế bảo vệ hệ thống: Kafka đóng vai trò là "hồ chứa đệm", cho phép Consumer đọc dữ liệu theo tốc độ mà nó có thể chịu đựng, không bị sập vì quá tải. |
| **Topic** | /ˈtɒp.ɪk/ (n) | Chủ đề / Kênh dữ liệu | Danh mục logic chứa các sự kiện cùng loại (vd: `giao_dich_the`, `xac_thuc_cccd`). |
| **Partition** | /pɑːˈtɪʃ.ən/ (n) | Phân vùng vật lý | Đơn vị lưu trữ và phân tán nhỏ nhất của Topic. Mỗi Partition là một tệp log ghi tuần tự (Append-only) trên đĩa của Broker. |
| **Offset** | /ˈɒf.set/ (n) | Chỉ số vị trí bản tin | Số nguyên tuần tự tăng dần gán cho mỗi message trong 1 Partition, xác định vị trí chính xác của bản tin đó. |
| **Producer** | /prəˈdʒuː.sər/ (n) | Bên phát tin | Ứng dụng xuất bản (ghi) bản tin vào các Topic trong cụm Kafka. |
| **Consumer** | /kənˈsjuː.mər/ (n) | Bên tiêu thụ tin | Ứng dụng đọc và xử lý bản tin từ các Topic trong Kafka. |
| **Consumer Group** | /kənˈsjuː.mər ɡruːp/ (n) | Nhóm tiêu thụ | Tập hợp các Consumer cùng chia nhau đọc các Partition của 1 Topic để xử lý song song và cân bằng tải. |
| **Rebalancing** | /ˌriːˈbæl.əns.ɪŋ/ (n) | Tái cân bằng phân vùng | Quá trình Kafka phân bổ lại quyền đọc các Partition giữa các Consumer trong nhóm khi có Consumer mới gia nhập hoặc bị sập (Crash). |
| **Broker** | /ˈbrəʊ.kər/ (n) | Máy chủ trung chuyển tin | Một server vật lý hoặc máy ảo chạy tiến trình Kafka, chịu trách nhiệm nhận, lưu trữ và chuyển giao bản tin. |
| **Cluster** | /ˈklʌs.tər/ (n) | Cụm máy chủ phân tán | Tập hợp nhiều Broker phối hợp với nhau để đảm bảo khả năng mở rộng (Scale-out) và tính sẵn sàng cao (High Availability). |
| **Replication Factor** | /ˌrep.lɪˈkeɪ.ʃən ˈfæk.tər/ (n) | Hệ số bản sao | Số lượng bản sao chép lưu trữ của mỗi Partition trên các Broker khác nhau để chống mất dữ liệu (thường đặt = 3). |
| **Leader Replica** | /ˈliː.dər ˈrep.lɪ.kə/ (n) | Bản sao chủ | Phân vùng đại diện chịu trách nhiệm xử lý 100% yêu cầu Đọc và Ghi từ Client (Producer/Consumer). |
| **Follower Replica** | /ˈfɒl.əʊ.ər ˈrep.lɪ.kə/ (n) | Bản sao tớ | Phân vùng dự phòng ngầm sao chép dữ liệu tuần tự từ Leader; không nhận ghi trực tiếp từ Client, sẵn sàng lên thay khi Leader chết. |
| **In-Sync Replicas (ISR)** | /ɪn sɪŋk ˈrep.lɪ.kəz/ (n) | Danh sách bản sao đồng bộ | Tập hợp các bản sao (Leader + Followers) đang bám sát dữ liệu mới nhất của Leader mà không bị trễ mạng quá ngưỡng cho phép. |
| **Acks (Acknowledgements)** | /əkˈnɒl.ɪdʒ.mənts/ (n) | Xác nhận ghi thành công | Cấu hình Producer chọn mức độ an toàn khi gửi tin: `0` (không cần phản hồi), `1` (Leader đã ghi), `all`/-1 (toàn bộ ISR đã ghi). |
| **Consumer Lag** | /kənˈsjuː.mər læɡ/ (n) | Độ trễ tiêu thụ | Khoảng cách giữa Offset mới nhất được ghi vào Partition và Offset hiện tại Consumer đang xử lý. Lag tăng cao là dấu hiệu hệ thống hạ nguồn bị nghẽn. |
| **Poison Pill** | /ˈpɔɪ.zən pɪl/ (n) | Bản tin "thuốc độc" | Một message bị lỗi định dạng (Corrupted/Malformed) khiến Consumer đọc vào bị crash liên tục, không thể commit offset và chặn đứng cả luồng xử lý. |
| **Dead Letter Queue (DLQ)** | /ded ˈlet.ər kjuː/ (n) | Hàng đợi thư chết | Topic riêng biệt dùng để cô lập các bản tin bị lỗi (như Poison Pill) để đội kỹ sư kiểm tra sau, tránh làm tắc nghẽn đường ống chính. |
| **Idempotent Producer** | /aɪˈdem.pə.tənt prəˈdʒuː.sər/ (n) | Cơ chế phát tin chống trùng lặp (Tính lũy đẳng) | Tính năng tự động gán Producer ID + Sequence Number cho từng tin nhắn, đảm bảo dù Producer có retry do mạng chập chờn thì Kafka cũng không bao giờ lưu trùng tin. |
| **Log Compaction** | /lɒɡ kəmˈpæk.ʃən/ (n) | Nén nhật ký theo khóa | Cơ chế dọn dẹp topic: Chỉ giữ lại bản tin có giá trị MỚI NHẤT cho mỗi Key, xóa bỏ các bản ghi cũ của Key đó (rất phổ biến khi lưu trạng thái thực thể). |
| **KRaft (Kafka Raft)** | /kræft/ (n) | Giao thức đồng thuận KRaft | Cơ chế quản trị Metadata tích hợp sẵn trong Kafka từ bản 3.x, thay thế hoàn toàn ZooKeeper, giúp mở rộng hàng triệu Partition mà không bị nghẽn. |

### 2. Thuật ngữ Tiếng Anh CDC & Tích Hợp Hệ Thống (Change Data Capture & Debezium)
| Thuật ngữ | Phiên âm / Loại từ | Ý nghĩa chuyên ngành | Ngữ cảnh sử dụng |
| :--- | :--- | :--- | :--- |
| **Change Data Capture (CDC)** | /tʃeɪndʒ ˈdeɪ.tə ˈkæp.tʃər/ (n) | Bắt vết thay đổi dữ liệu | Kỹ thuật theo dõi và ghi lại mọi thay đổi (INSERT, UPDATE, DELETE) trên Database nguồn theo thời gian thực mà không làm chậm DB. |
| **Write-Ahead Log (WAL) / Binlog** | /raɪt əˈhed lɒɡ/ (n) | Nhật ký ghi trước | Tệp nhật ký nhị phân của Database (PostgreSQL gọi là WAL, MySQL gọi là Binlog). CDC đọc trực tiếp từ log này thay vì chạy lệnh `SELECT`. |
| **Logical Decoding** | /ˈlɒdʒ.ɪ.kəl diːˈkəʊ.dɪŋ/ (n) | Giải mã logic | Cơ chế nội tại của PostgreSQL cho phép trích xuất các thao tác DML từ WAL thành cấu trúc dữ liệu logic (dòng/cột) dễ đọc thay vì raw bytes. |
| **Logical Replication Plugin** | /ˈlɒdʒ.ɪ.kəl ˌrep.lɪˈkeɪ.ʃən ˈplʌɡ.ɪn/ (n) | Plugin sao chép logic | Plugin thực thi giải mã log trong PostgreSQL (vd: `pgoutput` mặc định của Postgres 10+, hoặc `decoderbufs`). |
| **Replication Slot** | /ˌrep.lɪˈkeɪ.ʃən slɒt/ (n) | Khe sao chép | Cơ chế của PostgreSQL giữ con trỏ `restart_lsn` để bảo đảm WAL không bị xóa chừng nào consumer chưa xác nhận đã đọc xong. |
| **Log Sequence Number (LSN)** | /lɒɡ ˈsiː.kwəns ˈnʌm.bər/ (n) | Số thứ tự nhật ký | Mã định danh 64-bit chỉ vị trí byte chính xác của bản ghi trong chuỗi file WAL của PostgreSQL. |
| **WAL Bloat** | /wɔːl bləʊt/ (n) | Phình to nhật ký WAL | Hiện tượng đĩa máy chủ PostgreSQL bị đầy 100% do Replication Slot giữ chân các file WAL không cho giải phóng khi consumer sập. |
| **Replica Identity** | /ˈrep.lɪ.kə aɪˈden.tə.ti/ (n) | Danh tính bản sao | Cấu hình bảng trong PostgreSQL quy định thông tin nào của dòng CŨ (old tuple) được ghi vào WAL khi `UPDATE`/`DELETE` (`DEFAULT`, `FULL`, `NOTHING`, `INDEX`). |
| **Write Amplification** | /raɪt ˌæm.plɪ.fɪˈkeɪ.ʃən/ (n) | Hiện tượng khuếch đại ghi (Khuếch đại ghi đĩa) | Hiện tượng một thao tác sửa nhỏ (1 cột) khiến dung lượng ghi log tăng vọt gấp nhiều lần (khi bật `REPLICA IDENTITY FULL`). |
| **Tombstone Message** | /ˈtuːm.stəʊn ˈmes.ɪdʒ/ (n) | Bản tin bia mộ | Bản tin đặc biệt trong Kafka có `Key = ID` và `Value = null`, dùng để báo cho Kafka **Log Compaction** dọn dẹp vĩnh viễn Key này khỏi đĩa. |
| **Query-based Polling** | /ˈkwɪə.ri beɪst ˈpəʊ.lɪŋ/ (n) | Quét định kỳ bằng SQL | Cách làm thô sơ: Chạy định kỳ `SELECT * WHERE updated_at > last_time`. Gây lock contention, trễ dữ liệu và mù trước Hard Delete. |
| **Lock Contention** | /lɒk kənˈten.ʃən/ (n) | Tranh chấp khóa | Hiện tượng các lệnh SELECT lớn chiếm giữ Shared Lock làm nghẽn các câu lệnh INSERT/UPDATE của người dùng OLTP. |
| **Kafka Connect** | /ˈkæf.kə kəˈnekt/ (n) | Khung kết nối Kafka | Công cụ phân tán của hệ sinh thái Kafka giúp kéo dữ liệu từ DB vào Kafka (Source Connector) hoặc đẩy từ Kafka ra Lakehouse/ES (Sink Connector) mà không cần viết code. |
| **Schema Registry** | /ˈskiː.mə ˈredʒ.ɪ.stri/ (n) | Sổ đăng ký cấu trúc dữ liệu | Máy chủ trung tâm lưu trữ và kiểm soát tính tương thích của Schema (Avro/Protobuf) giữa Producer và Consumer, ngăn chặn dữ liệu bẩn làm sập hệ thống. |
| **Outbox Pattern** | /ˈaʊt.bɒks ˈpæt.ən/ (n) | Mẫu thiết kế Outbox | Kỹ thuật bảo đảm tính nhất quán: Ứng dụng ghi sự kiện vào bảng `outbox` trong cùng 1 transaction DB, sau đó Debezium bắt log từ bảng này đẩy vào Kafka. |
| **Dead Letter Queue (DLQ)** | /ded ˈlet.ər kjuː/ (n) | Hàng đợi thư chết | Topic Kafka lưu trữ các tin nhắn lỗi/hỏng cấu trúc không thể parse được, giúp pipeline không bị sập toàn bộ. |
| **Intermediate State** | /ˌɪn.təˈmiː.di.ət steɪt/ (n) | Trạng thái trung gian | Các bước nhảy trạng thái diễn ra giữa 2 chu kỳ quét (ví dụ: A -> B -> C). CDC bắt trọn được, Polling thì bỏ lỡ hoàn toàn. |
| **Snapshot Phase** | /ˈsnæp.ʃɒt feɪz/ (n) | Giai đoạn chụp ảnh ban đầu | Giai đoạn Debezium đọc quét toàn bộ dữ liệu hiện có trong bảng lúc ban đầu trước khi chuyển sang Streaming Phase (đọc WAL liên tục). |

---
*Kỷ luật ôn tập: Dành 5 phút mỗi ngày đọc to phát âm và giải thích nghĩa để biến từ vựng chuyên ngành thành phản xạ tự nhiên.*



