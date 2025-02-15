# **Hands-on CLI: Working with AWS Command Line Interface**  

The purpose of this hands-on training is to enable students to perform tasks using the AWS Command Line Interface (AWS CLI) that they would normally do in the AWS Management Console.

## **Learning Outcomes**  

By the end of this hands-on training, students will be able to:  

- Install and configure AWS CLI  
- Perform IAM service operations using AWS CLI  
- Perform EC2 service operations using AWS CLI  
- Perform S3 service operations using AWS CLI  

## **Outline**  

- **Section 1** – AWS CLI Documentation  
- **Section 2** – AWS CLI Installation and Configuration  
- **Section 3** – IAM User Operations with AWS CLI  
- **Section 4** – EC2 Service Operations with AWS CLI  
- **Section 5** – S3 Service Operations with AWS CLI  

---

## **Section 1 – AWS CLI Documentation**  

- [AWS CLI Overview](https://aws.amazon.com/cli/)  
- [AWS Documentation](https://docs.aws.amazon.com/index.html)  
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)  
- [AWS CLI API Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)  
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)  

---

## **Section 2 – AWS CLI Installation and Configuration**  

### **Installation**  
Let's check if AWS CLI is installed:

```bash
aws --version
```

If AWS CLI is not installed, follow the appropriate installation guide:  
[**AWS CLI Installation Guide**](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### **a. Installation for Linux**  
```bash
sudo dnf remove awscli -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
PATH="$PATH:/usr/local/bin"
aws --version
```

#### **b. Installation for Mac**  
```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

#### **c. Installation for Windows**  
- **AWS CLI MSI Installer:**  
  [Download MSI Installer](https://awscli.amazonaws.com/AWSCLIV2.msi)  
  Or, run the following command in PowerShell:  
  ```bash
  msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
  ```
  Alternatively, install via `pip`:  
  ```bash
  pip install awscli --upgrade --user
  aws --version
  ```

---

### **Configuration**  

#### **Generate `Access Key ID` and `Secret Access Key` from IAM Service**  

- Go to **IAM** service.  
- Click on **Access Management → Users** from the left menu.  
- Select your user.  
- Navigate to the **Security Credentials** tab.  
- Under **Access Keys**, click **Create Access Key**.  
- Select **CLI**, check **Confirmation**, and click **Next**.  
- Enter a description and click **Create Access Key**.  

#### **Run the AWS CLI Configuration Command**  
```bash
aws configure

  AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
  AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  Default region name [None]: us-east-1
  Default output format [None]: json
```

#### **Verify Configuration Files**  
- **For Windows:**  
  ```cmd
  C:\Users\<username>\.aws
  ```
- **For Linux:**  
  ```bash
  cd /.aws
  cat config
  cat credentials
  ```

#### **Create a New Profile**  
```bash
aws configure --profile techpro
cat /.aws/config
cat /.aws/credentials
aws s3 ls --profile techpro
```

#### **Switch Between Profiles**  
```bash
export AWS_PROFILE=techpro
export AWS_PROFILE=default
```

#### **List Configured Profiles**  
```bash
aws configure list-profiles
```

#### **Check AWS Account Information**  
```bash
aws sts get-caller-identity
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo $AWS_ACCOUNT_ID
```

#### **Help Commands**  
```bash
aws help  
aws s3 cp help
```

---

## **Section 3 – IAM User Operations with AWS CLI**  

### **Create, List, and Delete IAM Users**  
```bash
aws iam list-users  # List users
aws iam create-user --user-name techpro  # Create user
aws iam delete-user --user-name techpro  # Delete user
```

### **IAM Group Operations**  
```bash
aws iam list-groups  
aws iam create-group --group-name aws  
aws iam add-user-to-group --user-name techpro --group-name aws  
aws iam remove-user-from-group --user-name techpro --group-name aws  
aws iam delete-group --group-name aws  
```

---

## **Section 4 – EC2 Service Operations with AWS CLI**  

### **Create a Key Pair**  
```bash
aws ec2 create-key-pair --key-name techpro --query 'KeyMaterial' --output text > techpro.pem
aws ec2 describe-key-pairs
aws ec2 delete-key-pair --key-name techpro
```

### **Create and Configure Security Groups**  
```bash
aws ec2 create-security-group --group-name my-security-group --description "My Security Group"
aws ec2 authorize-security-group-ingress --group-name my-security-group --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name my-security-group --protocol tcp --port 22 --cidr 0.0.0.0/0
```

### **Launch an EC2 Instance**  
```bash
aws ec2 run-instances --image-id ami-0005e0cfe09cc9050 --count 1 --instance-type t2.micro --key-name techpro
```

### **List EC2 Instances**  
```bash
aws ec2 describe-instances
```

### **Start, Stop, Terminate EC2 Instances**  
```bash
aws ec2 start-instances --instance-ids $INSTANCE_ID
aws ec2 stop-instances --instance-ids $INSTANCE_ID
aws ec2 terminate-instances --instance-ids $INSTANCE_ID
aws ec2 reboot-instances --instance-ids $INSTANCE_ID
```

---

## **Section 5 – S3 Service Operations with AWS CLI**  

### **S3 Bucket and Object Operations**  
```bash
aws s3 ls  
aws s3 mb s3://techproed  # Create a new bucket
aws s3 cp file.txt s3://techproed  # Upload file
aws s3 cp s3://techproed/file.txt newfile.txt  # Download file
aws s3 ls s3://techproed  # List bucket contents
aws s3 rm s3://techproed/file.txt  # Delete file
aws s3 rb s3://techproed --force  # Delete bucket and contents
```

