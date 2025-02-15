# Hands-on ping, ssh, wget, curl, tar and unzip command

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- ping, ssh, wget, curl, tar ve unzip komutlarını kullanabileceklerdir.

## Anahatlar

- Bölüm 1 - ping, ssh, wget, curl, tar and unzip komutları

## Bölüm 1 - ping, ssh, wget, curl, tar and unzip komutları

## ping Komutu:

- Ping veya Packet Internet Groper, bir kaynak ve hedef cihaz arasındaki bağlantı durumunu kontrol etmek için kullanılan bir ağ yönetimi yardımcı programıdır.

Örnek:

```bash
ping 8.8.8.8
```

```bash
ping google.com
```

## ssh Komutu:

- ssh "Secure Shell" anlamına gelir.
  * Uzak bir sunucuya/sisteme güvenli bir şekilde bağlanmak için kullanılan bir protokoldür.

Örnek:

-Yeni bir ubuntu EC2 oluştur ve key dosyasının içeriğini ec2-user da oluştur ve aşağıdaki komutla bağlan.

```bash
ssh -i "firstkey.pem" ec2-user@<public_ip_yada_dns>
```

## wget Komutu:

- GNU Wget, web'den dosya indirmek için kullanılan bir komut satırı yardımcı programıdır. Wget ile HTTP, HTTPS ve FTP protokollerini kullanarak dosya indirebilirsiniz
 
Kullanımı:

wget [option] [url]

Örnek:

```bash
wget https://releases.hashicorp.com/terraform/1.4.6/terraform_1.4.6_linux_amd64.zip
```

- Bu komut, belirtilen URL'den terraform kurulum dosyasını indirir.

wget https://raw.githubusercontent.com/techpro-aws-devops/Todo-List-with-Jenkins-Pipeline/main/Jenkinsfile

## curl Komutu:

-curl, URL'ler üzerinden veri almak veya göndermek için kullanılır. HTTP, HTTPS, FTP ve diğer birçok protokolü destekler. curl ("Client URL "sinin kısaltması) çeşitli ağ protokolleri üzerinden veri aktarımını sağlayan bir komut satırı aracıdır.

Kullanımı:

curl [option] [url]
curl [url] > [local_file]

## Basit Curl Command Sözdizimi

- Curl’ün en basit kullanımı bir sayfanın içeriklerini göstermektir
Örnek:

```bash
curl www.google.com
```

```bash
curl http://example.com
```

## Curl Komutu Dosya Seçenekleri

- Curl komutları uzak bir konumdan dosyaları indirebilir.
Örnek:

```bash
curl -O https://example.com/dosya.zip
```

- Bu komut, belirtilen URL'den "dosya.zip" adlı dosyayı indirir.

```bash
sudo curl -SL https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

- Bu curl komutu, docker-compose aracının belirli bir sürümünü GitHub'dan indirir ve belirli bir dizine kaydeder. -S ve -L seçenekleri ile hata mesajları gösterilir ve HTTP yeniden yönlendirmeleri takip edilir. Sonrasında dosyayı çalıştırılabilir hale getirerek docker-compose komutunu sistemde kullanıma hazır hale getirmiş olursunuz.

## tar Komutu:

- tar, dosyaları bir araya getirme ve sıkıştırma işlemleri için kullanılır. Ayrıca, sıkıştırılmış dosyaları açma işlemlerini gerçekleştirir.

Örnekler:

## Bir dizini sıkıştırmak:

```bash
mkdir my_dizin
echo "Merhaba Dünya" > my_dizin/dosya1.txt
echo "Bu bir örnek" > my_dizin/dosya2.txt
tar -czvf my_dizin.tar.gz my_dizin/
```

- Bu komut, my_dizin adlı dizini sıkıştırarak my_dizin.tar.gz adlı bir sıkıştırılmış dosya oluşturur.


## Sıkıştırılmış bir dosyayı açmak:

- Bu komut, my_dizin.tar.gz adlı sıkıştırılmış dosyayı açar ve içindeki dosyaları belirtilen dizine çıkarır.

```bash
mkdir tarfolder
tar -xzvf my_dizin.tar.gz -C /home/ec2-user/tarfolder
```

## unzip Komutu:

- unzip, ZIP formatındaki dosyaları açmak için kullanılır.

Örnek:

```bash
sudo unzip terraform_1.4.6_linux_amd64.zip -d /usr/local/bin
```

- Bu komut, "terraform_1.4.6_linux_amd64.zip" adlı ZIP dosyasını açar ve içindeki dosyaları çıkarır.

Örnek:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
```

- bu komutlar AWS CLI v2'yi indirir, çıkarır ve sisteminize kurar.


Bu komutlar, dosya indirme, sıkıştırma ve açma işlemlerinde sıklıkla kullanılır. Her komutun daha fazla seçeneği ve kullanımı vardır; bu nedenle, ilgili komutun man sayfasını (man wget, man curl, man tar, man unzip, man ssh, man ping) inceleyerek daha fazla bilgi alabilirsiniz.