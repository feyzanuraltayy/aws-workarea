# Task: IAM Role with S3 Full Access and EC2 Instances

## Goal:
1. Create an IAM Role with S3 Full Access.
2. Launch two EC2 instances:
   - One with the IAM Role attached.
   - One without any IAM Role.
3. Configure both instances using the given user data script and ensure HTTP port access.

---

## Steps:

### 1. Create an IAM Role:
- **Name**: `TechProS3Role`
- **Trusted Entity**: AWS services
- **Use Case**: EC2
- **Permissions**: S3FullAccess (AmazonS3FullAccess)

---

### 2. Launch Two EC2 Instances:
#### Instance 1: Without IAM Role
- **AMI**: Amazon Linux 2023
- **Instance Type**: t2.micro
- **IAM Role**: None
- **User Data**:
```bash
#!/bin/bash
yum update -y
yum install -y httpd
cd /var/www/html
aws s3 cp s3://techpro-role-task/index.html .
aws s3 cp s3://techpro-role-task/cat.jpg .
systemctl enable httpd
systemctl start httpd
```

---

#### Instance 2: With IAM Role
- **AMI**: Amazon Linux 2023
- **Instance Type**: t2.micro
- **IAM Role**: `TechProS3Role`
- **User Data**:
```bash
#!/bin/bash
yum update -y
yum install -y httpd
cd /var/www/html
aws s3 cp s3://techpro-role-task/index.html .
aws s3 cp s3://techpro-role-task/cat.jpg .
systemctl enable httpd
systemctl start httpd
```

---

### 3. Security Group Configuration:
- Allow **HTTP (Port 80)** and **SSH (Port 22)** for both instances.

---

### Expected Outcome:
1. Instance without IAM Role:
   - Unable to fetch files from the S3 bucket.
   - Web server fails to serve the page.
2. Instance with IAM Role:
   - Successfully fetches files from the S3 bucket.
   - Web server serves the page with `index.html` and `cat.jpg`.
