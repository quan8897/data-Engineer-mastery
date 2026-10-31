"""
LAB THỰC HÀNH MÔ PHỎNG: REPLICA IDENTITY (DEFAULT vs FULL) TRONG POSTGRESQL & DEBEZIUM CDC
Mục tiêu: Tận mắt nhìn thấy cấu trúc bản tin JSON của Debezium và tại sao REPLICA IDENTITY FULL là bắt buộc cho SCD Type 2.
"""
import json
import sys

def simulate_wal_and_debezium():
    print("=" * 70)
    print(" BẢNG DỮ LIỆU BAN ĐẦU: nhan_khau")
    print(" (id: 101, ho_ten: 'Nguyen Van A', dia_chi: 'Hai Duong', luong: 15000000)")
    print("=" * 70)

    # Thao tác nghiệp vụ: Công dân A chuyển địa chỉ lên Hà Nội và tăng lương lên 20 triệu
    # UPDATE nhan_khau SET dia_chi = 'Ha Noi', luong = 20000000 WHERE id = 101;

    print("\n>>> THỰC THI GIAO DỊCH:")
    print("    UPDATE nhan_khau SET dia_chi = 'Ha Noi', luong = 20000000 WHERE id = 101;\n")

    # 1. KỊCH BẢN 1: REPLICA IDENTITY DEFAULT (Mặc định của PostgreSQL)
    print("-" * 70)
    print("🚨 [KỊCH BẢN 1]: REPLICA IDENTITY = DEFAULT (Mặc định)")
    print("PostgreSQL chỉ ghi Primary Key (id) vào log phần dữ liệu cũ để tiết kiệm đĩa:")
    print("-" * 70)

    msg_default = {
        "op": "u",
        "ts_ms": 1728556800000,
        "source": {"db": "ql_danso", "table": "nhan_khau", "lsn": 24589012},
        "before": {
            "id": 101,
            "ho_ten": None,      # <-- BỊ NULL!
            "dia_chi": None,     # <-- BỊ NULL! (Không biết địa chỉ cũ là gì!)
            "luong": None        # <-- BỊ NULL! (Không biết lương cũ là bao nhiêu!)
        },
        "after": {
            "id": 101,
            "ho_ten": "Nguyen Van A",
            "dia_chi": "Ha Noi",
            "luong": 20000000
        }
    }
    print(json.dumps(msg_default, indent=2, ensure_ascii=False))

    print("\n💥 HẬU QUẢ VỚI DATA WAREHOUSE (SCD TYPE 2):")
    print("-> Data Warehouse muốn ghi nhận: Từ năm 2020 đến 2026, A ở 'Hai Duong' hưởng lương 15tr.")
    print("-> NHƯNG trường 'before' toàn NULL! Pipeline không thể biết giá trị trước đó là gì!")
    print("-> Buộc Data Warehouse phải chạy câu lệnh SELECT ngược lại kho để tra cứu (CỰC KỲ CHẬM)!")


    # 2. KỊCH BẢN 2: REPLICA IDENTITY FULL
    print("\n" + "=" * 70)
    print("🛡️ [KỊCH BẢN 2]: CHẠY LỆNH:")
    print("    ALTER TABLE nhan_khau REPLICA IDENTITY FULL;")
    print("PostgreSQL sẽ nhân bản TOÀN BỘ giá trị cũ của mọi cột vào file WAL:")
    print("=" * 70)

    msg_full = {
        "op": "u",
        "ts_ms": 1728556800000,
        "source": {"db": "ql_danso", "table": "nhan_khau", "lsn": 24590450},
        "before": {
            "id": 101,
            "ho_ten": "Nguyen Van A",
            "dia_chi": "Hai Duong",  # <-- ĐÃ CÓ ĐỊA CHỈ CŨ!
            "luong": 15000000        # <-- ĐÃ CÓ LƯƠNG CŨ!
        },
        "after": {
            "id": 101,
            "ho_ten": "Nguyen Van A",
            "dia_chi": "Ha Noi",
            "luong": 20000000
        }
    }
    print(json.dumps(msg_full, indent=2, ensure_ascii=False))

    print("\n✅ THẮNG LỢI CHO SCD TYPE 2:")
    print("-> Pipeline tự trị 100%: Lấy 'before.dia_chi' (Hai Duong) để chốt đóng phiên bản cũ.")
    print("-> Mở phiên bản mới với 'after.dia_chi' (Ha Noi). Không cần query ngược vào database!")

    # 3. CÁI GIÁ PHẢI ĐÁNH ĐỔI (TRADE-OFF)
    print("\n" + "-" * 70)
    print("⚠️ CÁI GIÁ PHẢI ĐÁNH ĐỔI (TẦNG 5 — TRADE-OFF):")
    print("1. Write Amplification trên WAL:")
    size_def = len(json.dumps(msg_default))
    size_full = len(json.dumps(msg_full))
    print(f"   - Kích thước bản tin DEFAULT : {size_def} bytes")
    print(f"   - Kích thước bản tin FULL    : {size_full} bytes (+{round((size_full-size_def)/size_def*100)}% dung lượng!)")
    print("2. Với bảng có 50 cột hoặc có cột JSON/Text lớn: Mỗi lần chỉ sửa 1 ký tự,")
    print("   Postgres vẫn phải nhân bản cả 50 cột vào file WAL -> Tốn I/O đĩa và mạng gấp nhiều lần!")
    print("-" * 70)

if __name__ == "__main__":
    simulate_wal_and_debezium()
