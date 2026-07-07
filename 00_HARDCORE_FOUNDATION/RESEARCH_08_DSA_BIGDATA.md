# 🛡️ KIẾN TRÚC & TỐI ƯU: TASK 08 (DSA & DISK I/O FOR BIG DATA)

> **Quân luật:** Giải thích theo tư duy "Quản lý dòng chảy". Không Copy-paste lý thuyết. Dùng ví dụ thực tế của một máy chủ thực thụ có 8GB RAM nhưng phải xử lý 800GB dữ liệu.

---

**Trả lời (Phương pháp Feynman - Quản lý Dòng chảy):**
*   **Hiện tượng xảy ra (OOM/MemoryError):**
    *   Khi máy chủ chỉ có 8GB RAM mà ta nạp file 20GB vào list `data = []`, Python sẽ cố gắng cấp phát bộ nhớ cho toàn bộ 20GB dữ liệu thô này cùng lúc dưới dạng các Python Object (chiếm dung lượng thực tế gấp 3-4 lần dung lượng file do overhead cấu trúc dữ liệu của Python). 
    *   Hệ điều hành sẽ cạn kiệt RAM và phân vùng Swap. Cơ chế **OOM Killer (Out Of Memory Killer)** của Linux sẽ lập tức can thiệp và "tiêu diệt" (kill) tiến trình Python để bảo vệ hệ thống không bị treo. Python sẽ báo lỗi `MemoryError` hoặc đột ngột bị đóng với mã lỗi `Killed`.
*   **Giải pháp sử dụng Generator (`yield`):**
    *   *Ẩn dụ chiếc bàn ăn:* Hãy tưởng tượng RAM của bạn là một chiếc bàn ăn nhỏ (8GB), và tệp dữ liệu là một chiếc bánh kem khổng lồ nặng 20GB. Nếu bạn cố bê cả chiếc bánh đặt lên bàn, bàn sẽ gãy (`MemoryError`). 
    *   Thay vì thế, ta cắt bánh thành từng lát nhỏ (từng dòng/dòng dữ liệu) và mang từng lát ra bàn. Khách ăn xong lát nào (xử lý xong dòng đó), ta dọn đĩa (giải phóng RAM) rồi mới mang lát tiếp theo ra. Bàn ăn sẽ không bao giờ bị quá tải.
    *   Trong Python, thay vì dùng `return data` để trả về cả list, ta dùng **`yield row`**. Hàm chứa `yield` trở thành một **Generator Iterator**. Khi vòng lặp gọi tới dòng tiếp theo, Generator mới đọc dòng tiếp theo từ đĩa vào RAM và tự động giải phóng dòng cũ. RAM tiêu thụ sẽ duy trì ở mức siêu nhỏ (vài Kilobytes đến Megabytes) cho dù file có nặng hàng Terabytes!



## 2. Nghệ thuật của "Sự trì hoãn" (Buffering & Batching)
**Câu hỏi:** Giả sử script của cậu tìm thấy 1 triệu dòng lỗi. Việc mở file `error_rows.log` rồi ghi từng dòng một (`ef.write`) trong vòng lặp có hại gì cho ổ cứng (HDD/SSD)?
- Tại sao việc ghi 1 file lớn hàng triệu dòng một lần (Batch) lại nhanh hơn ghi 1 triệu lần mỗi lần 1 dòng?
- Em hãy đề xuất cách gom dữ liệu lỗi vào một `Buffer` (danh sách tạm) rồi chỉ ghi xuống ổ cứng khi danh sách đó đạt 10.000 dòng.

**Trả lời (Phương pháp Feynman - Nghệ thuật trì hoãn):**
*   **Tác hại của việc ghi từng dòng (Row-by-Row Write):**
    *   Mỗi khi gọi `ef.write()`, Python phải gửi một lệnh gọi hệ thống (**System Call - `write`**) yêu cầu hệ điều hành chuyển đổi ngữ cảnh (Context Switch) từ User Space sang Kernel Space để ghi dữ liệu xuống đĩa vật lý. 1 triệu dòng tương đương với 1 triệu System Calls và 1 triệu lần kích hoạt Disk I/O.
    *   **Với HDD:** Đầu đọc phải di chuyển vật lý liên tục (Random Write), gây tiếng ồn lớn và tốc độ chậm kinh hoàng do độ trễ cơ học.
    *   **Với SSD:** Mỗi lần ghi dù chỉ 1 ký tự, SSD vẫn phải xóa và ghi lại cả một phân vùng vật lý (Page/Block) do cơ chế **Write Amplification**. Ghi liên tục từng dòng sẽ nhanh chóng làm hao mòn tuổi thọ SSD (TBW - Terabytes Written) của máy chủ.
*   **Tại sao ghi hàng loạt (Batch Write) lại nhanh hơn?**
    *   *Ẩn dụ xe chở gạch:* Bạn cần chuyển 1 triệu viên gạch (dòng lỗi) về công trường. Nếu bạn tự đi xe máy chở từng viên một, bạn sẽ hỏng xe, tốn xăng và mất 100 năm. Thay vì thế, bạn xếp 10.000 viên lên một chiếc xe tải (Buffer) rồi chở đi một chuyến. Bạn chỉ cần đi 100 chuyến xe tải thay vì 1 triệu chuyến xe máy!
*   **Đề xuất cơ chế Buffer (Batching) trong Python:**
    *   Ta khởi tạo một list rỗng làm bộ đệm: `error_buffer = []`.
    *   Mỗi khi phát hiện dòng lỗi, thay vì ghi trực tiếp xuống file, ta thêm vào bộ đệm: `error_buffer.append(error_msg)`.
    *   Khi bộ đệm đạt kích thước mong muốn (ví dụ 10.000 dòng):
        ```python
        if len(error_buffer) >= 10000:
            with open(ERROR_FILE, mode='a', encoding='utf-8') as ef:
                ef.writelines(error_buffer)
            error_buffer.clear()  # Xóa sạch bộ đệm để nhận đợt mới
        ```
    *   *Lưu ý quan trọng:* Ở cuối pipeline, ta cần chạy một lệnh "dọn kho" (Flush) để ghi nốt số lượng dòng thừa còn lại trong buffer (ví dụ 3.500 dòng cuối cùng chưa đủ 10.000).



## 3. Row vs Column (Lưu trữ hàng tỷ bản ghi)
**Câu hỏi:** Dữ liệu quốc gia (như Bảo hiểm, Thuế) thường có hàng trăm cột, nhưng mỗi lần truy vấn chúng ta chỉ cần lấy 2-3 cột (VD: Họ tên, Số tiền).
- Nếu lưu bằng CSV (Theo hàng), máy tính phải đọc hết cả hàng (tất cả các cột) để tìm thấy cái mình cần. Điều này lãng phí bao nhiêu tài nguyên?
- Tìm hiểu về **Apache Parquet**. Tại sao lưu trữ theo Cột (Columnar) lại giúp việc truy vấn nhanh gấp 10-100 lần so với CSV?

**Trả lời (Phương pháp Feynman - Row vs Column):**
*   **Sự lãng phí tài nguyên của CSV (Row-oriented):**
    *   CSV lưu dữ liệu tuần tự theo dòng: `Dòng 1 (Cột A, Cột B, Cột C...) \n Dòng 2...`. Nếu file có 100 cột và nặng 100GB, khi bạn chỉ muốn lấy 2 cột (Họ tên và Số tiền), ổ đĩa vẫn phải quay và đọc qua toàn bộ 100GB dữ liệu (gồm cả địa chỉ, email, số điện thoại...) để trích xuất ra 2 cột cần thiết. Điều này gây lãng phí khủng khiếp về Disk I/O, thời gian đọc đĩa vật lý (Disk Seek Time) và nghẽn băng thông RAM/CPU.
*   **Tại sao định dạng Columnar (Parquet) lại nhanh vượt trội?**
    *   *Ẩn dụ cuốn sổ danh bạ:* CSV giống như việc viết tiểu sử của mỗi người vào một cuốn sách riêng. Muốn tìm tên của 1 triệu người, bạn phải giở từng cuốn sách và đọc qua toàn bộ cuộc đời của họ. Parquet giống như việc lập riêng một tờ giấy chỉ ghi tên, một tờ giấy chỉ ghi số điện thoại. Muốn tìm tên, bạn chỉ cần đọc đúng tờ giấy ghi tên.
    *   **Các tính năng ưu việt của Parquet:**
        1.  **Projection Pushdown (Trích xuất chọn lọc):** Hệ thống chỉ đọc đúng các byte dữ liệu của các cột được yêu cầu trên ổ đĩa, hoàn toàn bỏ qua các cột khác. Tiết kiệm 95%+ Disk I/O.
        2.  **Predicate Pushdown (Bộ lọc tại chỗ):** Parquet lưu trữ metadata (Min/Max, Null count) cho từng khối dữ liệu (Row Group). Nếu bạn tìm số tiền > 1 triệu, hệ thống sẽ đọc metadata trước và bỏ qua toàn bộ các Row Group không chứa giá trị phù hợp mà không cần quét dữ liệu thực tế.
        3.  **Tỷ lệ nén siêu cao:** Vì dữ liệu trong cùng một cột có cùng kiểu dữ liệu (ví dụ toàn là số tiền float hoặc toàn là ngày tháng), Parquet có thể nén bằng các thuật toán cực mạnh (Snappy, Gzip, Run-Length Encoding). Kích thước file Parquet thường chỉ bằng 10% - 20% so với CSV ban đầu, giảm tối đa dung lượng lưu trữ của kho dữ liệu.


---
*(Khi nộp bài, báo "Tôi đã sẵn sàng tối ưu hệ thống Task 08".)*
Giai đoạn 1 (Ingestion): Làm sao để kéo dữ liệu từ 63 tỉnh về mà không sợ hacker hay đứt mạng? (Dùng từ khóa Task 5).
- xây dựng đường hầm bảo mật ssh, hacker có tấn công MIMT cũng không thể giải mã, tấn công được hệ thống; dùng rsync để tránh việc đứt mạng hoặc tắt nguồn đột ngột, việc truyền dữ liệu sẽ được tiếp tục bằng cơ chế checksum
Giai đoạn 2 (Automation): Làm sao để hệ thống tự vận hành lúc 2h sáng mà không cần mình thức dậy? (Dùng từ khóa Task 6).
- hệ thống sẽ sử dụng crontab với cronjob 
2 h sáng hàng ngày: 0 2 * * * <lênh thực thi>
Giai đoạn 3 (Refining): Dữ liệu thô về rồi, làm sao để biến nó thành "Vàng" sạch sẽ cho kho dữ liệu quốc gia? (Dùng từ khóa Task 7).
- dữ liệu thô được chuyển về theo giao thức ETL truyền thống về data warehouse, để biến thành vàng dữ liệu sau khi trích xuất được chuẩn hóa có cấu trúc thành các bảng sau đó chạy các câu lệnh python để loại bỏ dữ liệu bị thiếu, sai định dạng, bị sai,...kết quả thu được dữ liệu đúng, đủ, sạch

Giai đoạn 4 (Maintenance): Làm sao để ổ cứng không bị đầy rác theo năm tháng? (Dùng từ khóa Task 4).
để ổ cứng ko bị đầy theo năm tháng: sẽ sử dụng tiến trình tự động thực hiện xóa dữ liệu đã quá 30 ngày hoặc 1 tháng