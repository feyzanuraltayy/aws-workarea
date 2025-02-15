# Hands-on Linux-06 : Managing Users and Groups

Bu uygulamalı eğitimin amacı, öğrencilere kullanıcıları ve grupları nasıl yöneteceklerini öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- linux'taki kullanıcıları ve grupları açıklayabilecektir.

- Kullanıcıları ve grupları yönetebileceklerdir.

## Anahatlar

- Bölüm 1 - Sudo Komutu

- Bölüm 2 - Temel Kullanıcı Komutları

- Bölüm 3 - Kullanıcı Yönetimi

- Bölüm 4 - Kullanıcı Parolaları

- Bölüm 5 - Grup Yönetimi


## Bölüm 1 - Sudo Komutu.
​
- Sudo Command.
​
```bash
yum update
sudo yum update
cd /
mkdir testfile
sudo su
mkdir testfile
exit
sudo su -
```

## Bölüm 2 - Temel Kullanıcı Komutları
​
- whoami.
​
```bash
whoami
sudo su
pwd
whoami
su ec2-user
sudo su -
pwd
```
​
- who.
​
```bash
exit
who
who # yeni bir shell açın ve giriş yapan kullanıcıları görmek için who komutunu tekrar deneyin.
```
​
- w.
​
```bash
w
who
```
​
- id.
​
```bash
id
id root
sudo su
useradd user1
id user1
```
​
- su.
​
```bash
su ec2-user
su user1
sudo su user1
pwd
exit
sudo su - user1
pwd
```
​
- passwd.
​
```bash
exit
sudo su
useradd user2
passwd user2    # give a password to user2
su - user2
passwd
exit
su user2
```
​
## Bölüm 3 - Kullanıcı Yönetimi
​
- /etc/passwd.
​
```bash
exit
cat /etc/passwd
tail -3 /etc/passwd
```
​
- useradd.
​
```bash
sudo useradd user3
cd /home
ls
cd /etc
ls login*
cat login.defs
sudo vim login.defs    # CREATE_HOME değişkeninin değerini "no" olarak değiştirin
sudo useradd user4
cd /home && ls
cat /etc/passwd
sudo useradd -m user5 # sistemi -m seçeneği ile kullanıcı için bir home dizini oluşturmaya zorlar.
cd /home && ls
sudo useradd -m -d /home/user6home user6    # kullanıcının home dizini adını -d ile değiştirin option.
ls
sudo useradd -m -c "this guy is developer" user7   # kullanıcıya -c seçeneği ile bir açıklama verin.
cat /etc/passwd
cat /etc/passwd | grep user7
```
​
- userdel.
​
```bash
cat /etc/passwd
sudo userdel user5
cat /etc/passwd
cd /home && ls
sudo userdel -r user1    # kullanıcıyı ve home dizinini -r seçeneği ile silin.
cd /home && ls
```
​
- usermod.
​
```bash
cat /etc/passwd
sudo usermod -c "Bu adam bir aws çözüm mimarı olacak" user7
cat /etc/passwd
sudo usermod --help
sudo usermod -l Superuser user2    # user2'nin adını -l seçeneği ile değiştirin.
cat /etc/passwd
```
​
## Bölüm 4 - Kullanıcı Parolaları
​
- passwd-etc/shadow-etc/login.defs.
​
```bash
  sudo su
  useradd user8
  passwd user8
  cd /etc
  cat shadow
  cat login.defs
```
​
## Bölüm 5 - Grup Yönetimi
​
- groups.
​
```bash
groups
sudo groupadd linux
sudo groupadd aws
sudo groupadd python
cat /etc/group
groups
sudo usermod -a -G linux ec2-user    # linux grubuna ec2-user ı ekleyin.
cat /etc/group
groups
sudo su - ec2-user
groups
sudo usermod -G aws ec2-user    # bu komut ec2-user'ın varsayılan grubu hariç ec2-user'ın içinde bulunduğu tüm grupları siler ve ec2-user'ı aws grubuna ekler.
groups ec2-user
cat /etc/group
sudo groupmod -n my-linux linux    # linux grubunun adını değiştirin.
cat /etc/group
groups
cat /etc/group
sudo groupdel python
cat /etc/group
sudo gpasswd -a user7 aws    # bir gruba kullanıcı ekleyin.
cat /etc/group
sudo gpasswd -d user7 aws    # bir gruptaki kullanıcıyı silin.
cat /etc/group
```