# AWS Flask Deployment - Auto Scaling and Load Balancer

## Proje Açıklaması
Bu proje, AWS üzerinde Flask tabanlı bir Python uygulamasını dağıtmayı amaçlamaktadır. Mimari, Auto Scaling Group, Application Load Balancer ve EC2 örnekleri kullanılarak oluşturulacaktır. Kaynak kodları GitHub'dan çekilecek ve Flask uygulaması otomatik olarak başlatılacaktır.

## Mimari Bileşenler
- **VPC (Virtual Private Cloud)**: İzole bir ağ oluşturur.
- **Public Subnet**: EC2 örneklerini barındıracak ağ bileşeni.
- **EC2 Instances**: Flask uygulamasını çalıştıran sanal makineler.
- **Auto Scaling Group**: Trafiğe göre EC2 örneklerini ölçeklendirir.
- **Application Load Balancer**: Trafiği eşit olarak dağıtır.
- **Security Groups**: Güvenlik duvarı kurallarını belirler.
- **GitHub**: Kaynak kodların yönetildiği depo.

## Gereksinimler
- AWS Hesabı
- AWS Management Console erişimi
- GitHub Hesabı
- Flask ile basit bir Python uygulaması

## 1. AWS Kaynaklarının Oluşturulması

### 1.1 VPC ve Subnet Tanımlama (AWS Management Console)
1. Default VPC ve subnetler kullanılacak.

### 1.2 Güvenlik Grupları Ayarlama
1. Hem EC2'lar için hem de ALB için security group oluşturulacak.
  - EC2 securiy group inbound: ssh:anywhere ve http: albssecuritygroup
  - ALB security group ise yalnızca http:anywhere olacak.

### 1.3 Load Balancer ve Target Group Oluşturma
1. Gerekli ayarları set ederek application load balancer ve target group oluşturulacak.

## 2. EC2 Örneklerinin Oluşturulması

### 2.1 Launch Template ile Flask Kurulumu
  - **EC2 Dashboard** > **Launch Templates** sekmesine gidin.
  - **Create Launch Template** butonuna tıklayın.
  - **Amazon Machine Image (AMI)** olarak **Ubuntu 24.04** seçin.
  - **Instance Type** olarak **t2.micro** seçin.
  - **Security Group** olarak oluşturduğunuz grubu ekleyin.
  - **User Data** sekmesine aşağıdaki komutları ekleyin:

```
#!/bin/bash
apt update -y
apt install git python3-pip python3-flask -y
cd /home/ubuntu
git clone https://github.com/your_github_repo/flask_app.git
cd flask_app
python3 app.py
```

  - Sonra **Launch Template** oluşturun.

### 2.2 Auto Scaling Group Ayarlama
1. **EC2 Dashboard** > **Auto Scaling Groups** sekmesine gidin.
2. **Create Auto Scaling Group** butonuna tıklayın.
3. Oluşturduğunuz **Launch Template**'i seçin.
4. Minimum: **1**, Maximum: **3**, Desired: **2** değerlerini girin.
5. **Target Group** olarak Load Balancer’a bağlayın.


## 3. Son Kontroller
- Load Balancer DNS adını tarayıcıya girerek Flask uygulamanızın çalıştığını doğrulayın.
- Auto Scaling Group'un EC2 örneklerini ölçeklendirdiğini test edin.

## Ekstra Kaynaklar
- [AWS Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/)
- [Flask Deployment on AWS](https://flask.palletsprojects.com/en/2.0.x/deploying/)
- [GitHub Actions for CI/CD](https://docs.github.com/en/actions)

