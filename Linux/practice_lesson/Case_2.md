# Case 2: Kullanıcı ve Grup Yönetimi

## Senaryo
Yeni bir kullanıcı ve grup oluşturmanız ve bu kullanıcıya bazı dosya izinleri vermeniz gerekiyor.

## Görevler

1. `developer` adında bir kullanıcı oluşturun.
2. `devgroup` adında bir grup oluşturun.
3. `developer` kullanıcısını `devgroup` grubuna ekleyin.
4. `project` dizinini `developer` kullanıcısına ve `devgroup` grubuna ait olacak şekilde ayarlayın.
5. `project` dizini ve altındaki tüm dosya ve dizinler için tam erişim izni (read, write, execute) verin.

## Çözüm

### Adım 1: `developer` Kullanıcısını Oluşturma

Yeni bir kullanıcı oluşturun:

```bash
sudo useradd developer
```

### Adım 2: `devgroup` Grubunu Oluşturma

Yeni bir grup oluşturun:

```bash
sudo groupadd devgroup
```

### Adım 3: `developer` Kullanıcısını `devgroup` Grubuna Ekleyin

Kullanıcıyı gruba ekleyin:

```bash
sudo usermod -aG devgroup developer
sudo cat /etc/passwd
sudo cat /etc/group
```

### Adım 4: `project` Dizinini Sahiplik Ayarlarını Yapma

`project` dizinini `developer` kullanıcısına ve `devgroup` grubuna ait olacak şekilde ayarlayın:

```bash
cd ~
ls -l
sudo chown -R developer:devgroup project
```

### Adım 5: `project` Dizinine ve Altındaki Dosyalara Tam Erişim İzni Verme

`project` dizini ve altındaki tüm dosya ve dizinler için tam erişim izni (read, write, execute) verin:

```bash
sudo chmod -R 777 project
ls -Rl
```
