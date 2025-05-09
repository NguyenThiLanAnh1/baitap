# Bài Tập Lớn - Thu thập dữ liệu từ website batdongsan.com.vn
# Giới thiệu
Dự án này được xây dựng nhằm mục tiêu tự động thu thập dữ liệu bất động sản từ website [batdongsan.com.vn](https://batdongsan.com.vn), cụ thể là các bài đăng bán căn hộ chung cư tại quận Sơn Trà, thành phố Đà Nẵng. 
Chương trình sử dụng thư viện Selenium và Undetected ChromeDriver để vượt qua các kiểm tra bot, sau đó trích xuất thông tin.
1. Truy cập vào website Batdongsan
2. Chọn khu vực (VD: Đà Nẵng, Hà Nội, HCM) và loại hình (VD: Căn hộ, đất nền, ...)
3. Lấy toàn bộ thông tin các bài đăng: Tiêu đề, Giá, Diện tích, Địa chỉ, Mô tả
4. Duyệt qua nhiều trang
5. Lưu vào file Excel (.xlsx)
6. Tự động chạy mỗi ngày lúc 6h sáng
Kết quả sẽ được lưu vào file batdongsandanang.xlsx và chương trình được thiết lập tự động chạy vào 6 giờ sáng mỗi ngày bằng thư viện schedule.
# Yêu cầu hệ thống
Để chạy được dự án, bạn cần đảm bảo hệ thống đáp ứng:
- Python 3.7 trở lên
- Google Chrome 
- pip 
# Cài đặt
Làm theo các bước dưới đây để thiết lập môi trường và chạy chương trình:
## 1. Clone repository từ GitHub
Mở terminal hoặc command prompt và chạy:
```bash
git clone https://github.com/NguyenThiLanAnh1/BaiTapLon.git
cd BaiTapLon
## 2. Tạo môi trường ảo (virtual environment)
python -m venv venv
.\venv\Scripts\activate
## 3. Cài đặt thư viện cần thiết
pip install -r requirements.txt
# Cách sử dụng
## 1. Chạy chương trình
python baitap.py
## 2. Lên lịch chạy tự động
Chương trình sử dụng schedule để tự chạy vào lúc 06:00 mỗi ngày 
schedule.every().day.at("06:00").do(batdongsan)
## Cấu trúc thư mục
BaiTapLon/
├── baitap.py                
├── requirements.txt        
└── README.md  
## Các thư viện sử dụng
undetected-chromedriver: tránh bị chặn khi dùng Selenium
selenium: điều khiển trình duyệt web tự động
pandas: xử lý và lưu dữ liệu
schedule: lập lịch tự động thu thập dữ liệu
openpyxl: ghi dữ liệu vào file Excel (.xlsx)   




