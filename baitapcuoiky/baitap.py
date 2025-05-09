# 1. Vào website đã chọn.
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import schedule

def batdongsan():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)

    data = []

    page = 1
    while True:
         # 2. Click chọn bất kì Tỉnh/TP(Hà Nội, Đà Nẵng, Hồ Chí Minh, …). 
        #    Chọn bất kì loại nhà đất(Căn hộ chung cư, nhà, đất, …).
        # 3. Bấm tìm kiếm(nếu trang web tin tức không có Button tìm kiếm thì có thể bỏ qua).
        url = f'https://batdongsan.com.vn/ban-can-ho-chung-cu-son-tra-ddn/p{page}'
        print(f"Đang xử lý trang {page}: {url}")
        driver.get(url)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="product-lists-web"]/div'))
            )
        except:
            print(f"Trang {page} không load được nội dung.")
            break

        posts = driver.find_elements(By.XPATH, '//*[@id="product-lists-web"]/div')
        if not posts:
            print("Không còn bài viết nào, kết thúc.")
            break

        for i in range(1, len(posts)+1):
            try:
                title = ""
                price = ""
                area = ""
                address = ""
                description = ""
                #4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Tên Công ty, Mức lương, Địa điểm) hiển thị ở bài viết.

                title_elements = posts[i-1].find_elements(By.XPATH, './/a/div[2]/div[1]/h3/span')
                if title_elements:
                    title = title_elements[0].text.strip()

                price_elements = posts[i-1].find_elements(By.XPATH, './/a/div[2]/div[1]/div[1]/div[1]/span[1]')
                if price_elements:
                    price = price_elements[0].text.strip()

                area_elements = posts[i-1].find_elements(By.XPATH, './/a/div[2]/div[1]/div[1]/div[1]/span[3]')
                if area_elements:
                    area = area_elements[0].text.strip()

                address_elements = posts[i-1].find_elements(By.XPATH, './/a/div[2]/div[1]/div[1]/div[2]/span[2]')
                if address_elements:
                    address = address_elements[0].text.strip()

                desc_elements = posts[i-1].find_elements(By.XPATH, './/a/div[2]/div[1]/div[2]')
                if desc_elements:
                    description = desc_elements[0].text.strip()

                data.append({
                    'Tiêu đề': title if title else "Không lấy được dữ liệu",
                    'Giá': price if price else "Không lấy được dữ liệu",
                    'Diện tích': area if area else "Không lấy được dữ liệu",
                    'Địa chỉ': address if address else "Không lấy được dữ liệu",
                    'Mô tả': description if description else "Không lấy được dữ liệu"
                })

            except Exception as e:
                print(f"Bỏ qua bài viết thứ {i} trang {page} do lỗi: {e}")
                continue
         # 5. Lấy tất cả dữ liệu của các trang.
        page += 1
        time.sleep(2)

    try:
        driver.quit()
    except Exception as e:
        print(f"Lỗi khi đóng trình duyệt: {e}")
    # 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    df = pd.DataFrame(data)
    df.to_excel("batdongsandanang.xlsx", index=False)
    print("Đã lưu toàn bộ dữ liệu vào: batdongsandanang.xlsx")

# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
schedule.every().day.at("06:00").do(batdongsan)

print("Chương trình đang chạy, chờ đến 6h sáng để thu thập dữ liệu nhé.")

while True:
    schedule.run_pending()
    time.sleep(60)
# 8. Tạo project github chế độ public.
# 9. Viết file README.md hướng dẫn cài đặt cho project github đầy đủ rõ ràng.
# 10. Push(file code, README.md, requirements.txt) lên project và nộp link project github vào classroom.
