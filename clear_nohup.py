import time
import os

file_path = 'nohup.out'  # Đường dẫn tới file nohup.out

while True:
    # Mở file và xóa nội dung
    open(file_path, 'w').close()
    print(f"{file_path} đã được làm rỗng.")
    
    # Chờ 30 phút (30 phút = 1800 giây)
    time.sleep(100)
