# Hands-on Linux-08 : Shell Scripting Temelleri

Bu uygulamalı eğitimin amacı, öğrencilere shellde nasıl script yazılacağını öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler;

- shell script dosyası yazmanın temellerini açıklar.

- Shell değişkenlerini açıklar.

- basit aritmetik işlemler yapar.

## Outline

- Bölüm 1 - Shell Scripting Temelleri

- Bölüm 2 - Shell Değişkenleri

- Bölüm 3 - Temel Aritmetik İşlemler

## Bölüm 1 - Shell Scripting Temelleri

- Bir klasör oluşturun ve adını shell-scripting koyun.

```bash
mkdir shell-scripting && cd shell-scripting
```

- 'basic.sh' adında bir 'komut dosyası' dosyası oluşturun. Tüm komut dosyalarının .sh uzantısına sahip olacağını unutmayın.

```bash
#!/bin/bash
echo "Hello World"
```

- Scriptimize başka bir şey eklemeden önce, sistemi bir shell scriptinin başlatıldığı konusunda uyarmamız gerekiyor.
Bu, ilk satırda `#!/bin/bash` belirtilerek yapılır; bu, scriptin başka bir shell yerine her zaman bash ile çalıştırılması gerektiği anlamına gelir. `#!`, `shebang` olarak adlandırılır çünkü `#` sembolüne hash denir ve `!` sembolüne de bang denir.

- Yukarıdaki içeriği kaydettikten sonra scripti çalıştırılabilir hale getirmemiz gerekiyor.

```bash
chmod +x basic.sh
```

- Daha sonra 'basic.sh'yi çalıştırabiliriz. Basic.sh'yi çalıştırmak için `basic.sh` dosyasının başına `./` eklenmesi gerekir. `./` geçerli çalışma dizinindeki bir şeyi çağırdığımız anlamına gelir. $PATH değişkenimizin dışındalarsa yürütülebilir dosyalar için yolu belirtmemiz gerekir.

```bash
./basic.sh
```

- Diğer shell komutlarını da scriptimize ekleyebiliriz.

```bash
#!/bin/bash
echo "hello"
date
pwd
ls
```

- Ve tekrar yürütün.

```bash
./basic.sh
```

### Shell Yorumları

- Bash, satırda `(#)' hash işaretinden sonra yazılan her şeyi yok sayar. Bu kuralın tek istisnası scriptin `#!` karakterleriyle başlayan ilk satırıdır.

- Yorumlar satırın başına veya diğer kodlarla birlikte satır içine eklenebilir. 'Basic.sh'yi güncelleyelim.

```bash
#!/bin/bash
echo "hello"
# date
pwd # This is an inline comment
# ls
```

- Çoğu programlama dilinin aksine Bash, çok satırlı yorumları desteklemez. Ancak bunun için 'here document' komutunu kullanabiliriz. Linux'ta, buradaki belge (genellikle 'heredoc' olarak da anılır), bir komuta yönlendirilecek çok satırlı dizeleri içeren özel bir kod bloğunu ifade eder. 'HereDoc bloğu' bir komuta yönlendirilmezse, çok satırlı yorumlar yer tutucusu olarak görev yapabilir.

### HEREDOC syntax

- Heredoc, **<<** `(yönlendirme operatörü)` ve ardından bir sınırlayıcı jetondan oluşur. Sınırlayıcı belirtecinden sonra içeriği oluşturacak dize satırları tanımlanabilir. Son olarak, sınırlayıcı jeton, sonlandırma görevi görecek şekilde sona yerleştirilir. Sınırlayıcı belirteci, içerikte görünmeyecek kadar benzersiz olduğu sürece herhangi bir değer olabilir.

- HereDoc'u nasıl kullanacağımızı görelim.

```bash
cat << EOF
Welcome to the Linux Lessons.
This lesson is about the shell scripting
EOF
```

- basic.sh` dosyasını güncelleyin.

```bash
#!/bin/bash
echo "hello"
# date
pwd # This is an inline comment
# ls

cat << EOF
Welcome to the Linux Lessons.
This lesson is about the shell scripting
EOF

<< multiline-comment
pwd
ls
Everything inside the
HereDoc body is
a multiline comment
multiline-comment
```

- basic.sh dosyasını çalıştırın.

```bash
./basic.sh
```

## Bölüm 2 - Shell Değişkenleri

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

- ?, `*` veya `-` gibi diğer karakterleri kullanamamamızın nedeni, bu karakterlerin shell için özel bir anlamı olmasıdır.

- Yeni bir dosya oluşturun ve adını `variable.sh` koyun.

```bash
#!/bin/bash
NAME=Joe
echo $NAME
```

- Komut dosyasını çalıştırılabilir hale getirin ve ardından çalıştırın.

```bash
chmod +x variable.sh && ./variable.sh
```

### Komut Yerine Geçme

- Komut Yerine Geçme, bir komutun veya programın çıktısını (genellikle ekrana yazılır) alıp bir değişkenin değeri olarak kaydetmemizi sağlar. Bunu yapmak için komutu parantez içine alırız ve ardından $ sembolü gelir.

```bash
content=$(ls)
echo $content
```

- ya da `(backtick) kullanabiliriz

```bash
content=`ls`
echo $content
```

- bunu bir scriptte görelim. Bir dosya oluşturun ve adını `command-substitution.sh` koyun.

```bash
#!/bin/bash
working_directory=$(pwd)
echo "Welcome, your working directory is $working_directory."
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın. 

```bash
chmod +x command-substitution.sh
./command-substitution.sh
```

- Aynı sonucu değişkenleri kullanmadan da elde edebiliriz. `Command-substitution.sh` dosyasını aşağıdaki gibi güncelleyin.

```bash
#!/bin/bash
echo "Welcome, your working directory is $(pwd)."
echo "Today is `date`"
echo "You are `whoami`"
```

- Ve uygulayın.

```bash
./command-substitution.sh
```

### Console input(Konsol girişi)

- Bash 'read' komutu, kullanıcı girişi almak için kullanılan güçlü bir yerleşik yardımcı programdır.

- 'variable.sh' dosyasını güncelleyin.

```bash
#!/bin/bash
echo "Enter your name: "
read NAME
echo "Welcome $NAME"
```

- Ve uygulayın.

```bash
./variable.sh
```

- Etkileşimli bash scriptleri yazarken, kullanıcı girdisini almak için read komutunu kullanabiliriz. Bir bilgi istemi dizesi belirtmek için -p seçeneğini kullanın. Bilgi istemi, read yürütülmeden önce yazdırılır ve yeni satır içermez.

```bash
read -p "Enter your name: " NAME
echo "Welcome $NAME"
```

- Hassas bilgileri girerken gelen girdiyi görüntülemek istemeyiz. Bunun için `read -s` kullanabiliriz

```bash
read -p "Enter your name: " NAME
echo "Welcome $NAME"

read -s -p "Enter your password: " PASSWORD
echo -e "\nYour password is $PASSWORD"
```

- echo -e: echo komutu, metin veya değişken değerlerini terminale yazdırmak için kullanılır. -e seçeneği, kaçış dizilerini (escape sequences) yorumlamasını sağlar. Kaçış dizileri, genellikle özel karakterlerin veya komutların yazdırılması için kullanılır. Örneğin, \n yeni bir satır ekler.

- \n: Bu kaçış dizisi yeni bir satır ekler. echo -e ile kullanıldığında, metnin başına bir satır ekleyecektir.


### Command Line Arguments

- Komut satırı argümanları, İşletim Sistemlerinin komut satırı kabuğunda programın adından sonra verilir. Komut satırı argümanları $1, $2, $3, ...$9 konumsal parametrelerdir; $0 gerçek komutu, programı, kabuk betiğini veya işlevi ve $1, $2, $3, ...$9 komutun argümanlarını gösterir.

- Yeni bir dosya oluşturun ve adını `argument.sh` koyun.

```bash
#!/bin/bash
echo "File Name is $0"
echo "First Parameter is $1"
echo "Second Parameter is $2"
echo "Third Parameter is $3"
echo "All the Parameters are $@"
echo "Total Number of Parameters : $#"
echo "$RANDOM is a random number"
echo "The current line number is $LINENO"
```

- Komut dosyasını çalıştırılabilir hale getirin. 

```bash
chmod +x argument.sh
```

- Aşağıdaki komut ile çalıştırın.

```bash
./argument.sh Joe Matt Timothy James Guile
```

### Arrays(diziler)

- Programlarımızda, genellikle tek bir değer olarak işlemek için birkaç değeri gruplandırmamız gerekir. Shell'de diziler aynı anda birden fazla değeri tutabilir.

#### Defining arrays(dizileri tanımlama)

- Aşağıda bir dizi değişkeni oluşturmanın en basit yöntemi verilmiştir. 

```bash
DISTROS[0]="ubuntu"
DISTROS[1]="fedora"
DISTROS[2]="debian"
DISTROS[3]="centos"
DISTROS[4]="alpine"
```

- Aşağıdaki yöntemi de kullanabiliriz.

```bash
devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")
```

#### Dizilerle çalışma

- Bir dizi içindeki bir değere aşağıdaki yöntemi kullanarak erişebiliriz.

```bash
echo ${DISTROS[0]}
echo ${DISTROS[1]}
```

- Sayı yerine `@` koyarak tüm elemanlara erişebiliriz.

```bash
echo ${DISTROS[@]}
```

- Aşağıdaki yöntemle eleman sayısını öğrenebiliriz.

```bash
echo ${#DISTROS[@]}
```

## Bölüm 3 - Temel Aritmetik İşlemler

- Bash komut dosyasında aritmetik ifadeleri değerlendirmenin birçok yolu vardır.

### expr

- `expr` komutu ifadenin değerini standart çıktıya yazdırır. Bunu görelim.

```bash
expr 3 + 5
expr 6 - 2
expr 7 \* 3
expr 9 / 3
expr 7 % 2
```

- `expr` komutunu kullanırken, ifadenin öğeleri arasında boşluk bırakmalı ve ifadenin etrafına tırnak işareti koymamalıyız. Bunu yaparsak, ifade değerlendirilmeyecek, bunun yerine yazdırılacaktır. Aradaki farkı görün.

```bash
expr "3 + 5"
expr 3-2
```

- Basit bir hesap makinesi oluşturalım. Bir dosya oluşturun ve adını `calculator.sh` koyun.

- Scripti çalıştırılabilir hale getirin. 

```bash
chmod +x calculator.sh
```

```bash
#!/bin/bash
read -p "Input first number: " first_number
read -p "Input second number: " second_number

echo "SUM="`expr $first_number + $second_number`
echo "SUB="`expr $first_number - $second_number`
echo "MUL="`expr $first_number \* $second_number`
echo "DIV="`expr $first_number / $second_number`
```

> Komut Satırı Argümanları ile nasıl yapabiliriz?

### let

- let` Bash'in basit aritmetik işlemleri yapmamıza yardımcı olan yerleşik bir fonksiyonudur. Cevabı yazdırmak yerine sonucu bir değişkene kaydetmesi dışında `expr`ye benzer. `expr`den farklı olarak ifadeyi tırnak içine almamız gerekir. 

```bash
let "sum = 3 + 5"
echo $sum
```

- İfadenin etrafına tırnak işareti koymazsak, boşluk bırakmadan yazılması gerektiğini unutmayın.

```bash
let sub=8-4
echo $sub
```

- Ayrıca `let` fonksiyonu ile değişkeni 1 artırabilir veya azaltabiliriz. Bunu görelim.

```bash
x=5
let ++x
echo $x

y=3
let y--
echo $y
```

- Bir dosya oluşturun ve adını `let-calculator.sh` koyun.

```bash
#!/bin/bash
read -p "Input first number: " first_number
read -p "Input second number: " second_number

let "sum = $first_number + $second_number"
let "sub = $first_number - $second_number"
let "mul = $first_number * $second_number"
let "div = $first_number / $second_number"
echo "SUM=$sum"
echo "SUB=$sub"
echo "MUL=$mul"
echo "DIV=$div"

let first_number++
let second_number--
echo "The increment of first number is $first_number"
echo "The decrement of second number is $second_number"
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın. 

```bash
chmod +x let-calculator.sh
./let-calculator.sh
```

#### `num++` and `++num`, or `num--` and `--num` (Aralarındaki farklar)

- Bir dosya oluşturun ve adını number.sh koyun.

```bash
number=10
let new_number=number++   # Bu ilk olarak sayıyı atar ve sonra artırır.
echo "Number = $number"
echo "New number = $new_number"

number=10
let new_number=--number   # Bu, önce sayıyı azaltır, ardından atama yapar.
echo "Number = $number"
echo "New number = $new_number"
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın. 

```bash
chmod +x number.sh
./number.sh
```

### Double Parentheses

- Aritmetik ifadeleri çift parantezle de değerlendirebiliriz. Bir komutun çıktısını alabileceğimizi ve bunu bir değişkenin değeri olarak kaydedebileceğimizi öğrendik. Bu yöntemi temel aritmetik işlemleri yapmak için kullanabiliriz.

```bash
sum=$((3 + 5))
echo $sum
```

- Aşağıda görebileceğimiz gibi, aralıkları kaldırırsak da aynı şekilde çalışır.

```bash
sum=$((3+5))
echo $sum
```

- Bir dosya oluşturun ve adını `parantheses-calculator.sh` koyun.

```bash
#!/bin/bash
read -p "Input first number: " first_number
read -p "Input second number: " second_number

sum=$(($first_number + $second_number)) 
sub=$(($first_number - $second_number)) 
mul=$(($first_number * $second_number)) 
div=$(($first_number / $second_number)) 


echo "SUM=$sum"
echo "SUB=$sub"
echo "MUL=$mul"
echo "DIV=$div"

(( first_number++ ))
(( second_number-- ))

echo "The increment of first number is $first_number"
echo "The decrement of second number is $second_number"
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın. 

```bash
chmod +x parantheses-calculator.sh
./parantheses-calculator.sh
```
