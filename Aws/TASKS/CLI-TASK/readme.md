### **AWS CLI Task: S3 ile Statik Web Site Hosting

#### **Görevler:**

1. **AWS CLI Kurulumu ve Yapılandırma:**
   - AWS CLI'yi bilgisayarınıza kurun.
   - `aws configure` komutunu kullanarak AWS kimlik bilgilerinizi (Access Key, Secret Key, bölge ve çıktı formatı) yapılandırın.

2. **S3 Bucket Oluşturma:**
   - Web sitesi için yeni bir S3 bucket oluşturun. Bucket adı, global olarak benzersiz olmalıdır.

3. **Web Sitesi Dosyalarını Hazırlama:**
   - Lokal bilgisayarınızda bir klasör oluşturun ve web sitesi dosyalarını (HTML, CSS, JS, resimler vb.) bu klasöre ekleyin.
   - Örnek bir `index.html` dosyası oluşturun.

4. **Dosyaları S3 Bucket'ına Yükleme:**
   - Web sitesi dosyalarını S3 bucket'ına yükleyin.

5. **S3 Bucket'ını Web Sitesi Hosting için Yapılandırma:**
   - Bucket'ı statik web sitesi hosting için yapılandırın.

6. **Bucket Politikasını Ayarlama (Herkese Açık Erişim):**
   - Web sitesine herkesin erişebilmesi için bucket politikasını güncelleyin. JSON formatında bir politika dosyası oluşturun ve bu politikayı bucket'a uygulayın.

7. **Web Sitesine Erişim:**
   - Web sitesine erişmek için S3 web site endpoint URL'sini kullanın.

8. **Temizlik (Opsiyonel):**
   - Web sitesini test ettikten sonra bucket'ı silin.


NOT: Bütün bu işlemler Aws cli ile yapılacaktır...