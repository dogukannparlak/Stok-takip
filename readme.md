# Trendyol Ürün Bildirimi

Bu program, Trendyol sitesinde belirtilen bir ürünün stok durumunu belirli aralıklarla kontrol eder ve stok durumu değiştiğinde e-posta ile bildirim gönderir.

## Gereksinimler

- Python 3.x
- requests
- BeautifulSoup
- smtplib (Python kütüphaneleri)

## Kurulum

1. Python'u [Python web sitesinden](https://www.python.org/downloads/) indirip yükleyin.
2. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisinde şu komutu çalıştırın:
   ```bash
   pip install requests beautifulsoup4
   ```

## Kullanım

Bu programı kullanmak için aşağıdaki adımları takip edin:

1. **Ürün Bilgilerini Belirleme:** `get_product_info` fonksiyonunda `url` değişkenine izlemek istediğiniz ürünün Trendyol linkini girin.

   Örnek:

   ```python
   url = 'https://www.trendyol.com/...'
   ```

2. **E-posta Ayarlarını Belirleme:** `send_email` fonksiyonunda `sender_email`, `receiver_email` ve `password` değişkenlerine uygun e-posta bilgilerinizi girin. Gmail kullanıyorsanız, SMTP şifresini almak için [buradaki adımları](#google-smtp-şifresini-edinme) takip edin.

   Örnek:

   ```python
   sender_email = "example@gmail.com"
   receiver_email = "recipient@gmail.com"
   password = "your_smtp_password"
   ```

3. **Ürünü Takip Etme:** `track_product` fonksiyonunda `check_interval_seconds` değişkenine stok durumunu kontrol etmek istediğiniz saniye aralığını girin.

   Örnek:

   ```python
   check_interval_seconds = 600  # 10 dakika
   ```

4. **Programı Çalıştırma:** Terminal veya komut istemcisinde `python script_adi.py` komutunu kullanarak programı çalıştırın. Ürünün stok durumu belirtilen aralıklarla kontrol edilecek ve stok durumu değiştiğinde e-posta gönderilecektir.

   Örnek:

   ```bash
   python script_adi.py
   ```

Stok durumu belirtilen aralıklarla kontrol edilecek ve stok durumu değiştiğinde belirlediğiniz e-posta adresine bildirim gönderilecektir.

## Google SMTP Şifresini Edinme

E-posta göndermek için Gmail SMTP sunucusunu kullanıyorsanız ve doğrudan Gmail hesabınızın şifresini kullanmak istemiyorsanız, Gmail'in daha az güvenli uygulamalara erişim izni veren bir SMTP şifresi oluşturabilirsiniz. İşte adımlar:

1. **Google Hesabınızda Güvenlik Ayarlarını Açın:**

   - Tarayıcınızda Gmail'e gidin ve Google hesabınıza giriş yapın.
   - Sağ üst köşede bulunan profil simgesine tıklayın ve "Google Hesabı" seçeneğini seçin.
   - Sol taraftaki menüden "Güvenlik" sekmesine tıklayın.

2. **Daha Az Güvenli Uygulamalara İzin Verme Seçeneğini Etkinleştirin:**

   - "Güvenlik" sekmesinde "Daha az güvenli uygulamalara erişim" başlığını bulun.
   - Bu başlığın yanındaki "Daha Az Güvenli Uygulamalara İzin Ver" seçeneğini etkinleştirin. Bu, Google SMTP şifresini kullanmanızı sağlar.

3. **Google SMTP Şifresini Oluşturma:**
   - Etkinleştirme işleminden sonra, Google SMTP şifrenizi oluşturabilirsiniz. Bu şifre, Gmail hesabınıza doğrudan giriş yapmanıza izin veren bir şifredir.
   - Google SMTP şifresi oluşturmak için [Google Hesap Ayarları](https://myaccount.google.com/security) sayfasına gidin.
   - "Giriş ve güvenlik" bölümüne gidin.
   - "Şifreleriniz" altında, "Uygulama şifreleri" seçeneğini bulun ve bunu tıklayın.
   - Şifre oluşturmak istediğiniz uygulama türünü seçin (örneğin, "Diğer (özel adlar için)").
   - İlgili uygulama için bir isim belirleyin ve "Şifre oluştur" düğmesine tıklayın.
   - Şifreyi kopyalayın veya not alın. Bu oluşturduğunuz şifre, Gmail hesabınızın asıl şifresi değil, sadece SMTP ile erişim için kullanılabilir bir şifredir.
