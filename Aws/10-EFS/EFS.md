**Hands-on EFS-01: How to Create EFS and Attach it to Multiple EC2 Instances**:

---

# **Hands-on EFS-01: How to Create EFS and Attach it to Multiple EC2 Instances**

## **Outline**

- **Section 1** - Preparation (EC2 SecGrp, EFS SecGrp, EC2 Instance)  
- **Section 2** - Creating EFS  
- **Section 3** - Attaching EFS to Multiple EC2 Instances  
- **Section 4** - Auto-Mounting EFS on Reboot  

---

## **Section 1 - Preparation (EC2 SecGrp, EFS SecGrp, EC2 Instance)**

### **Step 1 - Create EC2 Security Group (SecGrp)**

- Open the **Amazon EC2 console** at [AWS EC2 Console](https://console.aws.amazon.com/ec2/)
- From the left-hand menu, select **Security Groups**
- Click **Create Security Group**

```yml
Security Group Name  : EC2 SecGrp
Description          : EC2 SecGrp
VPC                  : Default VPC
Inbound Rules:
    - Type: SSH ----> Source: Anywhere
Outbound Rules: Keep it as default
Tag:
    - Key   : Name
      Value : EC2 SecGrp
```

---

### **Step 2 - Create EFS Security Group (SecGrp)**

- Click **Create Security Group**

```yml
Security Group Name  : EFS SecGrp
Description          : EFS SecGrp
VPC                  : Default VPC
Inbound Rules:
    - Type: NFS ----> Port: 2049 ------> Source: sg-EC2 SecGrp
Outbound Rules: Keep it as default
Tag:
    - Key   : Name
      Value : EFS SecGrp
```

---

### **Step 3 - Launch EC2 Instances**

#### **Launch First EC2 Instance in N.Virginia**
```yml
AMI             : Amazon Linux 3
Instance Type   : t2.micro
Network         : default
Subnet          : default
Security Group  : EC2 SecGrp
    Sec.Group Name : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EC2-1
```

#### **Launch Second EC2 Instance in N.Virginia**
```yml
AMI             : Amazon Linux 3
Instance Type   : t2.micro
Network         : default
Subnet          : default
Security Group  : EC2 SecGrp
    Sec.Group Name : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EC2-2
```

---

## **Section 2 - Creating EFS**

- Open the **Amazon EFS console** at [AWS EFS Console](https://console.aws.amazon.com/efs/)
- Click **Create File System**

```yml
Name                            : FirstEFS
Virtual Private Cloud (VPC)     : Default VPC (Keep default)
Availability and Durability     : Regional (Keep default)
```

- Click **Customize** to manually configure settings:

```yml
General

Name                    : FirstEFS (Pre-filled from previous step)
Availability and Durability : Regional (Pre-filled from previous step)
Automatic backups       : Unchecked "Enable automatic backups"
Lifecycle management    : Select "None"
Performance mode        : General Purpose
Throughput mode         : Bursting
Encryption              : Enable encryption of data at rest
Tags                    : Optional
```

Click **Next**

```yml
- Virtual Private Cloud (VPC): Default VPC
- Mount targets: 
  - Select all AZs (Keep default)
  - Remove "default sg" from all AZs
  - Add "EFS SecGrp" to all AZs
```

Click **Next**

```yml
File system policy - optional ----> Keep it as is
```

Click **Next** → **Review and Create**  
Confirm that the EFS has been successfully created.

---

## **Section 3 - Attaching EFS to Multiple EC2 Instances**

### **Step 1: Configure EC2-1 Instance**

- Open the **EC2 console**
- Connect to **EC2-1 via SSH**
```bash
ssh -i .....pem ec2-user@..................
```

- Update installed packages and package cache:
```bash
sudo dnf update -y
```

- Change the hostname:
```bash
sudo hostnamectl set-hostname First
```

- Run:
```bash
bash
```

- Install **Amazon EFS Utils**:
```bash
sudo dnf install -y amazon-efs-utils
```

- Create a mount point:
```bash
sudo mkdir efs
```

- Open the **EFS console**, select **FirstEFS**, click **Attach**, and copy the **EFS mount helper** command.

- Mount EFS:
```bash
sudo mount -t efs -o tls fs-xxxxxx:/ efs
```

- Verify the EFS mount:
```bash
ls
```

- Navigate to the EFS directory and create a file:
```bash
cd efs
sudo vim example.txt
```

- Write and save:
```yml
"hello from first EC2-1"
```

- Check the file:
```bash
cat example.txt
```

- Verify the EFS mount point's IP:
```bash
netstat -tulpan | grep 2049
```
The netstat command is used in Linux-based operating systems to query specific network activity.
---

### **Step 2: Configure EC2-2 Instance**

- Connect to **EC2-2 via SSH**:
```bash
ssh -i .....pem ec2-user@..................
```

- Repeat the same setup as EC2-1.
- Install **Amazon EFS Utils**:
```bash
sudo dnf install -y amazon-efs-utils
```

- Create a mount point:
```bash
sudo mkdir efs
```

- Open the **EFS console**, select **FirstEFS**, click **Attach**, and copy the **EFS mount helper** command.

- Mount EFS:
```bash
sudo mount -t efs -o tls fs-xxxxxx:/ efs
```

- Verify the EFS mount:
```bash
ls
```

- Navigate to the EFS directory:
```bash
cd efs
```

- Verify `example.txt` is accessible and update it:
```bash
sudo vim example.txt
"hello from first EC2-2"
```

- Confirm both entries exist:
```bash
cat example.txt
```

- Check from **EC2-1**:
```bash
cd efs
cat example.txt
```

---

### **Step 3: Configure EC2-3 to Mount EFS at Launch**

- Go to **EC2 console**, click **Launch Instance**, and configure:

```yml
AMI             : Amazon Linux 3
Instance Type   : t2.micro
Network         : Default VPC / Select any subnet
Subnet          : Select any default subnet
Configure Storage : Advanced Settings

                 File systems  >>>> Edit >>> Add Shared File System → FirstEFS
                (Note "/mnt/efs/fs1" as the mount point)
Security Group  : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EC2-3
```

- Connect to **EC2-3 via SSH**:
```bash
ssh -i .....pem ec2-user@..................
```

- Navigate to the mount directory:
```bash
cd /mnt/efs/fs1/
```

- Confirm **example.txt** exists:
```bash
ls
cat example.txt
```

- Add an entry:
```bash
sudo vim example.txt
"hello from first EC2-3"
```

- Verify all entries exist:
```bash
cat example.txt
```

---

## **Section 4 - Auto-Mounting EFS on Reboot**

- Reboot **EC2-1** or **EC2-2**:
```bash
sudo reboot now
```

- Show that EC2-1 / EC2-2 lost their configuration, while EC2-3 retains it.

- Backup `/etc/fstab`:
```bash
sudo cp /etc/fstab /etc/fstab.bak
```

- Edit `/etc/fstab`:
```bash
sudo vim /etc/fstab
```

- Add:
```yml
fs-067c32aa4ed707676:/  /home/ec2-user/efs  efs  defaults,_netdev   0    0
```

- Save (`esc + :wq`), then reboot:
```bash
sudo reboot now
```

- Verify volumes:
```bash
lsblk
```

- Check disk usage:
```bash
df -h
```

- Confirm data persistence.

- Terminate instances and delete the file system from the console.

