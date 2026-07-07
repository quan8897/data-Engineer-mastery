#!/bin/bash

# --- CỘT TRỤ 1: FAIL-SAFE MẠNH NHẤT ---
# Dừng script ngay khi có lỗi, có biến rỗng, hoặc lỗi trong đường ống (pipe)
set -euo pipefail

# --- KHAI BÁO BIẾN CỐT LÕI ---
INGESTION_DIR="${HOME}/data/ingestion"
LOG_FILE="${HOME}/cleanup.log"
RETENTION_DAYS=30
DRY_RUN=${DRY_RUN:-1} # Mặc định là 1 (Chạy ngầm/Dry-run) để bảo hiểm.

# --- CỘT TRỤ 2: BẮT TÍN HIỆU NGẮT (BẢO VỆ RÁC TRONG QUÁ TRÌNH XÓA) ---
trap 'echo "[CRITICAL] HỆ THỐNG BỊ NGẮT ĐỘT NGỘT! KIỂM TRA LẠI INGESTION_DIR" | tee -a "$LOG_FILE"; exit 1' SIGINT SIGTERM

echo "===========================================" | tee -a "$LOG_FILE"
echo "[$(date '+%Y-%m-%dT%H:%M:%S')] BẮT ĐẦU CHẠY CLEANUP SCRIPT (Quy mô: 63 Tỉnh Thành)" | tee -a "$LOG_FILE"
echo "===========================================" | tee -a "$LOG_FILE"

# --- CỘT TRỤ 3: TƯ DUY TỰ ĐỘNG HÓA QUA VÒNG LẶP ---
# Quét từng thư mục tỉnh thành (VD: /data/ingestion/hanoi, /data/ingestion/hcm...)
for PROVINCE_PATH in "${INGESTION_DIR}"/*; do
    
    # Kiểm tra xem nó có thực sự là một THƯ MỤC không (Bỏ qua nếu nó là file vớ vẩn)
    if [ ! -d "$PROVINCE_PATH" ]; then
        continue
    fi
    
    PROVINCE_NAME=$(basename "$PROVINCE_PATH")
    ARCHIVE_DIR="${PROVINCE_PATH}/archive"

    # KIỂM TRA MỨC ĐỘ TỒN TẠI (Nếu tỉnh này chưa có thư mục archive, bỏ qua)
    if [ ! -d "$ARCHIVE_DIR" ]; then
        echo "[WARNING] Tỉnh $PROVINCE_NAME chưa có ARCHIVE_DIR. Bỏ qua..." | tee -a "$LOG_FILE"
        continue
    fi
    
    echo "[$(date '+%Y-%m-%dT%H:%M:%S')] [INFO] Đang quét dọn cho tỉnh: $PROVINCE_NAME" | tee -a "$LOG_FILE"

    if [ "$DRY_RUN" -eq 1 ]; then
        echo "[$(date '+%Y-%m-%dT%H:%M:%S')] [DRY-RUN] Chỉ liệt kê, KHÔNG xóa:" | tee -a "$LOG_FILE"
        
        # --- NHIỆM VỤ 1: ĐIỀN THAM SỐ TÌM KIẾM THEO NGÀY VÀ LỌC THEO TẬP TIN ---
        # Làm sao để KHÔNG tìm thư mục mà CHỈ tìm TẬP TIN (file)?
        # Làm sao để tìm các tập tin CŨ HƠN tuổi thọ biến $RETENTION_DAYS?
        find "$ARCHIVE_DIR" -type f -mtime +${RETENTION_DAYS} | while read -r file; do
            echo "  Sẽ xóa: $file" | tee -a "$LOG_FILE"
        done

    else
        echo "[$(date '+%Y-%m-%dT%H:%M:%S')][PRODUCTION] ĐANG XÓA THẬT. Cảnh báo cấp Đỏ!" | tee -a "$LOG_FILE"
        
        # --- NHIỆM VỤ 2: ĐIỀN LỆNH DỌN DẸP AN TOÀN ---
        # Khi đã tìm đúng file rồi, lệnh xóa nào đi kèm với dấu cộng (+) để gom nhóm tối ưu tài nguyên?
        find "$ARCHIVE_DIR" -type f -mtime +${RETENTION_DAYS} -exec rm -vf {} + | tee -a "$LOG_FILE"
        
    fi

done

echo "[$(date '+%Y-%m-%dT%H:%M:%S')] HOÀN TẤT DỌN DẸP." | tee -a "$LOG_FILE"
