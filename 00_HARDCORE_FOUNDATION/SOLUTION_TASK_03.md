# 🛠️ GIẢI PHÁP HỆ THỐNG - MODULE 0

## TASK 3: TỐI ƯU HÓA PHÂN VÙNG (PARTITIONING) & LVM

### 1. Tại sao phải tách biệt phân vùng `/data`?
- **Kịch bản thảm họa:** Nếu dữ liệu của tỉnh Hà Nội gửi về quá lớn làm đầy ổ đĩa (100% disk usage), mà thư mục `/data` nằm chung với thư mục hệ thống `/`, chuyện gì sẽ xảy ra với Server Linux?
`hệ thống sẽ đứng, treo và tắt hệ thống khởi động lại vì tràn bộ nhớ`
- **Lợi ích bảo mật:** Nếu một phân vùng bị hỏng (Corrupted), việc tách biệt giúp bảo vệ phần còn lại như thế nào?
`nếu một phân vùng bị hỏng các phân vùng còn lại sẽ đóng vai trò backup trong khi đó chúng ta có thể sửa chữa phân vùng hỏng mà ko làm ảnh hưởng đến các phân vùng còn lại`
### 2. Tư duy về LVM (Logical Volume Manager)
Hãy tưởng tượng cậu có 2 ổ đĩa vật lý 1TB. 
- Nếu dùng phân vùng cứng (Standard Partition), cậu chỉ có 2 miếng 1TB rời rạc. 
- LVM giải quyết bài toán này như thế nào? (Gợi ý các khái niệm: **PV - Physical Volume**, **VG - Volume Group**, **LV - Logical Volume**). 
``Cách thức hoạt động các tầng của LVM:
Tầng đầu tiên: Hard drives là tầng các disk ban đầu khi chưa chia phân vùng
Partitions: Sau đó ta chia các disk ra thành các phân vùng nhỏ hơn *** Physical volume** : Từ một partitions ta sẽ tạo ra được một physical
Group volume : Ta sẽ ghép nhiều physical volume thành một group volume
Logical volume : Ta sẽ có thể tạo ra được logical volume
 theo ý hiểu của tôi: từ 2tb chúng ta sẽ chia nhỏ dần theo ý muốn thu được các phân vùng ảo của ổ đĩa ảo trên một đĩa cứng vật lý``có thể chia linh hoạt thay vì 2 ổ cứng vật lý, thiếu sự linh hoạt trong quản lý
- Tại sao khi làm cho TTDLQG, **LVM là bắt buộc**?
vì dữ liệu lớn, nên việc phân vùng để dễ trong việc quản lý, sửa chữa khi lỗi, việc thất thoát dữ liệu sẽ xảy ra nếu không có nhiều phân vùng hoặc hệ thống lưu trữ ko có khả năng mở rộng cũng như linh hoạt
### 3. English for Infrastructure
Giải thích ý nghĩa và tầm quan trọng của:
- **Scalability (Khả năng mở rộng):** Tại sao LVM lại đại diện cho tính Scalability?
dung lượng đĩa có thể được quản lý một cách động, giúp dễ dàng giải quyết tình trạng thiếu không gian đĩa, xây dựng lưu trữ quy mô lớn vượt qua giới hạn của các đĩa vật lý riêng lẻ; có thể gộp các ổ đĩa cứng thành một kho lưu trữ
- **Volume Expansion:** Quy trình mở rộng ổ đĩa mà không cần tắt Server (Zero Downtime).
Thêm Physical Volume mới vào Volume Group Đăng ký đĩa mới làm Physical Volume.
>sudo pvcreate /dev/sdc
Sau đó, mở rộng Volume Group:
sudo vgextend vg_data /dev/sdc
Mở rộng Logical Volume Ví dụ, thêm 10GB:
>sudo lvextend -L+10G /dev/vg_data/lv_data
Mở rộng File System Áp dụng việc tăng Logical Volume vào file system (ví dụ ext4):
>sudo resize2fs /dev/vg_data/lv_data 
# nguồn tham khảo: https://www.digibeatrix.com/ubuntu/vi/system-administration-and-optimization-vi/ubuntu-lvm-storage-management/
https://viblo.asia/p/tim-hieu-ve-lvm-trong-linux-logical-volume-manager-PwlVmbAP45Z
---
*Mentor Note: Task này đòi hỏi cậu phải đọc tài liệu về hạ tầng Linux. Cậu đang xây dựng "đất" cho dữ liệu đứng chân, đất không vững thì dữ liệu sẽ chìm vào hư vô.*
