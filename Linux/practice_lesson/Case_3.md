# Case 3: Bash Script Yazma

## Senaryo
Bir dizin içindeki belirli türdeki dosyaları yedeklemeniz gerekiyor.

## Görevler

1. `backup.sh` adında bir bash script yazın.
2. Bu script, `~/project/src` dizinindeki tüm `.sh` dosyalarını `~/backup` dizinine kopyalayacak.
3. `~/backup` dizini yoksa, script bu dizini oluşturmalı.

## Çözüm

### `backup.sh` Scriptini Yazma

Aşağıdaki adımları takip ederek `backup.sh` scriptini oluşturabilirsiniz:

### Adım 1: `backup.sh` Scriptini Oluşturma

```bash
touch backup.sh
vim backup.sh
```

```text
#!/bin/bash
SOURCE_DIR=~/project/src
BACKUP_DIR=~/backup

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

cp $SOURCE_DIR/*.sh $BACKUP_DIR/
echo "Backup completed."
```

### Adım 2: Scripti Çalıştırma İzni Verme

`backup.sh` scriptine çalıştırma izni verin:

```bash
chmod +x backup.sh
```

### Adım 3: Scripti Çalıştırma

Scripti çalıştırarak `~/project/src` dizinindeki tüm `.sh` dosyalarını `~/backup` dizinine kopyalayın:

```bash
ls
./backup.sh
ls ./backup
```

## Ekstra Örnek: Yedekleme İşlemine Tarih Ekleme

Yedekleme işlemine tarih eklemek isteyebilirsiniz. Bu, yedekleme işlemlerini daha iyi takip etmenize yardımcı olur. Aşağıdaki örnekte, yedeklenen dosyaların yeni bir alt dizine kopyalanması ve bu alt dizinin yedekleme tarihi ile adlandırılması gösterilmektedir:

### `backup_with_date.sh` Scriptini Yazma


```bash
touch backup_with_date.sh
vim backup_with_date.sh
``` 

```bash
#!/bin/bash
SOURCE_DIR=~/project/src
BACKUP_DIR=~/backup
DATE=$(date +%Y%m%d_%H%M%S)

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

DEST_DIR="$BACKUP_DIR/backup_$DATE"
mkdir -p "$DEST_DIR"

cp $SOURCE_DIR/*.sh $DEST_DIR/
echo "Backup completed to $DEST_DIR."
```

### Adım 2: Scripti Çalıştırma İzni Verme

`backup_with_date.sh` scriptine çalıştırma izni verin:

```bash
chmod +x backup_with_date.sh
```

### Adım 3: Scripti Çalıştırma

Scripti çalıştırarak `~/project/src` dizinindeki tüm `.sh` dosyalarını tarihli bir alt dizine kopyalayın:

```bash
./backup_with_date.sh
```

Bu adımları takip ederek hem temel yedekleme scriptini hem de tarih eklemeli yedekleme scriptini oluşturabilirsiniz.
