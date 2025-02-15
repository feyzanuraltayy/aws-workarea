# Hands-on Linux-04 : Linux'ta Paket Yöneticilerini Kullanma
​
Bu uygulamalı eğitimin amacı, öğrencilere Linux'ta paket yöneticilerinin nasıl kullanılacağını öğretmektir.
​
## Öğrenme Çıktıları
​
Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- Paket yönetiminin ne olduğunu açıklayın.

- En yaygın paket yönetim araçlarıyla çalışın.

- Paket yönetim araçlarını kullanarak yazılım paketlerini kurun, yükseltin, yapılandırın ve kaldırın.
​
## Anahatlar
​
- Bölüm 1 - Paket yöneticilerini kullanma ('yum' ve 'apt') 
​
## - Bölüm 1 - Paket yöneticilerini kullanma ('yum' ve 'apt') 
​
- Amazon Linux Instance Güncelleyin.
​
```bash
sudo yum update
```
- Ubuntu'nun paket listesini güncelleyin. Bu komut yerel depo veritabanını günceller ancak herhangi bir paket yüklemez.
​
```bash
sudo apt update
```
- Paketleri yükseltin. Bu komut listelenen mevcut paketleri yükler.

```bash
sudo apt upgrade
```

- Amazon Linux instance da 'git' yüklü olup olmadığını kontrol edin..
​
```bash
git --version
```
- Ubuntu örneğinde 'git' yüklü olup olmadığını kontrol edin.
​
```bash
git --version
```
- Amazon Linux instance'ına git yükleyin.
​
```bash
sudo yum install git
```
- Amazon Linux instance'ında git'i kaldırın.
​
```bash
sudo yum remove git
```
- Amazon Linux instance'ına git'i herhangi bir kesinti olmadan yükleyin.
​
```bash
sudo yum install git -y
```
- Amazon Linux instance'ında git'i herhangi bir kesinti olmadan kaldırın.
​
```bash
sudo yum remove git -y
```
- Amazon Linux instance'ında yüklü git sürümünü kontrol edin. (Bilgi olmamalı, çünkü bir dakika önce kaldırıldı)

```bash
git --version
```
- Neden hala sürüm bilgisi olduğunu açıklayın.
- Amazon Linux instance'ına git'i herhangi bir kesinti olmadan yükleyin.
​
```bash
sudo yum install git -y
```
- Amazon Linux instance'ında git'i bağımlılıklarla birlikte herhangi bir kesinti olmadan kaldırın.
​
```bash
sudo yum autoremove git -y
```
- Amazon Linux instance'ında yüklü git sürümünü kontrol edin. (Bilgi olmamalı, çünkü bir dakika önce kaldırıldı)
​
```bash
git --version
```
- Ubuntu instance'ında git'i kaldırın.
​
```bash
sudo apt remove git
```
- Ubuntu instance'ında yüklü git sürümünü kontrol edin (Bilgi olmamalı, çünkü bir dakika önce kaldırıldı)
​
```bash
git --version
```
- Ubuntu instance'ına git'i herhangi bir kesinti olmadan yükleyin.
​
```bash
sudo apt install git -y
```
- Ubuntu instance'ında git'i bağımlılıklarıyla birlikte herhangi bir kesinti olmadan kaldırın.
​
```bash
sudo apt autoremove git -y
```
- Amazon Linux instance'ında yüklü git paketi için bilgileri kontrol edin.
​
```bash
sudo yum info git
```
- Ubuntu instance'ında yüklü git paketi için bilgileri kontrol edin.
​
```bash
sudo apt info git
```
-  Amazon Linux instance için mevcut tüm paketleri listeleyin.
​
```bash
sudo yum list
```
- Ubuntu instance'ı için mevcut tüm paketleri listeleyin.
​
```bash
sudo apt list
```
- Amazon Linux instance'ı için mevcut tüm git paketlerini listeleyin.
​
```bash
sudo yum list git
```
- Ubuntu instance'ı için mevcut tüm git paketlerini listeler.
​
```bash
sudo apt list git
```
- Amazon Linux instance'ında yüklü tüm paketleri listeleyin.
​
```bash
sudo yum list installed
```
- Ubuntu instance'ında kurulu tüm paketleri listeler.
​
```bash
sudo apt list --installed
```
- Amazon Linux instance'ında git paketlerinin mevcut tüm sürümlerini listeleyin.
​
```bash
sudo yum --showduplicates list git
```
- Amazon Linux instance'ında yüklü git sürümünü kontrol edin.
​
```bash
git --version
```
-  Amazon Linux instance'ında git'i bağımlılıklarla birlikte herhangi bir kesinti olmadan kaldırın.
​
```bash
sudo yum autoremove git -y
```
- Amazon Linux instance'ına git'in önceki bir sürümünü yükleyin.
​
```bash
sudo yum --showduplicates list git
sudo yum install git-2.39.1-1.amzn2023.0.2 -y
```
- Amazon Linux instance'ında yüklü git sürümünü kontrol edin.
​
```bash
git --version
```
- Amazon Linux instance'ında git paketlerinin mevcut tüm sürümlerini listeleyin.
​
```bash
sudo yum --showduplicates list git
``` 
- info komutu ile git'in mevcut sürümünü kontrol edin.
​
```bash
sudo yum info git
```
- git'i güncelleyin ve sürümü kontrol edin.
​
```bash
sudo yum update git -y
git --version
```
