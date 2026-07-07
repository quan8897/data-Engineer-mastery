# 📘 NATIONAL DATA CENTER: ARCHITECTURE & OPERATIONS PLAYBOOK

## 📜 GIỚI THIỆU
Cuốn Playbook này tài liệu hóa toàn bộ quy trình thiết kế, triển khai và quản trị hệ thống dữ liệu quy mô quốc gia. 
**Tác giả:** [Tên cậu]
**Mentor:** Antigravity (Senior System Architect)
**Mục tiêu:** Tiêu chuẩn hóa quy trình xử lý dữ liệu Petabyte-scale.

---

## 📂 CHƯƠNG 1: THIẾT KẾ KIẾN TRÚC INGESTION LAYER
*Trạng thái: Đã hoàn thành (Duyệt ngày 2026-03-14)*

### 1.1. Cấu trúc Partitioning (Phân đoạn dữ liệu)
Để đảm bảo hiệu suất quét dữ liệu (**Scanning Performance**) và khả năng lưu trữ lâu dài, hệ thống áp dụng cấu trúc **Date-based Partitioning**:
- **Root:** `/data/raw`
- **Tầng 1 (Date):** `YYYYMMDD` (Giúp cô lập dữ liệu theo ngày, tối ưu lệnh `ls` và `find`).
- **Tầng 2 (Province):** Mã tỉnh (Ví dụ: `hn`, `hcm`).
- **Tầng 3 (Data Type):** Loại dữ liệu (Ví dụ: `bhyt`, `datdai`).

### 1.2. Naming Convention (Quy tắc đặt tên chuẩn quốc gia)
Mọi file nạp vào hệ thống bắt buộc tuân thủ: 
`YYYYMMDD_HHMMSS_Province_Type_UniqueID.extension`
- **Lợi ích:** Đảm bảo **Immutability** (tính bất biến), tránh **Overwrite** (ghi đè) và hỗ trợ **Alphanumeric Sorting** (sắp xếp tự động).

---

## 🔑 CHƯƠNG 2: LINUX SYSTEM ADMINISTRATION & SECURITY

### 2.1. Quản trị đặc quyền (Privilege Management)

Để làm chủ được hệ thống Linux tại Trung tâm Dữ liệu Quốc gia, mỗi cá nhân phải thấu hiểu hệ thống phân quyền. Điều này nhằm tối ưu hóa việc quản lý và duy trì tính ổn định, bảo mật cho hạ tầng dữ liệu quy mô lớn.
#### 2.1.1. Lớp hạ tầng (Infrastructure Layer - The Kernel & Shell)
Trong môi trường Trung tâm Dữ liệu, việc quản lý **Ownership & Access Control** (Quyền sở hữu & Quyền truy cập) là yếu tố then chốt để bảo vệ dữ liệu nhạy cảm. Hệ thống Linux quản lý mọi thứ (kể cả phần cứng) dưới dạng tệp tin thông qua **File System Hierarchy** (Hệ thống tệp).

**Cấu trúc thư mục gốc `/` (Root Directory):**
Điểm khởi đầu cho toàn bộ hệ thống tệp:
- `/root`: Thư mục nhà của người dùng quản trị (**Superuser / Root privileges**).
- `/var/log`: Nơi lưu trữ nhật ký hệ thống (log files) - cực kỳ quan trọng để debug lỗi đường ống dữ liệu.
- `/etc`: Chứa các tệp cấu hình hệ thống (như cấu hình cơ sở dữ liệu `db.conf`).

*Ví dụ từ Module 1:* Tạo cây thư mục nhằm mục đích lưu trữ dữ liệu của từng tỉnh:
```bash
mkdir -p /data/raw/20260315/hanoi /data/raw/20260315/hochiminh
```

#### 2.1.2. Quản lý Người dùng và Nhóm (User & Group Management)
**Khái niệm:** Phân chia người dùng vào các nhóm riêng biệt để dễ dàng quản lý đặc quyền.
Sau khi tạo người dùng, ta tiến hành gán quyền sở hữu, đồng thời phân quyền cho đơn vị nào thì chỉ được truy cập tài liệu của đơn vị đó.

**Example:**
```bash
# Tạo nhóm data_collector
groupadd data_collector

# Tạo user cho Hà Nội và HCM, đồng thời gán vào nhóm data_collector
useradd -m -G data_collector user_hanoi 
useradd -m -G data_collector user_hcm 
```

#### 2.1.3. Cấu trúc phân quyền (Permissions & Ownership)
**Khái niệm:** Có 3 quyền cơ bản gắn cho 3 đối tượng độc lập: Chủ sở hữu tệp (user), Nhóm (group), và Các người dùng khác (others).
- **Read (`r` - 4):** Quyền đọc nội dung dữ liệu.
- **Write (`w` - 2):** Quyền sửa nội dung dữ liệu.
- **Execution / Directory Traversal (`x` - 1):** Đối với file, `x` là quyền thực thi (Execution). Đối với thư mục (directory), `x` là quyền đi xuyên qua (Directory Traversal - cho phép dùng lệnh `cd` để vào thư mục, nhưng không được dùng lệnh `ls` nếu thiếu quyền `r`).

*Quy tắc cộng quyền:* Khả năng kết hợp các quyền như `7` (Full rwx), `6` (rw-), `5` (r-x).

**Quản lý quyền sở hữu (Ownership):**
- `chmod`: Thay đổi quyền truy cập.
- `chown`: Thay đổi người sở hữu tệp.

**Example:**
```bash
# Thay đổi quyền sở hữu (Ownership) cho user của từng tỉnh
chown user_hanoi:data_collector /data/raw/20260315/hanoi
chown user_hcm:data_collector /data/raw/20260315/hochiminh

# Cấp quyền xuyên qua thư mục cha cho các user (711 = rwx cho Root, x cho Group, x cho Others)
chmod 711 /data/raw /data/raw/20260315

# Bảo mật cấp Tỉnh: Cấp toàn quyền cho chủ sở hữu, chặn hoàn toàn người dùng khác (700)
chmod 700 /data/raw/20260315/hanoi
chmod 700 /data/raw/20260315/hochiminh
```

> [!CAUTION]
> **Cảnh báo Bảo mật (Security Warning):** Tại Trung tâm Dữ liệu Quốc gia, bắt buộc tuân thủ **Principle of Least Privilege (PoLP)** - Nguyên tắc đặc quyền tối thiểu. Chỉ cấp đúng quyền cần thiết để người dùng hoàn thành công việc nhằm tránh rủi ro.

---

### 2.2. Quản trị lưu trữ (Storage Management & LVM)

**Khái niệm:** LVM (**Logical Volume Manager**) là lớp trừu tượng hóa cho phép quản lý dung lượng đĩa cứng một cách linh hoạt (**Scalability**). Đây là tiêu chuẩn bắt buộc tại Trung tâm Dữ liệu Quốc gia để đảm bảo khả năng mở rộng không giới hạn.

#### 2.2.1. Mô hình "Xây nhà" (Analogy)
Để dễ hình dung hệ thống LVM, ta có thể so sánh với việc xây dựng một ngôi nhà:
- **Physical Volume (PV) - Viên gạch:** Các ổ đĩa vật lý rời rạc được khai báo vào hệ thống.
- **Volume Group (VG) - Đống gạch:** Kho chứa tổng dung lượng được hợp nhất từ nhiều PV.
- **Logical Volume (LV) - Móng nhà:** Phân vùng ảo được "cắt" ra từ VG để đưa vào sử dụng thực tế.
- **File System - Nền nhà:** Lớp định dạng (ext4/xfs) phủ lên LV để hệ điều hành có thể ghi dữ liệu.

#### 2.2.2. Quy trình mở rộng không dừng hệ thống (Zero Downtime Expansion)
Khi một phân vùng dữ liệu tỉnh bị đầy, ta thực hiện nới rộng theo các bước sau:
1. **Thêm gạch Physical Volume(PV):** `pvcreate /dev/sdb`
2. **Đổ gạch vào đống Volume Group(VG):** `vgextend vg_data /dev/sdb`
3. **Nới rộng móng nhà Logical Volume(LV):** `lvextend -L +100G /dev/vg_data/lv_data`
4. **Trát xi măng mặt nền (Resize FS):** `resize2fs /dev/vg_data/lv_data` (Đối với ext4) hoặc `xfs_growfs /data` (Đối với xfs).

> [!TIP]
> **Mẹo chuyên gia:** Bạn có thể gộp lệnh tăng LV và Resize File System làm một bằng tham số `-r`:
> `lvextend -L +10G /dev/vg_name/lv_name -r`

#### 2.2.3. Tầm quan trọng của việc nới rộng File System
Nếu kỹ sư chỉ chạy lệnh `lvextend` mà quên lệnh `resize2fs` hoặc `xfs_growfs`:
- **Lệnh `lsblk` hoặc `lvs`:** Vẫn ghi nhận dung lượng đã tăng (ví dụ từ 100GB lên 200GB).
- **Lệnh `df -h`:** Vẫn báo dung lượng cũ (100GB).
- **Hậu quả:** Hệ thống báo lỗi **"No space left on device"** khi ghi file mới, do lớp File System chưa được mở rộng để quản lý vùng dung lượng ảo mới thêm vào.

> [!IMPORTANT]
> **Isolated Storage:** Luôn tách biệt `/data` ra phân vùng (LV) riêng biệt để đảm bảo khi dữ liệu đầy, hệ điều hành (`/`) vẫn hoạt động bình thường để cứu hộ.

*Ghi chú của Mentor: Cậu càng viết chắc tay trong các file SOLUTION, cuốn Playbook này càng trở nên giá trị. Đừng viết cho xong, hãy viết như thể cậu đang bàn giao tài liệu cho thế hệ kỹ sư sau.*
