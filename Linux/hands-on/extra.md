# Hands-on awk command and crontab(wget, curl, tar and unzip command)

Bu uygulamalı eğitimin amacı, öğrencilere awk komutunun ve crontab'ın nasıl kullanılacağını öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- awk, wget, curl, tar ve unzip komutlarını ve crontab'ı kullanabileceklerdir.

## Anahatlar

- Bölüm 1 - awk komutu

- Bölüm 2 - crontab

- Bölüm 3 - ping, ssh, wget, curl, tar and unzip komutları


## Bölüm 1 - awk komutu

- Awk, Aho, Weinberger & Kernighan (adı da buradan gelmektedir) tarafından oluşturulan bir metin deseni tarama ve işleme dilidir. Belirtilen kalıplarla eşleşen çizgiler içerip içermediğini görmek için bir veya daha fazla dosyayı arar ve ardından ilgili eylemleri gerçekleştirir.

- Sed programı karakter tabanlı işlemeyle iyi çalışırken, awk programı sınırlandırılmış alan işlemeyle iyi çalışır.

- 'awk.txt' adında bir dosya oluşturun. 

```txt
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### awk komutunun sözdizimi

> awk options 'selection _criteria {action }' file

- Varsayılan olarak Awk, belirtilen dosyadaki her veri satırını yazdırır.

```bash
awk '{print}' awk.txt
```

**Output:**
```bash
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### Verilen kalıpla eşleşen satırları yazdırır

```bash
awk '/This/ {print}' awk.txt
```

**Output:**
```bash
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### Bir Satırı Alanlara Bölme

Varsayılan olarak, awk komutu bir boşluk karakteri ile sınırlandırılmış kaydı böler.  Awk her veri alanı için aşağıdaki gibi bazı değişkenler atar:

$0Tüm satır için.
$1 ilk alan için.
$2 İkinci alan için.
$n n'inci alan için.

```bash
awk '{print $2}' awk.txt
```

**Output:**
```bash
is
is
is
is
is
```

Daha fazla alan görüntüleyebiliriz. Aşağıdaki örnekte sadece iki alan görüntülenmektedir.

```bash
awk '{print $2,$4}' awk.txt
```

**Output:**
```bash
is 1
is 2
is 3
is 4
is 5
```

- F seçeneğini kullanarak sınırlayıcıyı değiştirebiliriz. Öncelikle awk.txt dosyasını aşağıdaki gibi güncelleyin.

```txt
This is part 1 of line 1 : This is part 2 of line 1
This is part 1 of line 2 : This is part 2 of line 2
This is part 1 of line 3 : This is part 2 of line 3
This is part 1 of line 4 : This is part 2 of line 4
This is part 1 of line 5 : This is part 2 of line 5
```

- Alanları `:` ile ayıralım.

```bash
awk -F: '{print $2}' awk.txt
```

**Output:**
```bash
 This is part 2 of line 1
 This is part 2 of line 2
 This is part 2 of line 3
 This is part 2 of line 4
 This is part 2 of line 5
```

- Filtre olarak awk komutunu kullanabiliriz. 

```bash
ls -l | awk '{print $9}'
```

**Output:**
```bash
awk.txt
sed.txt
```

- Belirli bir sütundaki herhangi bir dizeyi bulabiliriz. 

```bash
awk '{ if($7 == "3") print $0;}' awk.txt
```

**Output:**
```bash
This is part 1 of line 3 : This is part 2 of line 3
```

## - Bölüm 2 - crontab

- Crontab, `cron table` anlamına gelir ve sistemde düzenli zaman aralıklarında çalışması planlanan komutların bir listesidir. 

- Linux üzerinde herhangi bir görevi zamanlamamız gerekirse, temel olarak crontab dosyasını düzenlemeliyiz. Bunu aşağıdaki komutu kullanarak yapabiliriz.

```bash
crontab -e              # crontab dosyasını düzenleyin
crontab -l              # geçerli cron görevlerini listele
crontab -u username -e  # diğer kullanıcıların crontab dosyasını düzenleme
```

- Crontab dosyasını düzenlemek karmaşık değildir ancak öncelikle o dosyada 5* kullanarak tarih ve saati nasıl ayarlayacağımızı öğrenmeliyiz. Her cron görev satırında kullandığımız altı alan vardır. Bunlar aşağıdaki resimde ayrıntılı olarak açıklanmıştır.

![crontab format](./crontab-format.png)

- Birkaç örnek görelim;

```bash
* * * * * <shell command>   # cron işini her dakika yürüt
0 1 * * * <shell command>   # cron işini her gün saat 1'de çalıştırın.
* * 1 * * <shell command>   # Ocak ayının her dakikasını değerlendirin
* * * * 6 <shell command>   # her cumartesi̇ günü her daki̇ka çalişin
0 1/15 * jan,jun mon,fri <command> # ocak ve hazi̇ran aylarinda her pazartesi̇ ve cuma günleri̇ saat 13.00 ve 15.00'te uygulanacaktir
```

- Tarih kısmını tanımlamak için bazı düzenli ifadeler de kullanabiliriz.

```bash
* = Herhangi bir/Tüm değerler           # e.g. *
- = Değer aralığı                        # e.g. 1-5 
, = Çoklu/Değerler listesi  # e.g. 1,2,3
/ = Adım değerleri              # e.g. 1/3
```

- Son olarak bazı crontab görevleri oluşturalım. Her gün saat 1'de sistem tarih bilgisini date.log dosyasına yazan bir cron görevi oluşturun.

```bash
crontab -e
0 13 * * * date >> /home/ec2-user/date.log
```

- Her Pazar saat 3'te sunucumuzu güncelleyen ve yükselten bir cron görevi oluşturun.

```bash
0 3 * * sun sudo yum update -y
```

-  Cron görevlerini listeleyin.

```bash
crontab -l
```


## Bölüm 3 - ping, ssh, wget, curl, tar and unzip komutları

## ping Komutu:

- Ping veya Packet Internet Groper, bir kaynak ve hedef cihaz arasındaki bağlantı durumunu kontrol etmek için kullanılan bir ağ yönetimi yardımcı programıdır.

Örnek:

```bash
ping 8.8.8.8
```
## ssh Komutu:

- ssh "Secure Shell" anlamına gelir.
  * Uzak bir sunucuya/sisteme güvenli bir şekilde bağlanmak için kullanılan bir protokoldür.

Örnek:

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

## Curl Komutu Dosya Seçenekleri

- Curl komutları uzak bir konumdan dosyaları indirebilir.
Örnek:

```bash
curl -O https://example.com/dosya.zip
```

- Bu komut, belirtilen URL'den "dosya.zip" adlı dosyayı indirir.

```bash
curl -SL https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
- Bu komut, Docker Compose'ın belirli bir sürümünü (v2.24.7) indirip /usr/local/bin/docker-compose konumuna kaydeder.

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

```bash
tar -xzvf my_dizin.tar.gz
```
- Bu komut, my_dizin.tar.gz adlı sıkıştırılmış dosyayı açar ve içindeki dosyaları çıkarır.

```bash
mkdir tarfolder
tar -xzvf my_dizin.tar.gz -C /home/ec2-user/tarfolder
```

## unzip Komutu:

- unzip, ZIP formatındaki dosyaları açmak için kullanılır.

Örnek:

```bash
unzip terraform_1.4.6_linux_amd64.zip -d /usr/local/bin
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