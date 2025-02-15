# Instance Termination Finder

Bu proje, Cloudtrail olay geçmişi dosyasını kullanarak belirli bir kullanıcı tarafından sonlandırılan AWS EC2 instance id'lerini bulmak için bir bash script içerir.

## Proje Açıklaması

Bir Finans Şirketinde DevSecOps olarak çalışıyorsunuz. Son zamanlarda, şirket içinde biri tarafından bir instance'ınız sonlandırıldı. Bu instance, firmanın web uygulaması için çok önemliydi ve ayrıca altyapınız da bu sonlandırmadan etkilendi. Takım lideriniz, bekir kullanıcısından şüpheleniyor. Sizden, bekir kullanıcısı tarafından sonlandırılan instance id'lerini bulmanız istendi. Elinizde `log.csv` adlı bir Cloudtrail olay geçmişi dosyası bulunuyor. Bu olay geçmişindeki instance id'leri `i-0c127ab5cdf997cf4` gibi görünüyor. Bu görevleri yerine getirebilmek için bazı filtreleme ve dize manipülasyon komutları uygulamanız gerekiyor. Bu görevleri yerine getirmek amacıyla bir bash script oluşturup, bekir kullanıcısı tarafından sonlandırılan instance id'lerini `result.txt` dosyasına kaydetmeye karar verdiniz.

## Gereksinimler

- Bash shell
- Cloudtrail event history dosyası (`log.csv`)

## Kurulum ve Kullanım

### Adım 1: Script'in Oluşturulması

1. Terminalinizi açın.
2. Aşağıdaki komutu kullanarak bir bash script dosyası oluşturun:
   ```bash
   nano log-script.sh
   ```

3. Aşağıdaki script'i dosyaya yapıştırın ve kaydedin:
   ```bash
   #!/bin/bash

   while true
   do
     read -p 'Please write your file location: ' FILE 
     if [[ $FILE == '' ]]
     then
       echo "Please give a file"
     elif [[ ! -f $FILE ]]
     then
       echo "Please give an existing file"
     else
       break
     fi
   done

   cat $FILE | grep bekir | grep Terminate | grep -Eo "i-[a-zA-Z0-9]{17}" | sort | uniq > /tmp/result.txt 
   echo "Your result is ready under the /tmp/result.txt file"
   ```

### Adım 2: Script'i Çalıştırılabilir Hale Getirme

Script dosyasını çalıştırılabilir hale getirmek için aşağıdaki komutu çalıştırın:
```bash
chmod +x log-script.sh
```

### Adım 3: Script'i Çalıştırma

Script'i çalıştırmak için aşağıdaki komutu kullanın:
```bash
./log-script.sh
```

Script, sizden `log.csv` dosyasının konumunu isteyecek. Dosya konumunu girdikten sonra, `bekir` kullanıcısı tarafından sonlandırılan instance id'lerini `/tmp/result.txt` dosyasına kaydedecektir.

## Örnek Kullanım

Aşağıda, script'in kullanımına dair örnek bir çıktı bulunmaktadır:

```
Please write your file location: /path/to/log.csv
Your result is ready under the /tmp/result.txt file
```

Sonuçlar, `/tmp/result.txt` dosyasında bulunabilir.
