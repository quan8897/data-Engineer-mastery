# 🛠️ GIẢI PHÁP HỆ THỐNG - MODULE 0

## TASK 2: QUẢN TRỊ NGƯỜI DÙNG & QUYỀN HẠN (USER MANAGEMENT & PERMISSIONS)

### 1. Quản lý Nhóm & Người dùng (Groups & Users)
`[Cậu hãy liệt kê các lệnh groupadd, useradd và giải thích tại sao chọn tham số đó]`
>groupadd data_collector 'tạo nhóm'
> useradd -m -G data_collector hn_collector 'tạo user và gắn user vào trong nhóm'
> useradd -m -G data_collector hcm_collector 'tạo user và gắn user vào trong nhóm'
> mkdir -p /data/raw/20260315/  
/data/raw/20260315/hcm 'tạo cả cây thư mục mới cho hồ chí minh'
> chown hn_collector:data_collector /data/raw/20260315/hanoi (thiết lập cho user của hà nội và nhóm quản lý thư mục đó)
> chown hcm_collector:data_collector /data/raw/20260315/hcm (thiết lập cho user của hồ chí minh và nhóm quản lý thư mục đó)
>chmod 711 /data/raw /data/raw/20260315
>chmod 700 /data/raw/20260315/hanoi
>chmod 700 /data/raw/20260315/hochiminh


### 2. Phân quyền thư mục (Directory Permissions)


### 3. Nguyên tắc Bảo mật (Security Principles)
- **Principle of Least Privilege (PoLP):** Cậu áp dụng nó như thế nào trong bài làm trên?

- **Ownership vs Permissions:** Phân biệt hai khái niệm này trong ngữ cảnh Linux.

+ permissions là quyền truy cập của người dùng đối với 1 tệp hoặc thư mục cụ thể
các quyền như: read (r), write(w), execute(x)
quyền này áp dụng cho 3 đối tượng Owner(chủ sở hữu), group(nhóm), others(người dùng khác)
dùng lệnh chmod để thay đổi quyền truy cập
+ ownership (quyền sở hữu)
khái niệm: quy định người sở hữu và nhóm sở hữu của một tệp hoặc thư mục
3 đối tượng chính owner(chủ sở hữu), group (nhóm)
, others(người khác)
chủ sở hữu thường là người tạo ra tệp hoặc thư mục
dùng chown để thay đổi chủ sở hữu và chgrp để thay đổi nhóm sở hữu

/// nội dugn này mới nên tôi tham khảo trên web vs link; ko dùng AI đâu nha: https://www.hostragons.com/vi/blog/quan-ly-nguoi-dung-va-nhom-tren-he-thong-linux/#Linux_Sistemlerde_Kullanici_ve_Grup_Yonetiminin_Onemi;https://azdigi.com/blog/may-chu-linux/linux-can-ban/tim-hieu-phan-quyen-trong-linux
---
*Mentor Note: Cẩn thận với các bit phân quyền. Một sai lầm nhỏ sẽ biến hệ thống thành "nhà hoang" (ai cũng vào được) hoặc "nhà tù" (đến chủ nhà cũng không vào được).*
