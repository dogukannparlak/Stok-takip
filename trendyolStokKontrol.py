import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    #burdaki bilgiler değişebilir ilerleyen zamanlarda kontrol ederek çalıştırın
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_name = soup.find('h1', class_='pr-new-br').text.strip()

    product_price_elem = soup.find('span', class_='prc-dsc')
    if product_price_elem:
        product_price = product_price_elem.text.strip()
    else:
        product_price = 'Fiyat bilgisi bulunamadı.'

    availability = soup.find('div', class_='notice-alarm')
    if availability:
        stock_status = 'Stokta Yok'
    else:
        stock_status = 'Stokta Var'

    return product_name, product_price, stock_status


def send_email(product_name):
    # E-posta ayarları
    sender_email = ""
    receiver_email = ""
    password = "" #SMTP şifresi nasıl alabileceğiniz readme dosyasında yazıyor

    # E-posta gövdesi
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Trendyol Ürün Bildirimi" #Email başlığı

    body = f"Aradığın, {product_name} ürünü tekrar  stokta  " #Email mesajı

    message.attach(MIMEText(body, "plain"))

    # SMTP oturumu başlatma
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def track_product(url, interval):
    last_stock_status = None
    while True:
        product_name, product_price, stock_status = get_product_info(url)
        print(f"Ürün Adı: {product_name}")
        print(f"Fiyat: {product_price}")
        print(f"Stok Durumu: {stock_status}")
        print("=" * 50)

        if stock_status != last_stock_status and stock_status == "Stokta Yok":
            send_email(product_name)

        last_stock_status = None  #eğer sadece 1 email almak istiyor spam olarak gelmesini istemiyorsanız last_stock_status = stock_status olarak güncelleyin
        time.sleep(interval)


if __name__ == "__main__":
    product_url = '' #Ürünün urlsi buraya gelecek
    check_interval_seconds = 10 # ürün stoğunu kontrol etme süresi sn
    track_product(product_url, check_interval_seconds)
