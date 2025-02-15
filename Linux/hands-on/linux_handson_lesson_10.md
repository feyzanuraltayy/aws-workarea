# Hands-on Linux-10 : Shell Scripting/Loops

Bu uygulamalı eğitimin amacı, öğrencilere shellde döngülerin nasıl kullanılacağını öğretmektir.

## Öğrenme Çıktıları

Bu uygulamalı eğitimin sonunda öğrenciler şunları yapabileceklerdir;

- shellde döngüleri açıklayabilecektir.

- shell script de while döngülerini kullanabilecek

- shell script de until döngülerini kullanma

- shell script de for döngülerini kullanma

- shell script de continue ve break deyimlerini kullanma

- shell script de select döngülerini kullanma

- https://killercoda.com/playgrounds/scenario/ubuntu (ubuntu kurulu hazır sistem)

## Anahatlar

- Bölüm 1 - While döngüleri

- Bölüm 2 - Until döngüleri

- Bölüm 3 - For döngüleri

- Bölüm 4 - Continue ve Break İfadeleri

- Bölüm 5 - Select döngüleri

## Bölüm 1 - While döngüleri

- Shell'de program yazarken bazı durumlarda kod bloğumuzu yalnızca bir kez çalıştırmak yeterli olmayabilir. Döngüler, bir kod bloğunun yürütülmesini tekrarlamak (yinelemek) için kullanılır.

- while döngülerinin if ifadelerine benzer bir boole mantığı vardır. Koşulun sonucu True değerini döndürdüğü sürece while döngüsünün altındaki kod bloğu çalışır. Koşul Yanlış'a döndüğünde döngü yürütmesi sonlandırılır ve program kontrolü bir sonraki işleme geçer.

- Bir klasör oluşturun ve onu 'loops' olarak adlandırın.

```bash
mkdir loops && cd loops
```

- 1'den 10'a kadar olan sayıları `while döngüsü` ile gösterelim. `while-loop.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

number=1

while [[ $number -le 10  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x while-loop.sh
./while-loop.sh
```

## Bölüm 2 - Until döngüleri

- Until döngüsü while döngüsüyle aynıdır, tek farkı test doğru olana kadar içindeki komutları yürütmesidir.

- 'until-loop.sh' adında bir 'komut dosyası' dosyası oluşturun.

```bash
#!/bin/bash

number=1

until [[ $number -ge 10  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

- Dikkat edin, bu sefer '-le' yerine '-ge' yazıyoruz. Yani ilk durumda koşul yanlıştır. Koşul doğrulanıncaya kadar kodu çalıştıracaktır.

- Komut dosyasını yürütülebilir hale getirin ve çalıştırın.

```bash
chmod +x until-loop.sh
./until-loop.sh
```

## Bölüm 3 - For döngüleri

- Bazen belirli bir listedeki öğelerin her biri için bir kod bloğunu yinelemek isteriz. Bunun için 'for döngüsü'nü kullanıyoruz.

- İşte basit bir örnek. 'for-loop.sh' adında bir 'komut dosyası' dosyası oluşturun.

```bash
#!/bin/bash

echo "Numbers:"

for number in 0 1 2 3 4 5 6 7 8 9
do
   echo $number
done

echo "Names:"

for name in Joe David Matt John Timothy
do
   echo $name
done

echo "Files in current folder:"

for file in `pwd`/*
do
   echo $file
done

for ((i=1; i<=10; i++))
 do
    echo "Sayı: $i"
 done
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x for-loop.sh
./for-loop.sh
```

### Dizileri for döngüsü ile kullanma

- `for-array.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")

for tool in ${devops_tools[@]}
do
   echo $tool
done
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x for-array.sh
./for-array.sh
```

## Bölüm 4 - Continue ve Break İfadeleri
 
- Gerekli koşul sağlanmadıkça döngü sonsuza kadar devam eder. Sonlanmadan sonsuza kadar çalışan bir döngü sonsuz sayıda tekrarlanabilir. Bu nedenle bu döngülere sonsuz döngü adı verilmektedir.

- 'infinite-loop.sh' adında bir 'komut dosyası' dosyası oluşturun.

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

- Komut dosyasını çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x infinite-loop.sh
./infinite-loop.sh
```

- ctrl + C tuşlarına basın ve işlemi sonlandırın.

### Break ifadesi

- Yukarıda gördüğümüz gibi sonsuz döngü sonsuza kadar çalışır. Break deyimi tüm döngünün yürütülmesini sonlandırmak için kullanılır.

- 'infinite-loop.sh' dosyasını değiştirelim.

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  echo $number
  ((number++))
  if [[ $number -eq 100 ]]
  then
    break
  fi
done
```

- Komut dosyasını çalıştırın.

```bash
./infinite-loop.sh
```

### Continue İfadesi

- Continue ifadesi Break komutuna benzer, tek farkı tüm döngü yerine döngünün geçerli yinelemesinden çıkılmasına neden olmasıdır.

- 'infinite-loop.sh' dosyasını değiştirelim. Bu sefer 10 ve katlarını (10, 20 ..) göstermiyoruz.

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  ((number++))
  
  tens=$(($number % 10))
  
  if [[ $tens -eq 0 ]]
  then
    continue
  fi

  echo $number
    
  if [[ $number -gt 100 ]]
  then
    break
  fi
done
```

- Komut dosyasını çalıştırın.

```bash
./infinite-loop.sh
```

## Bölüm 5 - Select döngüleri

- Select Loop, kullanıcıların seçenekleri seçebileceği numaralandırılmış bir menü oluşturur. Kullanıcıdan bir seçenek listesinden bir veya daha fazla öğe seçmesini istemeniz gerektiğinde faydalıdır.

- Select-loop.sh` adında bir `script` dosyası oluşturun. 

```bash
#!/bin/bash

read -p "Input first number: " first_number
read -p "Input second number: " second_number

PS3="Select the operation: "

select operation in addition subtraction multiplication division exit
do
  case $operation in
    addition) 
      echo "result= $(( $first_number + $second_number))"
    ;;
    subtraction)
       echo "result= $(( $first_number - $second_number))"
    ;;
    multiplication)
       echo "result= $(( $first_number * $second_number))" 
       ;;
    division)
       echo "result= $(( $first_number / $second_number))"
    ;;
    exit)
       break
    ;;   
    *)
       echo "Wrong choice..." 
    ;;
  esac
done
```

- Görüntülenen istemi değiştirmek için "PS3 sistem değişkenini" değiştirebileceğimizi unutmayın.

- Betiği çalıştırılabilir hale getirin ve çalıştırın.

```bash
chmod +x select-loop.sh
./select-loop.sh
```