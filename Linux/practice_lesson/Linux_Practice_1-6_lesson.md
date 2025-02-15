# Linux Exercise

## Exercise 1: Temel Komutlar
### Task:
1. Ana dizininizde `linux_practice` adında yeni bir dizin oluşturun.

2. `linux_practice` dizinine gidin.

3. Dizin içerisinde `exercise.txt` adında boş bir dosya oluşturun.

4. Dosyaya bir metin düzenleyici açmadan "Linux is fun!" yazısını ekleyin.

5. `exercise.txt` dosyasının içeriğini terminalde görüntüleyin.

6. Dosyanın adını `linux_fun.txt` olarak değiştirin.

---

## Exercise 2: Paket Yönetimi
### Task:
1. Sistemdeki tüm paketleri güncelleyin.
2. Paket yöneticinizi kullanarak `nginx` paketini yükleyin.
3. `nginx` sürümünü görüntüleyerek kurulumunu doğrulayın.
4. `nginx` paketini kaldırın.

---

## Exercise 3: Kullanıcı ve Grup Yönetimi
### Task:
1. `test_group` adında yeni bir grup oluşturun.
2. `test_user` adında yeni bir kullanıcı oluşturun ve ana dizin olarak `/home/test_user` ayarlayın.
3. `test_user` kullanıcısını `test_group` grubuna ekleyin.
4. `test_user` kullanıcısının  `test_group` grubuna üye olduğunu doğrulayın.
5. `test_user` hesabına geçiş yapın, ana dizini kontrol edin ve grup üyeliklerini doğrulayın.
6. `test_user` kullanıcısını `test_group` grubundan çıkarın.
7. `test_user` kullanıcısını ve ana dizinini silin.
8. `test_group` grubunu silin.

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
8. `env_test` dizininde `sample.txt` adında bir dosya oluşturun ve içine "Linux is powerful." yazısını ekleyin(text editör kullanın).
9. `sample.txt` dosyasının izinlerini şu şekilde ayarlayın:
   - Sahip ve grup tarafından okunabilir, yazılabilir ve çalıştırılabilir.
   - Diğer kullanıcılar tarafından erişilemez.
