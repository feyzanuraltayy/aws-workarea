# Hands-on Linux-05 : Linux Environment Variables

Bu uygulamalı eğitimin amacı, öğrencilere environment değişkenlerinin nasıl kullanılacağını öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- environment değişkenlerini açıklayabilecektir.

- Değişkenler ile Alıntı yapmayı anlayabileceklerdir.

## Anahatlar

- Bölüm 1 - Environment  Değişkenleri ve Değişkenlere Erişim

- Bölüm 2 - PATH Değişkeni

- Bölüm 3 - Değişkenlerle Alıntı Yapma


## Bölüm 1 - Ortak Environment/Shell Değişkenleri ve Değişkenlere Erişim
​
- Değişkenler iki ana kategoride sınıflandırılabilir: `environment değişkenleri` ve `shell değişkenleri`. 

- Shell değişkenleri geçerli shell örneğinde geçerlidir.

- environment değişkenleri sistem genelinde geçerli olan değişkenlerdir.


### Shell Variables

- Bir değişken gerçek verinin işaretçisidir. Shell değişkenleri oluşturmamızı, atamamızı ve silmemizi sağlar.

- Bir değişkenin adı yalnızca harfler (a'dan z'ye veya A'dan Z'ye), rakamlar (0'dan 9'a) veya alt çizgi karakterini (_) içerebilir ve bir harf veya alt çizgi karakteriyle başlayabilir.

- Aşağıdaki örnekler geçerli değişken adlarıdır.

```bash
KEY=value
_VAR=5
techpro_education=test
```

> Eşittir ( = ) işaretinin her iki tarafında da boşluk olmadığına dikkat edin. 

- Aşağıdaki örnekler geçersizdir.

```bash
3_KEY=value
-VAR=5
techpro-education=test
KEY_1?=value1
```

- ?, `*` veya `-` gibi diğer karakterleri kullanamamamızın nedeni, bu karakterlerin kabuk için özel bir anlamı olmasıdır.

### Environment Variables

- environment değişkenleri, sistemin nasıl çalıştığını ve sistemdeki uygulamaların davranışını özelleştirmenize olanak tanır.

- env veya printenv komutlarını kullanarak tüm environment değişkenlerimizin bir listesini görebiliriz.

```bash
printenv
env
```

#### Difference between "env" and "printenv" commands. 

- İki komut arasındaki fark, `printenv` ile tek tek değişkenlerin değerlerini talep edebilmenizdir:

```bash
printenv HOME
echo $HOME
env HOME
```
​
- Tüm shell değişkenlerinin, environment değişkenlerin ve shell işlevlerinin bir listesini almak için `set` komutunu yazın.

```bash
set
```

- Export` komutu ile bir environment değişkeni oluşturun.

```bash
export ENVVAR=value
env
```
​
- unset komutu ile environment veya shell değişkenini kaldırın.
​
```bash
export ENVVAR=value
env | grep ENVVAR
unset ENVVAR
env | grep ENVVAR
```
​
## Part 2 - Path Variable
​
- PATH variable.
​
```bash
printenv PATH
cd /bin
ls ca*    # cat komutuna bakın.
which ls
```
​
- Bir script çalıştırmak için PATH değişkenine bir yol ekleyin.
​
```bash
cd
mkdir test && cd test
vim script.sh
# echo "hello world" kodunu kopyalayın ve script.sh dosyasına yapıştırın 
chmod +x script.sh
./script.sh
cd    # change directory to ec2-user's home directory
./script.sh    # Çalışmıyor. 
./test/script.sh
printenv PATH
cd test
pwd
export PATH=$PATH:/home/ec2-user/test
printenv PATH
cd
script.sh
cd /
script.sh
```
​
- Script içinde ortam değişkeninin kullanılması.
​
```bash
cd test
export TECHPRO=env.var
EDUCATION=shell.var
vim script2.sh
# kodu kopyalayıp yapıştırın(echo "normalde env. değişkeni $TECHPRO'yu görmeliyiz ama muhtemelen shell değişkeni $EDUCATION'ı göremiyoruz")
chmod +x script2.sh
./script2.sh
```
​
## Part 3 - Quoting with Variables.
​
- Double Quotes.
​
```bash
MYVAR=my value
echo $MYVAR
MYVAR="my value"
echo $MYVAR
MYNAME=james
MYVAR="my name is $MYNAME"
echo $MYVAR
MYNAME="james"
MYVAR="hello $MYNAME"
echo $MYVAR
MYVAR="hello \$MYNAME"
echo $MYVAR
```
​
- Single Quotes.
​
```bash
echo '$SHELL'
echo 'My\$SHELL'
```
​
