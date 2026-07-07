# học từ Gemini_AI
## học về Biến
- Hãy hình dung thế này: Biến giống như một cái thùng carton. Bạn lấy bút lông viết tên lên vỏ thùng (Khai báo tên biến), rồi bỏ đồ vật vào trong thùng (Gán giá trị). Khi cần dùng đồ, bạn chỉ cần gọi tên cái thùng ra.

- Trong Bash Script (Linux), có 3 luật thép về biến mà bạn bắt buộc phải khắc cốt ghi tâm. Nếu sai, kịch bản sẽ lỗi ngay lập tức.
+ Luật Thép 1: Quy tắc "Cấm Khoảng Trắng" khi khai báo
Trong các ngôn ngữ như Python hay C++, bạn có thể viết TEN = "Nguyen" cho đẹp mắt. Nhưng trong Linux thì tuyệt đối không.

❌ Lỗi (Sai bản chất): TEN = "Nguyen"
(Bash sẽ tưởng TEN là một câu lệnh, còn = và "Nguyen" là tham số truyền vào lệnh đó -> Báo lỗi command not found).

✅ Chuẩn (Đúng): TEN="Nguyen"
(Dấu bằng = phải dính chặt vào tên biến và giá trị).

+ Luật Thép 2: Chìa khóa "Dollar" ($) để mở thùng
Khi bạn viết tên thùng (TEN), Linux chỉ hiểu đó là chữ "T", "E", "N". Để lấy được đồ vật bên trong thùng ra, bạn phải gắn biểu tượng chìa khóa $ vào đằng trước.

Khai báo: TUOI=25

Sử dụng: echo "Tôi năm nay $TUOI tuổi."

Mẹo nâng cao (Chuẩn DE): Khi ghép biến vào sát một chữ khác, hãy dùng thêm cặp ngoặc nhọn {} để Bash không bị nhầm lẫn.
(Ví dụ: echo "Tôi có 5 ${LOAI_QUA}s" thay vì $LOAI_QUAs sẽ làm Bash đi tìm biến tên là LOAI_QUAs).

+ Luật Thép 3: Sự khác biệt tử thần giữa ' ' và " "
Đây là nơi 90% người mới học Linux dính bẫy.

Ngoặc kép " " (Mềm mỏng): Nó cho phép chìa khóa $ hoạt động.
echo "Xin chào $TEN" -> In ra: Xin chào Nguyen

Ngoặc đơn ' ' (Đóng băng): Bất cứ thứ gì nằm trong ngoặc đơn đều biến thành chữ viết chết (text tĩnh). Chìa khóa $ bị vô hiệu hóa.
echo 'Xin chào $TEN' -> In ra đúng nguyên văn: Xin chào $TEN