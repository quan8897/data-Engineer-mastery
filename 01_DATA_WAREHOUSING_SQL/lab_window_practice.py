import sqlite3
import pandas as pd

import pathlib

# Xác định thư mục chứa file script này và trỏ file DB vào đúng đó
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
DB_FILE = str(SCRIPT_DIR / "practice.db")

def init_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 1. Xóa bảng cũ nếu có để đảm bảo chạy lại luôn sạch (Idempotency)
    cursor.execute("DROP TABLE IF EXISTS fact_sales;")
    
    # 2. Tạo bảng doanh số
    cursor.execute("""
    CREATE TABLE fact_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tinh_id TEXT NOT NULL,
        quy TEXT NOT NULL,
        ngay_giao_dich TEXT NOT NULL,
        doanh_so REAL NOT NULL
    );
    """)
    
    # 3. Chèn dữ liệu thực hành (Có đồng doanh số ở Quý 1 để test RANK)
    sales_data = [
        # Tỉnh A
        ('Tinh_A', 'Q1', '2026-01-05', 100.0),
        ('Tinh_A', 'Q1', '2026-02-10', 150.0),
        ('Tinh_A', 'Q2', '2026-04-15', 200.0),
        ('Tinh_A', 'Q3', '2026-07-20', 300.0),
        
        # Tỉnh B (Đồng doanh số tổng Q1 với Tỉnh A để test câu hỏi RANK)
        ('Tinh_B', 'Q1', '2026-01-12', 100.0),
        ('Tinh_B', 'Q1', '2026-03-01', 150.0),
        ('Tinh_B', 'Q2', '2026-05-18', 250.0),
        ('Tinh_B', 'Q3', '2026-08-25', 150.0),
        
        # Tỉnh C (Doanh số thấp hơn)
        ('Tinh_C', 'Q1', '2026-02-01', 80.0),
        ('Tinh_C', 'Q1', '2026-03-15', 100.0),
        ('Tinh_C', 'Q2', '2026-06-01', 120.0),
        ('Tinh_C', 'Q3', '2026-09-10', 400.0)
    ]
    
    cursor.executemany("""
    INSERT INTO fact_sales (tinh_id, quy, ngay_giao_dich, doanh_so)
    VALUES (?, ?, ?, ?);
    """, sales_data)
    
    conn.commit()
    conn.close()
    print("-> Đã khởi tạo cơ sở dữ liệu practice.db với bảng fact_sales thành công!")

def run_query(sql_query):
    """Hàm chạy SQL và in kết quả ra màn hình dưới dạng bảng đẹp"""
    conn = sqlite3.connect(DB_FILE)
    try:
        df = pd.read_sql_query(sql_query, conn)
        # Thiết lập hiển thị rộng rãi cho console
        pd.set_option('display.width', 1000)
        pd.set_option('display.max_columns', 10)
        print("\n" + "="*80)
        print(f"SQL QUERY:\n{sql_query.strip()}")
        print("="*80)
        print("RESULT:")
        print(df.to_string(index=False))
        print("="*80 + "\n")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    init_database()
    
    # --- KHU VỰC CHẠY THỬ NGHIỆM TRUY VẤN ---
    
    # [1] THỬ NGHIỆM TRỰC QUAN: Sự khác biệt của ORDER BY trong OVER()
    
    query_1 = """
    SELECT tinh_id, quy, ngay_giao_dich, doanh_so,
           SUM(doanh_so) OVER (PARTITION BY quy) as tong_doanh_so_quy
    FROM fact_sales;
    """
    
    query_2 = """
    SELECT tinh_id, quy, ngay_giao_dich, doanh_so,
           SUM(doanh_so) OVER (PARTITION BY quy ORDER BY ngay_giao_dich) as tong_luy_ke_quy
    FROM fact_sales;
    """

    query_3 = """
    SELECT tinh_id, quy, ngay_giao_dich, doanh_so,
           SUM(doanh_so) OVER (PARTITION BY quy ORDER BY tinh_id) as tong_luy_ke_theo_tinh
    FROM fact_sales;
    """
    
    run_query(query_1)
    run_query(query_2)
    run_query(query_3)

    # =========================================================================
    # ⚔️ THỬ THÁCH THỰC CHIẾN (CHALLENGES)
    # Nhiệm vụ của anh: Viết câu lệnh SQL hoàn chỉnh để giải quyết các bài toán sau.
    # =========================================================================

    # --- [CHALLENGE 1]: Xếp hạng các tỉnh trong từng quý theo tổng doanh số.
    # Gợi ý: 
    # Bước 1: Dùng GROUP BY tinh_id, quy để tính tổng doanh số của từng tỉnh theo quý.
    # Bước 2: Dùng CTE (WITH) kết hợp DENSE_RANK() để xếp hạng.
    
    challenge_1 = """
    -- Viết SQL của anh ở đây:
    with ds as (select tinh_id, quy, sum(doanh_so) as tong_doanh_so_theo_quy
    from fact_sales
    group by tinh_id, quy)
    
    select *,
    dense_rank() over(partition by quy order by tong_doanh_so_theo_quy desc) as rank 
    from ds  
    """ 

    # --- [CHALLENGE 2]: Lọc ra tỉnh đứng ĐẦU (Top 1) doanh số của mỗi quý.
    # Gợi ý: Dựa trên kết quả xếp hạng của Challenge 1, dùng lọc WHERE rank = 1.
    
    challenge_2 = """
    -- Viết SQL của anh ở đây:
    with ds as 
    (select tinh_id, quy, sum(doanh_so) as tong_doanh_so_theo_quy
    from fact_sales
    group by tinh_id, quy),
    ds_2 as (select *,
    dense_rank() over(partition by quy order by tong_doanh_so_theo_quy desc) as rank 
    from ds)
    select * from ds_2 where rank=1
    """

    # --- [CHALLENGE 3]: Tính tỷ lệ tăng trưởng doanh số của từng tỉnh so với quý trước.
    # Gợi ý: 
    # Bước 1: Tính tổng doanh số của từng tỉnh theo quý.
    # Bước 2: Dùng LAG() để lấy tổng doanh số quý trước đặt cạnh tổng doanh số quý này.
    # Bước 3: Áp dụng công thức tính tăng trưởng: ((nay - truoc) / truoc) * 100
    
    challenge_3 = """
    -- Viết SQL của anh ở đây:
    with ds_3 as (select tinh_id, quy, sum(doanh_so) as tong_doanh_so_tinh_theo_quy
    from fact_sales
    group by tinh_id, quy),
    ds_4 as (select tinh_id, quy, tong_doanh_so_tinh_theo_quy, 
    lag (tong_doanh_so_tinh_theo_quy, 1, null) over (partition by tinh_id order by quy) as Doanh_so_quy_truoc
    from ds_3)
    
    select *, 
    ((tong_doanh_so_tinh_theo_quy-Doanh_so_quy_truoc)/Doanh_so_quy_truoc)*100 as ty_le_tang_truong_doanh_so
    from ds_4 
    """

    # --- Chạy thử thách (Mở comment bên dưới khi anh làm xong) ---
    print("\n" + "#"*40 + " CHẠY THỬ THÁCH " + "#"*40)
    run_query(challenge_1)
    run_query(challenge_2)
    run_query(challenge_3)


