# 🏛️ RESEARCH 00 — MEDALLION ARCHITECTURE & CLOUD-NATIVE STORAGE

> **Task:** 2.0 | **Module:** 2 — Distributed Systems & Big Data
> **Ngày bắt đầu:** 2026-08-28
> **Trạng thái:** ✅ Hoàn thành — 2026-09-02

---

## 🎯 Mục tiêu đầu ra (Learning Outcomes)
Hoàn thành bài này, bạn phải đạt được các năng lực cốt lõi:
1. **Tư duy Kiến trúc Lakehouse:** Hiểu vì sao Data Lakehouse kết hợp được ưu điểm của Data Warehouse (ACID, schema enforcement, hiệu năng BI) và Data Lake (lưu trữ chi phí thấp, định dạng mở, phục vụ AI/ML).
2. **Làm chủ 3 tầng Medallion:** Phân biệt rõ mục đích, tiêu chuẩn dữ liệu và đối tượng sử dụng của **Bronze** (Raw/Append-only), **Silver** (Cleaned/Enriched/Conformed), và **Gold** (Aggregated/Business Metrics).
3. **Quản trị chất lượng & Bất biến:** Nắm vững nguyên tắc Immutability ở tầng Bronze (Single Source of Truth) để phục vụ tái xử lý (Reprocessing/Audit) khi logic chuyển đổi thay đổi.
4. **Nhận diện Anti-patterns:** Nhận biết các lỗi thiết kế phổ biến khiến Medallion sụp đổ (bỏ qua Silver nhảy thẳng sang Gold, biến Bronze thành bãi rác không dọn, hoặc over-engineering cho các dự án quy mô nhỏ).

---

## 🧠 Framework 5 Tầng — Medallion Architecture

### Tầng 1 — WHAT
> *(Viết định nghĩa bằng lời của BẠN — 1-2 câu, không copy)*

```
medallion architecture là cách tổ chức dữ liệu thành 3 tầng chất lượng tăng dần từ bronze, sliver, gold
```

### Tầng 2 — HOW (3 Layer)

#### Bronze Layer
```
[dữ liệu tầng này là raw data, dữ liệu thô được lấy từ API Web apps hay các nguồn khác nhau, dữ liệu gần giống với phiên bản gốc nhất,  tính bất biến (immutability) ]
```

#### Silver Layer
```
[chuyển đổi làm sạch dữ liệu từ bronze, dữ liệu được biến đổi, chuẩn hóa, sẵn sàng cung cấp cho tầng trên cùng sử dụng, Silver còn join nhiều nguồn thành 1 schema thống nhất — đây là việc khó nhất ở tầng này]
```

#### Gold Layer
```
[phục vụ báo cáo, tổng hợp, phân tích đánh giá cho lãnh đạo của công ty, giúp hoạch định chiến lược, Gold phục vụ nhiều đối tượng khác nhau (Bộ trưởng, DA, Data Scientist) bằng các bảng khác nhau]
```

### Tầng 3 — WHY
> *(Tại sao Medallion tốt hơn kiến trúc cũ DWH + Data Lake riêng?)*

```
[medallion của data lakehouse kế thừa những ưu điểm của kiến trúc cũ dwh+data lake; dwh có luồng dữ liệu: etl(extract-transform-load) chúng xử lý dữ liệu sau đó mới load vào warehouse điều này dẫn đến quá trình xử lý làm sach chậm, tốn nhiều tài nguyên; còn data lake thì elt (extract-load-transform) chúng đưa hết dữ liệu vào lake rồi một luồng dùng để huấn luyện là ML, còn nếu muốn tính toán, phân tích thì chúng lại phải etl làm sạch dữ liệu rồi mới sử dụng được, nhược điểm là dữ liệu bẩn, lưu trữ tốn kém; còn medallion thì kết hợp mô hình medaliion và elt để xử lý dữ liệu dữ liệu được load mưu trữ sau đó xử lý lồng ghéo qua mô hình medallion bằng cách tranform qua từng mô hình]
``` 

### Tầng 4 — FAILURE
> *(3 cách Medallion có thể fail trong thực tế)*

```
1. [biến tầng sliver thành nơi chứa đựng những dữ liệu rác, chưa được làm sạch, khi DE lười hoặc bị áp lực về tiến độ nên bỏ hoặc làm hời hợt việc làm sạch dữ liệu]
2. [chi phí vận hành tăng do sử dụng nhiều pipeline giữa các tầng mà không đem lại hiệu quả tương xứng, vì các tầng trong mô hình medallion thông qua transform và cung cấp dữ liệu chất lượng cao ]
3. [sự mẫu thuẫn giữa DE và DA, khi DE và DA không lắng nghe, hiểu nhau, thì việc thiết kế medallion sẽ không đem đến hiệu quả khi DE phụ trách các tầng bronze-sliver còn DA sử dụng kết quả tại tầng gold để phân tích đánh giá]
```

### Tầng 5 — TRADE-OFF
> *(Khi nào KHÔNG nên dùng Medallion?)*

```
[hệ thống có quy mô nhỏ, giới hạn về lưu trữ, chi phí triển khai , hệ thống có nguồn dữ liệu sạch có thể sử dụng cho các tác vụ cấp cap như phân tích, đánh giá hoặc huấn luyện mô hình ml]
```

---

## 🔗 Kết Nối Kiến Thức Cũ — Idempotency Trong Medallion Pipeline

> **Nguồn gốc:** Module 0 Task 7 (ETL Foundation) → áp dụng trực tiếp vào Bronze→Silver pipeline
> **Bài học từ Hiệu trưởng 2026-09-02:** Biết tên khái niệm chưa đủ — phải biết CƠ CHẾ.

### ❌ Cách sai — gây trùng dữ liệu

```sql
-- Pipeline fail lúc 2am, chạy lại sáng hôm sau
INSERT INTO silver
SELECT * FROM bronze WHERE date = '2026-09-02'

-- Chạy lần 2: INSERT lại toàn bộ → dữ liệu bị trùng đôi
-- 50% đã được ghi từ lần 1 → giờ có 150% dữ liệu
```

### ✅ Phương án 1 — MERGE/UPSERT

```sql
MERGE INTO silver AS target
USING (SELECT * FROM bronze WHERE date = '2026-09-02') AS source
ON (target.id_can_cuoc = source.id_can_cuoc
    AND target.valid_from = source.ngay_nap)
WHEN MATCHED THEN
    UPDATE SET target.tinh = source.tinh, ...
WHEN NOT MATCHED THEN
    INSERT (id_can_cuoc, tinh, valid_from, ...) VALUES (...)

-- Chạy lần 2: record đã có → UPDATE (không thêm dòng mới)
-- Kết quả: luôn như nhau dù chạy bao nhiêu lần
```

**Khi nào dùng:** Khi Silver cần giữ lịch sử (SCD Type 2), cần xác định chính xác dòng nào đã tồn tại.

### ✅ Phương án 2 — Xóa partition rồi ghi lại

```sql
-- Bước 1: Xóa sạch partition của ngày đó
DELETE FROM silver WHERE batch_date = '2026-09-02'

-- Bước 2: Ghi lại từ đầu
INSERT INTO silver
SELECT * FROM bronze WHERE date = '2026-09-02'

-- Chạy lần 2: Bước 1 xóa sạch → Bước 2 ghi lại
-- Kết quả: luôn như nhau dù chạy bao nhiêu lần
```

**Khi nào dùng:** Khi pipeline đơn giản hơn, Silver không cần merge phức tạp, partition rõ ràng theo ngày.

### 📌 Ghi nhớ cốt lõi

```
Idempotency = "Chạy 1 lần hay 10 lần → kết quả như nhau"

Bronze đã idempotent tự nhiên:
  → Mỗi batch là 1 file riêng theo ngày → chạy lại chỉ ghi đè file đó
  → s3://bronze/date=2026-09-02/batch.parquet (overwrite)

Silver cần CHỦ ĐỘNG implement idempotency:
  → Dùng MERGE hoặc DELETE+INSERT theo partition
  → Không dùng INSERT thuần túy
```

---

## 🛠️ BÀI TẬP — Thiết Kế Medallion Cho Bộ Nội Vụ

**Tình huống:**
- Bộ Nội Vụ cần xây Data Platform cho 63 tỉnh thành
- Hiện tại: Oracle DB tại mỗi tỉnh (Legacy, on-premise)
- Mục tiêu: Báo cáo thống nhất toàn quốc + lưu lịch sử 10 năm

**Yêu cầu:** Thiết kế sơ đồ 3 layer cho hệ thống này:

### BRONZE Layer
```
Dữ liệu đến từ đâu?:
  ✅ Đúng — Oracle DB tại mỗi tỉnh (63 nguồn)
  📌 Thêm: Cơ chế nạp là CDC (Change Data Capture) hoặc batch export hàng đêm

Lưu định dạng gì?:
  ✅ Đúng — Parquet

Tổ chức thư mục:
  ❌ Cậu viết: tỉnh/năm
  ✅ Đúng phải là: partition theo NGÀY NẠP (không phải tỉnh/năm)
     Lý do: khi pipeline fail ngày 15, ta chạy lại đúng ngày 15, không ảnh hưởng ngày khác

Ví dụ path chuẩn:
  s3://bucket/bronze/noi_vu/
    ├── entity=ho_so_can_bo/year=2026/month=09/day=02/batch_HN.parquet
    ├── entity=ho_so_can_bo/year=2026/month=09/day=02/batch_DN.parquet
    ├── entity=ky_luat/year=2026/month=09/day=02/batch_HN.parquet
    └── entity=luong/year=2026/month=09/day=02/batch_HN.parquet

Mỗi entity là 1 loại dữ liệu riêng:
  - entity=ho_so_can_bo  : họ tên, CCCD, ngày sinh, chức vụ, đơn vị
  - entity=bien_che      : số được phép vs thực tế đang có
  - entity=tuyen_dung    : kỳ thi, người đậu, ngày vào biên chế
  - entity=ky_luat       : ai, lỗi gì, ngày nào, mức độ
  - entity=luong         : bậc lương, hệ số
```

### SILVER Layer
```
Transform những gì từ Bronze?:
  ✅ Đúng — chuẩn hóa định dạng (ngày tháng, mã tỉnh, tên cột)
  📌 Thêm 2 việc cậu bỏ sót:
    - Join nhiều nguồn: merge ho_so + luong + ky_luat thành view thống nhất
    - Áp SCD Type 2: khi cán bộ chuyển tỉnh → thêm dòng mới, đánh is_current

Schema chuẩn hóa:
  ❌ Cậu đặt Star Schema vào Silver — sai tầng
  ✅ Silver = bảng "sạch" gần với nguồn, KHÔNG aggregate, KHÔNG denormalize

  silver_ho_so_can_bo:
    id_surrogate (PK, auto-increment — không phải CCCD)
    id_can_cuoc (12 số, NK)
    ho_va_ten
    ngay_sinh       (format: yyyy-mm-dd)
    chuc_vu
    don_vi
    ma_tinh         (chuẩn hóa về mã 2 chữ số)
    valid_from      (SCD Type 2 — ngày bắt đầu hiệu lực)
    valid_to        (SCD Type 2 — ngày kết thúc, NULL nếu đang hiện hành)
    is_current      (True/False)
    batch_date      (ngày nạp — dùng cho Idempotency)

  silver_luong:
    id_can_cuoc, bac_luong, he_so, ngay_ap_dung, batch_date

  silver_ky_luat:
    id_can_cuoc, loai_ky_luat, ngay_ky_luat, muc_do, batch_date

Validation rules (6 rules đã viết):
  ✅ id_can_cuoc: đúng 12 ký tự số
  ✅ he_so_luong > 0 và ≤ mức tối đa theo bậc
  ✅ ngay_sinh ≤ năm hiện tại (không sinh trong tương lai)
  ✅ 1 CCCD chỉ có 1 dòng is_current = True (SCD constraint)
  ✅ CCCD unique trong Silver tại cùng valid_from (không duplicate import)
  ✅ Tất cả datetime format yyyy-mm-dd
```

### GOLD Layer
```
❌ Cậu liệt kê nội dung/cột thay vì đặt TÊN BẢNG cụ thể
✅ Gold = tên bảng rõ ràng, denormalized hoàn toàn, đọc là hiểu ngay

Bảng phục vụ báo cáo Bộ trưởng:
  → rpt_bien_che_toan_quoc
    (tinh, tong_bien_che_duoc_phep, tong_thuc_te, tong_luong_chi_tra,
     tong_ky_luat, tong_den_tuoi_huu, thang, nam)

Bảng phục vụ tra cứu công dân:
  → dim_can_bo_lookup
    (id_can_cuoc, ho_va_ten, ngay_sinh, chuc_vu, don_vi, tinh_hien_tai,
     trang_thai [đang làm / đã nghỉ / kỷ luật])

Bảng phục vụ phân tích trend:
  → fact_bien_dong_nhan_su
    (tinh, thang, nam,
     so_can_bo_nu, so_can_bo_chuyen_tinh, so_can_bo_moi_tuyen,
     so_can_bo_ky_luat, so_cap_vo_chong_cung_nha_nuoc)
```

---

## 📝 Ghi Chú Cá Nhân
*(Những điều bạn tự rút ra, câu hỏi phát sinh, liên hệ với bài cũ)*

```
[Học viên điền vào đây]
```
