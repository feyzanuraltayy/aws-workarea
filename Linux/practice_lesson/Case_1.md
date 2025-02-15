# Case 1: Dosya ve Dizin İşlemleri

## Senaryo

Bir projenin dosya ve dizin yapısını organize etmeniz gerekiyor.

## Görevler

1. `project` adında bir dizin oluşturun.
2. Bu dizinin içinde `src`, `bin`, `docs` ve `tests` adında dört alt dizin oluşturun.
3. `docs` dizini içine `README.md` dosyası oluşturun ve içine "Project Documentation" yazın.
4. `src` dizini içine `main.sh` adında bir bash script dosyası oluşturun ve içine temel bir "Hello World" scripti yazın.
5. `main.sh` scriptini her yerden çalıştırabilmek için PATH variable kullanımını ayarlayın.

## Çözüm

### Adım 1: `project` Dizinini Oluşturma

```bash
mkdir project
cd project
```

### Adım 2: Alt Dizinleri Oluşturma

```bash
mkdir src bin docs tests
```

### Adım 3: `README.md` Dosyasını Oluşturma

```bash
echo "Project Documentation" > docs/README.md
```

### Adım 4: `main.sh` Scriptini Oluşturma

```bash
echo '#!/bin/bash' > src/main.sh
echo 'echo "Hello World"' >> src/main.sh
chmod +x src/main.sh
```

### Adım 5: PATH Variable Kullanımı

`main.sh` scriptini her yerden çalıştırabilmek için `src` dizinini PATH değişkenine ekleyin.

```bash
export PATH=$PATH:$(pwd)/src
```

Bu adımı `~/.bashrc` veya `~/.bash_profile` dosyanıza ekleyerek kalıcı hale getirebilirsiniz:

```bash
echo 'export PATH=$PATH:$(pwd)/src' >> ~/.bashrc
source ~/.bashrc
```

Bu adımları takip ederek proje yapınızı başarıyla organize edebilir ve `main.sh` scriptini her yerden çalıştırabilirsiniz.
