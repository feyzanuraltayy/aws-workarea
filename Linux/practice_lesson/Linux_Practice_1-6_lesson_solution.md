# Linux Exercise

## Exercise 1: Temel Komutlar
### Task:
1. Ana dizininizde `linux_practice` adında yeni bir dizin oluşturun.
2. `linux_practice` dizinine gidin.
3. Dizin içerisinde `exercise.txt` adında boş bir dosya oluşturun.
4. Dosyaya bir metin düzenleyici açmadan "Linux is fun!" yazısını ekleyin.
5. `exercise.txt` dosyasının içeriğini terminalde görüntüleyin.
6. Dosyanın adını `linux_fun.txt` olarak değiştirin.

### Solution:
```bash
# Adım 1: Yeni bir dizin oluşturun
mkdir ~/linux_practice

# Adım 2: Dizin içerisine gidin
cd ~/linux_practice

# Adım 3: Boş bir dosya oluşturun
touch exercise.txt

# Adım 4: Dosyaya metin ekleyin
echo "Linux is fun!" > exercise.txt

# Adım 5: Dosya içeriğini görüntüleyin
cat exercise.txt

# Adım 6: Dosya adını değiştirin
mv exercise.txt linux_fun.txt
```

---

## Exercise 2: Paket Yönetimi
### Task:
1. Sistemdeki tüm paketleri güncelleyin.
2. Paket yöneticinizi kullanarak `nginx` paketini yükleyin.
3. `nginx` sürümünü görüntüleyerek kurulumunu doğrulayın.
4. `nginx` paketini kaldırın.

### Solution:
```bash
# Adım 1: Paket indeksini güncelleyin
sudo apt update  # Debian/Ubuntu tabanlı sistemler için
# OR
sudo yum update  # Red Hat/CentOS tabanlı sistemler için

# Adım 2: nginx paketini yükleyin
sudo apt install nginx  # Debian/Ubuntu tabanlı sistemler için
# OR
sudo yum install nginx  # Red Hat/CentOS tabanlı sistemler için

# Adım 3: nginx sürümünü doğrulayın
nginx -version

# Adım 4: nginx paketini kaldırın
sudo apt remove nginx  # Debian/Ubuntu tabanlı sistemler için
# OR
sudo yum remove nginx  # Red Hat/CentOS tabanlı sistemler için
```

---

## Exercise 3: Kullanıcı ve Grup Yönetimi
### Task:
1. `test_group` adında yeni bir grup oluşturun.
2. `test_user` adında yeni bir kullanıcı oluşturun ve ana dizin olarak `/home/test_user` ayarlayın.
3. `test_user` kullanıcısını `test_group` grubuna ekleyin.
4. `test_user` kullanıcısının hem `test_group` hem de `sudo` gruplarına üye olduğunu doğrulayın.
5. `test_user` hesabına geçiş yapın, ana dizini kontrol edin ve grup üyeliklerini doğrulayın.
6. `test_user` kullanıcısını `test_group` grubundan çıkarın.
7. `test_user` kullanıcısını ve ana dizinini silin.
8. `test_group` grubunu silin.

### Solution:
```bash
# Adım 1: Yeni bir grup oluşturun
sudo groupadd test_group

# Adım 2: Yeni bir kullanıcı oluşturun
sudo adduser --home /home/test_user test_user

# Adım 3: Kullanıcıyı gruba ekleyin
sudo usermod -aG test_group test_user

# Adım 4: Kullanıcı grup üyeliklerini doğrulayın
groups test_user

# Adım 5: Kullanıcı hesabına geçiş yapın ve kontrolleri yapın

sudo su - test_user
echo $HOME  # Ana dizini doğrulayın
groups  # Grup üyeliklerini doğrulayın
exit

# Adım 6: Kullanıcıyı gruptan çıkarın
sudo gpasswd -d test_user test_group

# Adım 7: Kullanıcıyı ve ana dizinini silin
sudo userdel -r test_user

# Adım 8: Grubu silin
sudo groupdel test_group
```

---

## Exercise 4: Ortam Değişkenleri, Dosya İzinleri ve Dizinler
### Task:
1. Terminalde tüm ortam değişkenlerini görüntüleyin.
2. `MY_VAR` adında, değeri `LinuxIsGreat` olan bir ortam değişkeni oluşturun ve değerini görüntüleyin.
3. `MY_VAR` değişkenini `.bashrc` dosyasına ekleyerek kalıcı hale getirin.
4. Ana dizininizde `env_test` adında bir dizin oluşturun.
5. `env_test` dizininin yolunu `PATH` ortam değişkenine ekleyin.
6. `env_test` dizini içinde `hello.sh` adında, "Hello, Linux!" yazısını yazdıran bir betik oluşturun.
7. `hello.sh` betiğini çalıştırılabilir hale getirin ve herhangi bir dizinden yalnızca adıyla çalıştırın.
8. `env_test` dizininde `sample.txt` adında bir dosya oluşturun ve içine "Linux is powerful." yazısını ekleyin.
9. `sample.txt` dosyasının izinlerini şu şekilde ayarlayın:
   - Sahip ve grup tarafından okunabilir, yazılabilir ve çalıştırılabilir.
   - Diğer kullanıcılar tarafından erişilemez.

### Solution:
```bash
# Adım 1: Tüm ortam değişkenlerini görüntüleyin
printenv

# Adım 2: Yeni bir ortam değişkeni oluşturun ve değerini görüntüleyin
export MY_VAR="LinuxIsGreat"
echo $MY_VAR

# Adım 3: Değişkeni kalıcı hale getirin
echo 'export MY_VAR="LinuxIsGreat"' >> ~/.bashrc
source ~/.bashrc

# Adım 4: Yeni bir dizin oluşturun
mkdir ~/env_test

# Adım 5: Dizin yolunu PATH değişkenine ekleyin
export PATH=$PATH:~/env_test
echo 'export PATH=$PATH:~/env_test' >> ~/.bashrc
source ~/.bashrc

# Adım 6: Betiği oluşturun
echo '#!/bin/bash' > ~/env_test/hello.sh
echo 'echo "Hello, Linux!"' >> ~/env_test/hello.sh

# Adım 7: Betiği çalıştırılabilir hale getirin
chmod +x ~/env_test/hello.sh

# Herhangi bir dizinden çalıştırın
hello.sh

# Adım 8: Metin dosyasını oluşturun
vim sample.txt
i tuşu ile insert moda geçiş.
sonra editörde -->> ("Linux is powerful.")
esc + :wq

# Adım 9: Dosya izinlerini değiştirin
chmod 770 ~/env_test/sample.txt
```
```