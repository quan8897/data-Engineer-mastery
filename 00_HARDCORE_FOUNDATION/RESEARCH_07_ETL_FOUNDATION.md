# 🛡️ KIẾN TRÚC & PHÒNG THỦ: TASK 07 (ETL FOUNDATION)

> **Quân luật:** Giải thích như một Kỹ sư thực thụ giải thích cho người lính mới. Cấm Copy-paste wikipedia. Dùng ví dụ đời sống/dòng chảy để minh họa khái niệm.

---

## 1. Bản chất của lò luyện ETL
**Câu hỏi:** Trong môi trường dữ liệu quy mô lớn (Petabyte), **ETL (Extract - Transform - Load)** nghĩa là gì? Tại sao phải chia làm 3 bước này mà không tải thẳng vào CSDL rồi đọc luôn?
*(Điền câu trả lời của cậu: ...)*
- ETL là trích xuất dữ liệu - chuyển đổi và tải, nếu ko làm theo 3 bước mà tải thẳng dữ liệu sẽ rác khả năng dữ liệu ko thể phục vụ cho sau này, ko theo một quy chuẩn nào cả, và việc xử lý dữ liệu sau này sẽ rất khó khăn, ko chuyển đổi, dữ liệu từ nhiều nguồn nhiều định dạng làm việc xử lý dữ liệu trở nên tốn thời gian xử lý và tài nguyên tính toán, mỗi loại dữ liệu lại mỗi kiểu không có tính nhất quán

## 2. Nút thắt cổ chai (Bottleneck) của Database
**Câu hỏi:** Nhiều người bảo: "Cứ Load thẳng dữ liệu thô vào SQL Database, rồi dùng lệnh UPDATE/SELECT để biến đổi (Transform) luôn trong đó cho nhanh, đỡ phải viết code Python/Spark". 

Dưới góc độ Kiến trúc sư Hệ thống, cậu hãy vạch ra hậu quả thảm khốc của việc làm này khi dữ liệu lên tới hàng chục Terabyte? Tại sao việc tách khâu "Transform" ra một máy chủ khác (bằng Python/Spark) lại cứu mạng toàn bộ hệ thống?
*(Điền câu trả lời của cậu: ...)*
dữ liệu từ nhiều nguồn nhiều định dạng làm việc xử lý dữ liệu trở nên tốn thời gian xử lý và tài nguyên tính toán, mỗi loại dữ liệu lại mỗi kiểu không có tính nhất quán; ví dụ như ngày tháng từ các nguồn dữ liệu có định dạng khác nhau, nếu load thẳng về luôn dùng update.select thì đúng là thảm họa, chẳng biết làm như nào cho đúng

## 3. Bài toán "Nửa nạc nửa mỡ" (Data Inconsistency / Atomic failure)
**Câu hỏi:** Giả sử script Python của cậu đang trong quá trình "Load" (Bơm dữ liệu đã làm sạch vào Database). Mới bơm được 50% thì... Đùng! Khởi động lại Server do mất điện. 

Cơ sở dữ liệu đang chứa một mớ dữ liệu "nửa nạc nửa mỡ". Ngày hôm sau, khi hệ thống có điện lại và Cron tự chạy script lần nữa, nó sẽ cắm đầu bơm lại từ đầu, gây **Trùng lặp dữ liệu (Data Duplication)**. 

Là một Senior Data Engineer, cậu sẽ thiết kế cơ chế/tư duy gì (không cần code, chỉ cần mô tả thuật toán) để script của cậu KHÔNG BAO GIỜ bơm đúp dữ liệu khi gặp sự cố sập nguồn này?
*(Điền câu trả lời của cậu: ...)*
nếu việc đồng bộ dữ liệu bị ngắt đột ngột, chúng ta sử dụng cron deamon giống như người thư kí theo dõi tiến trình nếu chưa thực hiện xong sẽ tiếp tục thực hiện mà ko chạy lại gây trùng lặp dư thừa
---
*(Khi nộp bài, báo "Tôi đã sẵn sàng phòng thủ Task 07".)*
--------------tranh luận-----------------
🥊 Đòn 1: Tại sao phải có "Vùng hạ cánh" (Raw/Landing Zone)?
Cậu nói ETL là để tránh dữ liệu rác. Vậy tại sao các kỹ sư Big Data không vừa Extract (kéo) vừa Transform (xử lý) luôn trên đường truyền cho nhanh? Tại sao người ta luôn phải tốn thêm ổ cứng để lưu một bản Dữ liệu thô (Raw Data) y hệt như nguồn trước khi bắt đầu Transform? Nếu nguồn thay đổi định dạng đột ngột, việc có bản Raw này giúp gì cho cậu?
bản raw data nếu nguồn thay đổi định dạng đột ngột, việc lưu trữ raw để so sánh được trước và sau khi thay đổi định dạng , thay vì kéo xử lý luôn, khi thay đổi định dạng đột ngột, ko biết được dữ liệu đổi từ định dạng nào sang định dạng nào để đánh giá; raw data còn có thể sử dụng lại khi dữ liệu có lỗi, làm hỏng đoạn dữ liệu thì có raw-data để thực hiện xử lý lại.
🥊 Đòn 2: Sự sụp đổ của "All-in-SQL"
Cậu có nhắc đến việc "thảm họa" khi dùng UPDATE/SELECT trực tiếp trong DB. Nhưng giả sử tôi nâng cấp CPU/RAM cho Database cực mạnh, tại sao việc vác 10TB dữ liệu ra ngoài chạy Python/Spark vẫn tối ưu hơn là dùng lệnh SQL xử lý ngay tại chỗ? Hãy giải thích dưới góc độ Tách rời Tính toán (Compute) và Lưu trữ (Storage).
sql sẽ tập trung việc lưu trữ hơn là tính toán

🥊 Đòn 3: Trận chiến với Idempotency (Tính khả dĩ)
Quay lại tình huống sập nguồn khi đang Load 50%. Cậu nói dùng "thư ký Cron" để theo dõi. Thực tế, Cron không làm được việc đó. Bây giờ, hãy tưởng tượng script Python của cậu bị chết giữa chừng. Khi chạy lại, làm sao cậu đảm bảo kết quả cuối cùng trong Database vẫn chuẩn 100%, không thiếu một dòng và không thừa một dòng, dù cậu có lỡ tay chạy script đó 10 lần liên tiếp? (Gợi ý: Hãy tìm hiểu từ khóa Idempotency hoặc cơ chế Staging Table/Atomic Swap).

theo như tìm hiểu thì nó giống như một transaction vậy: nếu A chuyển cho B 1 triệu, lệnh chỉ được báo là thành công nếu B nhận được 1 triệu, nếu B chưa nhận được thì nếu A đã đến bước bị trừ tiền sẽ được hoàn tiền trở lại, 
sql transaction begin commit rollback
Lính mới, hãy phản công! Đừng dùng lý thuyết suông, hãy mô tả logic và giải pháp cụ thể. Chỉ khi cậu "thông" 3 điểm này, chúng ta mới bắt đầu đặt tay vào code.