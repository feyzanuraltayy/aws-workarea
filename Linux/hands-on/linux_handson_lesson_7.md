# Hands-on Linux-07 : Filters and Control Operators
​
Bu uygulamalı eğitimin amacı, öğrencilere Linux'ta filtrelerin ve kontrol operatörlerinin nasıl kullanılacağını öğretmektir.
​
## Öğrenme Çıktıları
​
Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- Filtre komutlarını kullanın.

- Pipe komutları.

- Sed komutunu kullanın

- Kontrol operatörlerini kullanın.
​
## Anahatlar
​
- Bölüm 1 - Filtreleri Kullanma

- Bölüm 2 - Sed komutu

- Bölüm 3 - Kontrol Operatörlerini Kullanma
​
## Bölüm 1 - Filtreleri Kullanma
​
**cat**

- dosyaları birleştirir ve standart çıktıya yazdırır

- Bir klasör oluşturun ve adını filters koyun.
​
```bash
mkdir filters
cd filters
```
- `days.txt` adında bir `text` dosyası oluşturun.
​
```bash
vim days.txt
```
​
```bash
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
- days.txt dosyasının içeriğini görüntüleyin.
```bash
cat days.txt
```
- Bir pipe içinde kullanıldığında cat komutunun ne yaptığını gösterin.
​
```bash
cat days.txt | cat | cat | cat | cat
```
- `count.txt` adında bir `text` dosyası oluşturun.
​
```bash
vim count.txt
```
```text
one
two
three
four
five
six
seven
eight
nine
ten
eleven 
```
- count.txt dosyasının içeriğini görüntüleyin.

```bash
cat count.txt
```

**tee**

- Standart girişten okuma ve standart çıkışa ve dosyalara yazma

- count.txt dosyasının içeriğini ters sırada temp.txt adlı başka bir dosyaya yazın ve temp.txt'nin içeriğini ters sırada görüntüleyin.

```bash
tac count.txt | tee temp.txt | tac
```
- temp.txt dosyasının oluşturulup oluşturulmadığını kontrol edin ve içeriği görüntüleyin.
​
```bash
ls
cat temp.txt
```

**grep**
​
- Kalıplarla eşleşen satırları yazdırır. grep'in en yaygın kullanımı, belirli bir dizeyi içeren (veya içermeyen) metin satırlarını filtrelemektir.

- tennis.txt` adında bir `text` dosyası oluşturun.
​
```bash
cat > tennis.txt
​
Amelie Mauresmo, Fra
Justine Henin, BEL
Serena Williams, USA
Venus Williams, USA
```
>**press ctrl+d for EOF**
​
- tennis.txt içeriğini görüntüleyin.

```bash
cat tennis.txt
```

- tennis.txt dosyasında yalnızca 'Williams' içeren satırları görüntüleyin.
​
```bash
cat tennis.txt | grep Williams
```

- tennis.txt dosyasında yalnızca 'us' içeren satırları görüntüleyin.
​
```bash
cat tennis.txt | grep us
```

​
**cut**

- Cut filtresi, bir sınırlayıcıya veya bayt sayısına bağlı olarak dosyalardan sütun seçebilir
​
- Geçerli dizindeki tüm dosyaların sahipler sütununu (3. sütun) görüntüleyin.

```bash
ls -l | cut -d' ' -f3
```

- etc/passwd dizininin içeriğini görüntüler.
​
```bash
cat /etc/passwd
```

- Yalnızca kullanıcı adlarını görüntüleyin.
​
```bash
cut -d: -f1 /etc/passwd
```

**tr**
​
- 'tr' komutu 'translate' anlamına gelir. Küçük harften büyük harfe veya tam tersine ya da yeni satırları boşluklara çevirmek için kullanılır.

- techproeducation.txt` adında bir `text` dosyası oluşturun.
​
```bash
cat << EOF > techproeducation.txt
Take a career voyage with us.
EOF
```

- techproeducation.txt dosyasının içeriğini görüntüleyin.
​
```bash
cat techproeducation.txt
```

- techproeducation.txt dosyasının içeriğinde 'aer' harflerini 'QAZ' ile değiştirin veya çevirin.
​
```bash
cat techproeducation.txt | tr aer QAZ
```
​
- count.txt dosyasının içeriğini aynı satıra yazın.
​
```bash
cat count.txt | tr '\n' ' '
```
​
- techproeducation.txt dosyasının içeriğindeki tüm sesli harfleri silin.
​
```bash
cat techproeducation.txt | tr -d aeiou
```
​
- techproeducation.txt dosyasının tüm içeriğini büyük harflerle yazın.
​
```bash
cat techproeducation.txt | tr [a-z] [A-Z]
```

**wc**
​
- Her dosya için satır, kelime ve karakterleri yazdırın.

- count.txt dosyasının içeriğindeki satırları, kelimeleri ve harfleri sayın.
​
```bash

wc count.txt
```

- Bilgisayarda kaç kullanıcı olduğunu bulun.

```bash
wc -l /etc/passwd
```

**sort**
​
- Sıralama filtresi varsayılan olarak alfabetik sıralama yapacaktır. 

- marks.txt` adında bir `text` dosyası oluşturun.
​
```bash
cat << EOF > marks.txt
aaron   70
julia   80
albert  90
james   60
kate    60
john    80
oliver  75
tom     54
victor  30
walter  60
jane    100
EOF
```

marks.txt dosyasının içeriğini görüntüleyin.
​
```bash
cat marks.txt
```

- marks.txt içeriğini sıralayın.
​
```bash
sort marks.txt
```

- marks.txt içeriğini ters sırada sıralayın.
​
```bash
sort -r marks.txt
```

**uniq**
​
- tekrarlanan satırları raporlar veya atlar. uniq komutu yardımıyla, her kelimenin yalnızca bir kez geçeceği sıralı bir liste oluşturabilirsiniz.

- Trainees.txt` adında bir `text` dosyası oluşturun.
​
```bash
cat << EOF > trainees.txt
john
james
aaron
oliver
walter
albert
james
john
travis
mike
aaron
thomas
daniel
john
aaron
oliver
mike
john
EOF
```

- Trainees.txt dosyasının içeriğini görüntüleyin.
​
```bash
cat trainees.txt
```

- Trainees.txt içeriğinde yalnızca benzersiz adları görüntüleyin.
​
****** uniq komutunu kullanmadan önce dosya sıralanmalıdır******
​
```bash
sort trainees.txt | uniq
```

**comm**

- Sıralanmış iki dosyayı satır satır karşılaştırır. Varsayılan olarak, `comm` her zaman üç sütun görüntüleyecektir. 
İlk sütun ilk dosyanın eşleşmeyen öğelerini gösterir, ikinci sütun eşleşmeyen öğeleri gösterir 
ve üçüncü sütun her iki dosyanın eşleşen öğelerini gösterir. 

- 'comm' komutunun çalıştırılabilmesi için her iki dosyanın da sıralı olması gerekir.

- file1.txt` adında bir `metin` dosyası oluşturun.
​
```bash
cat << EOF > file1.txt
Aaron
Bill
James
John
Oliver
Walter
EOF
```

- file2.txt` adında başka bir `metin` dosyası oluşturun.
​
```bash
cat << EOF > file2.txt
Guile
James
John
Raymond
EOF
```

- Compare file1.txt and file2.txt.
​
****** comm komutunu kullanmadan önce dosyalar sıralanmalıdır******
​
```bash
comm file1.txt file2.txt
```

## Bölüm 2 - sed komutu

- Sed bir akış düzenleyicisidir. Bir akış düzenleyici, bir dosya üzerinde arama, bulma ve değiştirme, ekleme veya silme gibi birçok işlevi gerçekleştirmek için kullanılır.

- Bir klasör oluşturun ve adını `sed-command` koyun.

```bash
cd ~
mkdir sed-command && cd sed-command
```

- sed.txt adında bir dosya oluşturun. 

```txt
Linux is an OS. Linux is life. Linux is a concept.
I like linux. You like linux. Everyone likes linux.
Linux is free. Linux is good. Linux is hope.
```

### Dizeyi değiştirme veya yerine koyma

Aşağıdaki sed komutu dosyadaki "linux" kelimesini "ubuntu" ile değiştirir.

```bash
sed 's/linux/ubuntu/' sed.txt
```
- `s` değiştirme işlemini belirtir. 
- `/` sınırlayıcılardır. 
- 'Linux' arama modelidir ve 'ubuntu' değiştirme dizesidir.

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like linux. Everyone likes linux.
Linux is free. Linux is good. Linux is hope.
```
> sed komutunun varsayılan olarak her satırda kalıbın `ilk geçtiği yeri` değiştirdiğine dikkat edin.

### Bir satırdaki herhangi bir desen oluşumunu değiştirme

Bir desenin satırdaki ilk, ikinci oluşumunu değiştirmek için /1, /2 vb bayraklarını kullanın. Aşağıdaki komut, “linux” sözcüğünün bir satırdaki üçüncü kullanımını “ubuntu” ile değiştirir.

```bash
sed 's/linux/ubuntu/3' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like linux. You like linux. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

### Büyük/küçük harf ayrımlarını göz ardı ederek bir dizeyi değiştirme.

Varsayılan olarak sed komutu büyük/küçük harf ayrımını göz ardı etmez. Bunun için `i` kalıbı kullanılabilir.

```bash
sed 's/linux/ubuntu/i' sed.txt
```

**Output:**
```bash
ubuntu is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like linux. Everyone likes linux.
ubuntu is free. Linux is good. Linux is hope.
```

#### Bir satırdaki desenin tüm oluşumlarını değiştirme 

g bayrağı` (global değiştirme) sed komutunu satırdaki dizenin tüm geçtiği yerleri değiştirecek şekilde tanımlar.

```bash
sed 's/linux/ubuntu/g' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

- Aynı şeyi büyük/küçük harf ayrımlarını göz ardı ederek de yapabiliriz. `i` ve `/g` kombinasyonunu kullanın.

```bash
sed 's/linux/ubuntu/ig' sed.txt
```

**Output:**
```bash
ubuntu is an OS. ubuntu is life. ubuntu is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
ubuntu is free. ubuntu is good. ubuntu is hope.
```

#### Bir satırdaki herhangi bir oluşumdan tüm oluşumlara değiştirme

- /1, /2 vb. ve /g kombinasyonunu kullanarak bir satırda herhangi bir desen oluşumundan itibaren tüm desenleri değiştirebiliriz. Aşağıdaki sed komutu, bir satırdaki ikinci, üçüncü ve benzeri “linux” kelimesini “ubuntu” kelimesiyle değiştirir.

```bash
sed 's/linux/ubuntu/2ig' sed.txt
```

**Output:**
```bash
Linux is an OS. ubuntu is life. ubuntu is a concept.
I like linux. You like ubuntu. Everyone likes ubuntu.
Linux is free. ubuntu is good. ubuntu is hope.
```

#### Belirli bir satır numarasındaki dizeyi değiştirme

- Belirli bir satır numarasındaki dizeyi değiştirmek için sed komutunu sınırlayabiliriz. Aşağıdaki komut sadece ikinci satırı değiştirir.

```bash
sed '2 s/linux/ubuntu/ig' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

#### Belirli bir satır numarasındaki dizeyi silme

- Aşağıdaki komut ikinci satırı siler.

```bash
sed '2d' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
Linux is free. Linux is good. Linux is hope.
```
####  sed komutu ile doğrudan dosyayı değiştirme.

- Aşağıdaki sed komutu dosyadaki "linux" kelimesini "ubuntu" ile kalıcı olarak dosyada değiştirir.

```bash
sed -i 's/linux/ubuntu/g' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

## Bölüm 3 - Kontrol Operatörlerini Kullanma
​
>**;**
​
- Birden fazla komut `;` ile tek bir satırda kullanılabilir.

- ; kullanarak aynı satırda iki ayrı cat komutu yazın.
​
```bash
cd ../filters
cat days.txt ; cat count.txt 
```

```bash
echo Hello ; echo World! 
```

>**&**

- Bir satır & işareti ile bittiğinde, shell komutun bitmesini beklemeyecektir. Shell komut isteminizi geri alırsınız ve komut arka planda yürütülür. Bu komut arka planda yürütülmeyi bitirdiğinde bir mesaj alırsınız.

- sleep 10 komutunu çalıştırın ve bu komutun işlemi bitene kadar çekirdeğin meşgul olduğunu gösterin.
​
```bash
sleep  10
```

- sleep 20 komutunu çalıştırın ve siz diğer komutları çalıştırırken bu komutun arkada çalışmasına izin verin.
​
```bash
sleep  20 &
ls -l
cat count.txt
cat days.txt
```

>**$?**
​
- Bu kontrol operatörü son çalıştırılan komutun durumunu kontrol etmek için kullanılır. Eğer durum '0' gösteriyorsa komut başarılı bir şekilde yürütülmüştür ve eğer '1' gösteriyorsa komut başarısız olmuştur.

- ls komutunu çalıştırın ve başarıyla yürütüldüğünü gösterin.
​
```bash
ls
echo $?
```

- lss komutunu çalıştırın ve başarısız olduğunu gösterin.
​
```bash
lss
echo $?
```

Exit Code | Meaning |
|:-------:|---------|
|1| Genel hataları yakalayın
|2| Kabuk yapılarının yanlış kullanımı
|126| Çağrılan komut yürütülemiyor
|127| Komut bulunamadı
|128| Çıkış için geçersiz bağımsız değişken
|128+n| Önemli hata sinyali "n"
|255| Çıkış durumu aralık dışında (çıkış yalnızca 0 - 255 aralığındaki tamsayı bağımsız değişkenleri alır)

>**&&**

- Komut kabuğu &&'yi mantıksal AND olarak yorumlar. Bu komutu kullanırken, ikinci komut yalnızca ilki başarıyla yürütüldüğünde yürütülecektir.
​
- Days.txt dosyasını görüntüleyin ve düzgün çalışıyorsa count.txt dosyasını görüntüleyin.
​
```bash
cat days.txt && cat count.txt
```

- days.text dosyasını görüntüleyin ve düzgün çalışıyorsa count.txt dosyasını görüntüleyin.
​
```bash
cat days.text && cat count.txt
```

>**||**

- Komut kabuğu (||) karakterini mantıksal "VEYA" olarak yorumlar. Bu mantıksal 'VE'nin tersidir. İkinci komutun yalnızca ilk komut başarısız olduğunda yürütüleceği anlamına gelir.
​
- Days.txt dosyasını görüntüleyin veya ekrana 'techproeducation' yazın, ardından 'one' yazın.
​
```bash
cat days.txt || echo techproeducation ; echo one
```

- Write 'first' or write 'second' on the screen, then write 'third'.
​
```bash
echo first || echo second ; echo third
zecho first || echo second ; echo third
```

>**&& and ||**

- Komut satırına if-then-else yapısını yazmak için bu mantıksal VE ve mantıksal VEYA'yı kullanabiliriz. Bu örnek, rm komutunun başarılı olup olmadığını görüntülemek için echo'yu kullanır.
​
- file1.txt dosyasının bir kopyasını oluşturun ve onu file11.txt olarak adlandırın.
​
```bash
cp file1.txt file11.txt
```
- file11.txt dosyasını silin ve düzgün silinmişse bir mesaj yazın.
​
```bash
rm file11.txt && echo 'it worked' || echo 'it failed'
```
- Son komutu tekrar çalıştırın.
​
```bash
rm file11.txt && echo 'it worked' || echo 'it failed'
```

>**#**

- Bir pound işaretinden (#) sonra yazılan her şey kabuk tarafından dikkate alınmaz. Bu, bir kabuk yorumu yazmak için kullanışlıdır ancak komutun yürütülmesi veya kabuk genişletilmesi üzerinde hiçbir etkisi yoktur.​

- echo komutunu çalıştırın ve bir yorum satırı ekleyin.
​
```bash
echo '# is the comment sign' # echo command displays the string comes after it.
echo # is the comment sign
echo \# is the comment sign
```

>** \ **

- Ters eğik çizgiyle biten satırlar bir sonraki satırda devam eder. Kabuk, yeni satır karakterini yorumlamaz ve ters eğik çizgi olmayan bir yeni satırla karşılaşılıncaya kadar kabuğun genişletilmesini ve komut satırının yürütülmesini bekleyecektir.

- Escape karakterler, kabuk genişletmede kontrol karakterlerinin kullanımını sağlamak için kullanılır, ancak bu karakterler kabuk tarafından yorumlanmaz.
​
- Birden fazla satırda tek bir komut çalıştırın.
​
```bash
echo this command is written \
not only on a single line \
but also on multiple lines.
```
- Ekrana aşağıdaki cümleyi yazın: Özel karakterler *, \, ", #, $, ''dir.
​
```bash
echo The special characters are \*, \\, \", \#, \$, \'.
```
