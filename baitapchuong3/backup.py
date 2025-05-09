import os 
import shutil
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_FILE = os.path.join(BASE_DIR, "database", "anh.sqlite3")
BACKUP_FOLDER = os.path.join(BASE_DIR, "backup")
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)
def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Gửi mail thành công.")
    except Exception as e:
        print(f"Gửi mail thất bại: {e}")
def backup_database():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.sqlite3"
    backup_path = os.path.join(BACKUP_FOLDER, backup_filename)

    try:
        if not os.path.exists(DB_FILE):
            raise FileNotFoundError(f"Không tìm thấy : {DB_FILE}")
        shutil.copy2(DB_FILE, backup_path)
        print(f"thành công: {backup_path}")
        send_email(
            subject="thành công",
            body=f"Thời gian: {timestamp}\nFile backup: {backup_filename}"
        )

    except Exception as e:
        print(f" lỗi: {e}")
        send_email(
            subject="thất bại",
            body=f"Xảy ra lỗi khi backup:\n{e}"
        )
schedule.every().day.at("10:17").do(backup_database)

print("Chờ thực hiện backup vào 10:14 mỗi ngày...")
while True:
    schedule.run_pending()
    time.sleep(60)
