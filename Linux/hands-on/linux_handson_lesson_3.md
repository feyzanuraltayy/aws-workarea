# Hands-on Linux-03 : Linux'ta Dosyaları Yönetme

Bu uygulamalı eğitimin amacı, öğrencilere Linux'ta dosyaların nasıl yönetileceğini öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- Text Editörlerle çalışma.

- Dosya oluşturma ve düzenleme.

- Dosya içerikleri ile çalışma

- Dosyaları ara.

## Anahatlar

- Bölüm 1 - Text Editörlerle Çalışma

- Bölüm 2 - Dosya İçeriği ile Çalışma

- Bölüm 3 - Dosya Arama

## Bölüm 1: Text Editörlerle Çalışma

PS1="\[\e[1;32m\]\u@\h:\[\e[1;34m\]\w\[\e[m\]\$"

## Nano Kullanımı

### Adım 1: Nano'yu Açma
Terminali açın ve aşağıdaki komutu girerek `test.txt` adında bir dosya oluşturup açın:
```sh
nano test.txt
```

### Adım 2: Nano İçinde Metin Yazma
Açılan editörde istediğiniz metni yazın. Örneğin:
```sh
Bu bir test dosyasıdır.
Nano ile metin düzenlemek oldukça kolaydır.
```

### Adım 3: Dosyayı Kaydetme
Dosyayı kaydetmek için `Ctrl + O` tuşlarına basın.
Dosya adını onaylamak için `Enter` tuşuna basın.

### Adım 4: Nano'dan Çıkma
Editörden çıkmak için `Ctrl + X` tuşlarına basın.

## Vim Kullanımı

### Adım 1: Vim'i Açma
Terminali açın ve aşağıdaki komutu girerek `test.txt` adında bir dosya oluşturup açın:
```sh
vim test.txt
```

### Adım 2: Insert Moduna Geçme
Vim başlangıçta komut modunda açılır. Metin ekleyebilmek için `i` tuşuna basarak insert moduna geçin.

### Adım 3: Metin Yazma
Insert modunda iken istediğiniz metni yazın. Örneğin:
```sh
Bu bir test dosyasıdır.
Vim ile metin düzenlemek oldukça esnektir.
```

### Adım 4: Normal Moda Geçme ve Dosyayı Kaydetme
Normal moda geri dönmek için `Esc` tuşuna basın.
Dosyayı kaydetmek ve çıkmak için `:wq` yazın ve `Enter` tuşuna basın.

### Adım 5: Diğer Temel Komutlar
- **Dosyayı kaydetme:** `:w`
- **Çıkış:** `:q`
- **Kaydetmeden çıkış:** `:q!`

## Bölüm 2 - Dosya İçeriği ile Çalışma


- Bir klasör oluşturun ve linux-lessons olarak adlandırın.

```bash
mkdir linux-lessons
cd linux-lessons
```

- `techproeducation.txt` adında bir `text` dosyası oluşturun.

```txt
Welcome to the linux lessons
line 2
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12
line 13
line 14
Line 15
```

- techproeducation.txt dosyasının ilk 10 satırını gösterin.

```bash
head techproeducation.txt
```

- techproeducation.txt dosyasının ilk 5 satırını gösterin.

```bash
head -5 techproeducation.txt
```

- techproeducation.txt dosyasının son 10 satırını göster.

```bash
tail techproeducation.txt
```

- techproeducation.txt dosyasının son 5 satırını göster.

```bash
tail -5 techproeducation.txt
```

- Ekranda techproeducation.txt dosyasını görüntüleyin.

```bash
cat techproeducation.txt
```

- echo komutu ile üç dosya oluşturun ve file1 file2 file3 olarak adlandırın.

```bash
echo "this is file1" > file1
echo "this is file2" > file2
echo "this is file3" > file3
```

- file1, file2 ve file3 dosyalarını ekranda görüntüleyin.

```bash
cat file1 file2 file3
```

- file1, file2 ve file3 dosyalarını `all.txt` dosyasında birleştirin.

```bash
cat file1 file2 file3 > all.txt
```

- `cat` komutu ile bir dosya oluşturun.

```bash
cat > summer.txt 
```
- Dosyaya aşağıdaki içeriği yazın.

Today is cold.
Today is rainy


- Son satırdan sonra, Control (Ctrl) tuşunu basılı tutun ve d tuşuna basın.

- Cat ile dosyanın içeriğini görüntüleyin.
```bash
cat summer.txt 
```

- techproeducation.txt dosyasını `more` komutu ile görüntüleyin.

```bash
more techproeducation.txt
```

- techproeducation.txt dosyasını `less` komutu ile görüntüleyin.

```bash
less techproeducation.txt
```

- More ve less arasındaki temel fark, less komutunun daha hızlı olmasıdır çünkü tüm dosyayı bir kerede yüklemez ve sayfa yukarı/aşağı tuşlarını kullanarak dosyada gezinmeye izin verir. (shell dönmek için q ya basın)

- techproeducation.txt dosyasını tersten görüntüleyin.

```bash
tac techproeducation.txt
```

- techproeducation.txt dosyasının tersi olarak reverse-techproeducation.txt dosyasını oluşturun.

```bash
tac techproeducation.txt > reverse-techproeducation.txt
```

- Cat ile `reverse-techproeducation.txt` dosyasının içeriğini görüntüleyin.

```bash
cat reverse-techproeducation.txt
```

## Bölüm 3 - Dosya Arama

### `find` command

- Geçerli çalışma dizininde adı techproeducation.txt olan tüm dosyaları bulun.

```bash
find . -name techproeducation.txt
```

- techproeducation.txt adıyla /home dizini altındaki tüm dosyaları bulun.

```bash
find /home -name techproeducation.txt
```

- Adı techproeducation.txt olan ve /home dizininde hem büyük hem de küçük harfler içeren tüm dosyaları bulun.

```bash
find /home -iname techproeducation.txt
```

- Adı linux-lessons olan tüm dizinleri /home dizini içinde bulun.

```bash
find /home -type d -name linux-lessons
```

- Çalışma dizinindeki tüm txt dosyalarını bulun.

```bash
find . -type f -name "*.txt"
```

- Çalışma dizinindeki tüm boş dosyaları bulun.

```bash
find . -type f -empty
```

- /home dizinindeki tüm boş dosyaları bulun.

```bash
find /home -type f -empty
```

- Home dizini altındaki tüm 100MB dosyaları bulmak için. 

```bash
find /home -size 100M
```

- Home dizini altında 50MB'den büyük ve 100MB'den küçük olan tüm dosyaları bulun. +` ve `-` öneklerinin daha büyük ve daha küçük anlamına geldiğini unutmayın.

```bash
find /home -size +50M -size -100M
```

- /home dizininde 10 gün önce değiştirilen tüm dosyaları bulun.

```bash
find /home -mtime 10
```

- Son 10 gün içinde /home dizininde değiştirilen tüm dosyaları bulun.

```bash
find /home -mtime -10
```

- /home dizininde 10 günden daha uzun bir süre içinde değiştirilen tüm dosyaları bulun.

```bash
find /home -mtime +10
```

- Geçerli klasörde 10 dakikadan daha uzun süre önce ve 30 dakikadan daha kısa süre önce değiştirilmiş tüm dosyaları bulun.

```bash
find . -mmin +10 -mmin -30
```

### `grep` command

Grep, belirtilen bir dosyada bir karakter dizisini aramak için kullanılan bir Linux / Unix komut satırı aracıdır.

- Bir dosya oluşturun ve adını `grep.txt` koyun.

```txt
grep  searches  for  PATTERNS  in  each  FILE.
PATTERNS  is  one  or more patterns separated by newline characters, and grep prints each line that matches a pattern.  
Typically PATTERNS should be  quoted  when grep is used in a shell command.
```

- Başka bir dosya oluşturun ve `linux.txt` olarak adlandırın

```txt
Linux is a family of open-source Unix-like operating systems based on the Linux kernel.
It is an operating system kernel first released on September 17, 1991, by Linus Torvalds.Linux is typically packaged in a Linux distribution.
Distributions include the Linux kernel and supporting system software and libraries.
Popular Linux distributions include Debian, Fedora, and Ubuntu. 
Commercial distributions include Red Hat Enterprise Linux and SUSE Linux Enterprise Server.
```

- `Linux.txt` dosyasında `kernel` ifadesini arayın. 

```bash
grep "kernel" linux.txt
```

- Tüm dosyalarda `is` ifadesi için arama yapın.

```bash
grep  "is" *
```

- `linux.txt` dosyasında `linux` ifadesi için arama yapın.

```bash
grep "linux" linux.txt
```

- Linux ifadesini bulamadı. Çünkü grep büyük/küçük harfe duyarlıdır. Şimdi aşağıdaki komut ile deneyin.

```bash
grep -i "linux" linux.txt
```

- `Linux.txt` dosyasında `ker` sözcüğünü arayın.

```bash
grep -i "ker" linux.txt
```

- Şimdi aşağıdaki komutla `linux.txt` dosyasında `ker` sözcüğünü arayın.

```bash
grep -w "ker" linux.txt
```

- `ker`ı bulamadı. Grep sadece `-w` bayrağı ile tüm kelimeleri bulmanızı ve sonuçları yazdırmanızı sağlar. Aşağıdaki komut ile deneyelim.

```bash
grep -w "kernel" linux.txt
```

- Belirtilen arama kalıbı ile eşleşmeyen satırları -v seçeneğini kullanarak görüntüleyebiliriz. 

```bash
grep -v "kernel" linux.txt
```

- `^` düzenli ifade kalıbı bir satırın başlangıcını belirtir. Bu, verilen dize veya kalıpla başlayan satırları eşleştirmek için grep'te kullanılabilir. 

```bash
grep "^li" techproeducation.txt
```

- `$` düzenli ifade kalıbı bir satırın sonunu belirtir. Bu, verilen dize veya kalıpla biten satırları eşleştirmek için grep'te kullanılabilir.

```bash
grep "kernel.$" linux.txt
```

- Bazen neyin en alakalı olduğuna karar vermek için arama sonuçlarında daha fazla içeriğe ihtiyaç duyarız. Bunun için, istenen satırları bir eşleşmeden önce, sonra veya her ikisini birden eklemek için aşağıdaki operatörleri kullanabiliriz:

    - Bir eşleşmeden sonra görüntülemek için -A ve satır sayısını kullanın.
    
    ```bash
    grep -A3 "line 5" techproeducation.txt # bu komut eşleşmeden sonra üç satır yazdırır.
    ```

    - Bir eşleşmeden önce görüntülemek için -B ve satır sayısını kullanın.
    
    ```bash
    grep -B2 "line 5" techproeducation.txt # bu komut eşleşmeden önce iki satır yazdırır.
    ```

    - Eşleşmeden önce ve sonra görüntülemek için -C ve bir dizi satır kullanın.
    
    ```bash
    grep -C4 "line 5" techproeducation.txt # bu komut eşleşmeden önce ve sonra dört satır yazdırır.
    ```

- Ayrıca `grep` komutunu | ( pipe) ile de kullanabiliriz.

```bash
man pwd | grep "print"
```

```bash
man find | grep -A5 "variable"
```

```bash
info pwd | grep "print"
```

```bash
info pwd | grep -B5 "options"
```

```bash
history | grep "find"
```

  grep "^li" techproeducation.txt
   34  grep "kernel.$" linux.txt
   35   grep -A3 "line 5" techproeducation.txt
   36   grep -B2 "line 5" techproeducation.txt
   37  grep -C4 "line 5" techproeducation.txt
   38  man pwd
   39  info pwd
   40  man pwd
   41  man pwd | grep "print"
   42  history