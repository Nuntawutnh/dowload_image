import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os

# โหลดข้อมูลจาก Excel
df = pd.read_excel('20250616-20250619/การจอดไหล่ทาง-01 Incoorrect.xlsx')  # เปลี่ยนชื่อไฟล์ตามต้องการ

# สร้างโฟลเดอร์สำหรับเก็บภาพ (ถ้ายังไม่มี)
output_folder = '20250616-20250619/ไหล่ทาง_01_incoorect'
os.makedirs(output_folder, exist_ok=True)

# โหลดรูปจาก URL ทีละรูป
for i, row in df.iterrows():
    url = row['Video']  # ชื่อคอลัมน์ใน Excel
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            # ตั้งชื่อไฟล์ตามลำดับ เช่น image_0.jpg
            filename = f'image_{i}.jpg'
            image.save(os.path.join(output_folder, filename))
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download image at row {i}")
    except Exception as e:
        print(f"Error at row {i}: {e}")
