# Hands-on Linux-09 : Shell Scripting/Conditional Statements

Bu uygulamalı eğitimin amacı, öğrencilere shellde koşullu ifadelerin nasıl kullanılacağını öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- Shell'deki koşullu ifadeleri açıklayabilecektir.

- shell scriptlerinde if deyimlerini kullanabilecek

- shell scriptlerinde case deyimlerini kullanma

## Anahatlar

- Bölüm 1 - If İfadeleri

- Bölüm 2 - If Else İfadeleri

- Bölüm 3 - If Elif Else İfadeleri

- Bölüm 4 - İç İçe If İfadeleri

- Bölüm 5 - Boolean İşlemleri

- Bölüm 6 - Case İfadeleri

## Bölüm 1 - If İfadeleri

- Unix Shell, farklı koşullar temelinde farklı eylemler gerçekleştirmek için kullanılan koşullu deyimleri destekler.

- Basit bir if deyimi temel olarak, belirli bir test doğruysa, belirtilen bir dizi eylemi gerçekleştirin. Eğer doğru değilse, bu eylemleri gerçekleştirmeyin.

- Bir klasör oluşturun ve `conditional-statements` olarak adlandırın.

```bash
mkdir conditional-statements && cd conditional-statements
```

- `if-statement.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash
read -p "Input a number: " number

if [[ $number -gt 50 ]]
then
  echo "The number is big."
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x if-statement.sh
./if-statement.sh
```

- Yukarıdaki if deyiminde köşeli parantezler ( [ ] ) içinde `İlişkisel Operatörler`, `String Operatörleri` veya `Dosya Test Operatörleri` kullanabiliriz. 

### İlişkisel Operatörler

- Bourne Shell, sayısal değerlere özgü olan aşağıdaki ilişkisel operatörleri destekler. Bu operatörler string değerler için çalışmaz.

| Operator | Description |
| -------- | ----------- |
| -eq   | equal                  |
| -ne   | not equal              |
| -gt   | greater than           |
| -lt   | less than              |
| -ge   | greater than or equal  |
| -le   | less than or equal     |

### String Operatörleri

- Aşağıdaki string operatörleri Bourne Shell tarafından desteklenmektedir.

| Operator | Description |
| -------- | ----------- |
| =    | equal            |
| !=   | not equal        |
| -z   | Empty string     |
| -n   | Not empty string |

- Bunu görelim. Bir dosya oluşturun ve adını `string-operators.sh` koyun

```bash
#!/bin/bash

if [[ "a" = "a" ]]
then
  echo "They are same"
fi

if [[ "a" != "b" ]]
then
  echo "They are not same"
fi

if [[ -z "" ]]
then
  echo "It is empty"
fi

if [[ -n "text" ]]
then
  echo "It is not empty"
fi
```

- Açılış parantezi `[` ile "text" = "text" parametreleri arasında ve ardından parametreler ile kapanış parantezi `]` arasında boşluklar olduğuna dikkat edin. Bunun nedeni tam olarak buradaki parantezlerin bir komut görevi görmesi ve komutu parametrelerinden ayırıyor olmanızdır.

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x string-operators.sh
./string-operators.sh
```

### Dosya Test Operatörleri

- Bir Linux dosyasıyla ilişkili çeşitli özellikleri test etmek için kullanılabilecek birkaç operatör vardır.

| Operator | Description |
| -------- | ----------- |
| -d file   | directory  |
| -e file   | exists     |
| -f file   | ordinary file     |
| -r file   | readable          |
| -s file   | size is > 0 bytes |
| -w file   | writable          |
| -x FILE   | executable        |

- Bunu deneyelim. Aşağıdaki dosyaları oluşturun ve yapılandırın.

```bash
mkdir folder
touch file 
chmod 400 file
```

Bir dosya oluşturun ve adını `file-operators.sh` koyun

```bash
#!/bin/bash

if [[ -d folder ]]
then
  echo "folder is a directory"
fi

if [[ -f file ]]
then
  echo "file is an ordinary file"
fi

if [[ -r file ]]
then
  echo "file is a readable file"
fi

if [[ -w file ]]
then
  echo "file is a writable file"
fi

if [[ -s file ]]
then
  echo "file is > 0 bytes"
fi

if [[ -x $0 ]]
then
  echo "$0 is an executable file "
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x file-operators.sh
./file-operators.sh
```

## Bölüm 2 - If Else İfadeleri

- Bazen bir ifade doğruysa bir kod bloğunu, yanlışsa başka bir kod bloğunu çalıştırmak isteriz.

- `ifelse-statement.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash
read -p "Input a number: " number

if [[ $number -ge 10 ]]
then
  echo "The number is bigger than or equal to 10."
else 
  echo "The number is smaller than 10"
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x ifelse-statement.sh
./ifelse-statement.sh
```
# EXAMPLE:1 

> - Bir komut dosyası oluşturun. Kullanıcıdan oluşturmak için `bir dosya adı` girmesini isteyin.
> - Eğer aynı isimde bir dosya varsa, "Dosya zaten var." mesajını yazdırın.
> - Değilse, dosyayı oluşturun ve "Dosya oluşturuldu" mesajını yazdırın.

## Bölüm 3 - If Elif Else İfadeleri

- Programımızda birkaç koşul belirtmek gerektiğinde elif deyimi kullanılır.

- `elif-statement.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash
read -p "Input a number: " number

if [[ $number -eq 10 ]]
then
  echo "The number is equal to 10."
elif [[ $number -gt 10 ]]
then
  echo "The number is bigger than 10"
else 
  echo "The number is smaller than 10"
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x elif-statement.sh
./elif-statement.sh
```

## Bölüm 4 - İç İçe If İfadeleri

- If deyimleri iç içe geçebilir. İç içe geçmiş yapıyı aşağıdaki örnek üzerinde görelim.

- `nested-if-statement.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

read -p "Lütfen bir sayı girin: " sayi

if [ $sayi -gt 0 ]

then
    echo "Girilen sayı pozitif."

    if [ $((sayi % 2)) -eq 0 ]; 
    then
        echo "Ayrıca, girilen sayı çift."
    else
        echo "Ayrıca, girilen sayı tek."
    fi

elif [ $sayi -lt 0 ]; 
then
    echo "Girilen sayı negatif."
else
    echo "Girilen sayı sıfır."
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x nested-if-statement.sh
./nested-if-statement.sh
```

## Bölüm 5 - Boolean İşlemleri

- Aşağıdaki Boolean operatörleri Bourne Shell tarafından desteklenmektedir.

| Operator | Description |
| -------- | ----------- |
| !        | negation    |
| &&       | and         |
| ||       | or          |

- !` doğru bir koşulu yanlışa çevirir veya tam tersini yapar.

- &&` mantıksal AND'dir. İşlenenlerin her ikisi de doğruysa, koşul doğru aksi takdirde yanlış olur.

- `||` mantıksal VEYA'dır. İşlenenlerden biri doğruysa, koşul doğru olur.

- `boolean.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

read -p "Input your name: " name
read -sp "Input your password: " password

if [[ $name = $(whoami) ]] && [[ $password = Aa1234 ]]
then
  echo -e "\nWelcome $(whoami)"
else
  echo -e "\nIt is wrong account"
fi
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x boolean.sh
./boolean.sh
```

# EXAMPLE:2
> -Kullanıcıdan bir dosya adı veya dizin adı girmesini isteyen ve eğer bu isimde bir dosya veya dizin varsa uygun bir mesaj yazdıran yoksa o isimde bir file oluşturan scripti oluşturalım.


## Bölüm 6 - Case İfadeleri

- Çok yönlü bir dallanma yürütmek için birkaç if-elif deyimi kullanabiliriz, ancak bu kısa sürede karmaşık hale gelecektir. Bash case deyimleri if-else deyimlerine benzer ancak daha kolay ve basittir. Bir değişkeni birkaç değerle eşleştirmeye yardımcı olur.

- `case-statement.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

read -p "Input first number: " first_number
read -p "Input second number: " second_number
read -p "Select an math operation
1 - addition
2 - subtraction
3 - multiplication
4 - division
" operation

case $operation in
  "1") 
     echo "result= $(( $first_number + $second_number))"
  ;;
  "2")
     echo "result= $(( $first_number - $second_number))"
  ;;
  "3")
     echo "result= $(( $first_number * $second_number))" 
     ;;
  "4")
     echo "result= $(( $first_number / $second_number))"
  ;;
  *)
     echo "Wrong choice..." 
  ;;
esac
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x case-statement.sh
./case-statement.sh
```

# EXAMPLE-1 SOLUTIONS:
#!/bin/bash

# Kullanıcıdan dosya adı girişi al
read -p "Bir dosya adı girin: " filename

# Dosyanın mevcut olup olmadığını kontrol et
if [ -e "$filename" ]; then
  echo "Dosya zaten var."
else
  # Dosya mevcut değilse oluştur
  touch "$filename"
  echo "Dosya oluşturuldu."
fi

# EXAMPLE-2 SOLUTIONS:
#!/bin/bash

# Kullanıcıdan dosya veya dizin adı girişi al
read -p "Bir dosya veya dizin adı girin: " name

# Dosya veya dizinin mevcut olup olmadığını kontrol et
if [ -f "$name" ] || [ -d "$name" ]; then
  echo "Dosya veya dizin zaten var."
else
  # Dosya veya dizin mevcut değilse dosya oluştur
  touch "$name"
  echo "Dosya oluşturuldu."
fi
