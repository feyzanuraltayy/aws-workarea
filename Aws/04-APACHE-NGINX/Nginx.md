# Hands-on Nginx : How to Install Nginx Web Server on EC2 Linux 2023

Purpose of the this hands-on training is to give the students basic knowledge of how to install Nginx Web Server on Amazon Linux 2023 EC2 instance.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- demonstrate how to launch AWS EC2 Instance.

- establish a connection with AWS EC2 Instance with SSH.

- install the Nginx Server on Amazon Linux 2023 Instance.

- configure the Nginx Server to run simple HTML page.

- write a simple bash script to run the Web Server

- automate the process of installation and configuration of a Web Server using the `user-data` script of EC2 Instance.

## Outline

- Part 1 - Create a Security group

- Part 2 - Launching an Amazon Linux 2023 EC2 instance and Connect with SSH

- Part 3 - Installing and Configuring Nginx Web Server to Run a Simple Web Page

- Part 4 - Automation of Web Server Installation through Bash Script


## Part 1 - Create Security Group

In the EC2 dashboard, go to Security Group section and create a security group named Nginx-Sec-Gr with Inbound rules as:
- SSH 22, 0.0.0.0/0 anywhere
- HTTP 80, 0.0.0.0/0 anywhere



## Part 2 - Launching an Amazon Linux 2 EC2 instance and Connect with SSH

Launch an Amazon 2023 (one for spare)EC2 instance with AMI as `Amazon Linux 2023`, instance type as `t2.micro` and in default VPC choose Nginx-Sec-Gr security group which allows connections.

Connect to your instance with SSH.


ssh -i [Your Key pair] ec2-user@[Your EC2 IP / DNS name]


## Part 3 - Installing and Configuring Nginx Web Server to Run a Simple Web Page

1. Update the installed packages and package cache on your instance.


sudo dnf update -y


2. Install the Nginx Web Server and Git.

```bash
sudo dnf install nginx -y
sudo yum install git -y
```

3. Start the Nginx Web Server.

```bash
sudo systemctl status nginx
sudo systemctl start nginx
```

4. Check from browser with public IP/DNS


5. Go to /usr/share/nginx/html folder.

```bash
cd /usr/share/nginx/html
```

6. Show content of folder and change the permissions of /usr/share/nginx/html

```bash
ls
sudo chmod -R 777 /usr/share/nginx/html
```

7. Remove existing `index.html`.

```bash
sudo rm index.html
```

8. Upload new `designer web site` with `git clone` command.

```bash
git clone https://github.com/techproedu/designer.git
cp -R ./designer/. /usr/share/nginx/html
```

9. restart the Nginx Web Server.

```bash
sudo systemctl restart nginx
```

10. configure to start while launching
```bash
sudo systemctl enable nginx
```

## Part 4 - Automation of Web Server Installation through Bash Script (User data)

11. Configure an Amazon EC2 instance with AMI as `Amazon Linux 2023`, instance type as `t2.micro`, in default VPC, choose Nginx-Sec-Gr security group which allows connections.

12. Configure instance to automate web server installation with `user data` script.

```bash
#!/bin/bash
dnf update -y
dnf install nginx -y
dnf install git -y
systemctl start nginx
cd /usr/share/nginx/html
git clone https://github.com/techproedu/designer.git
chmod -R 777 /usr/share/nginx/html
rm index.html
cp -R ./designer/. .
systemctl restart nginx
systemctl enable nginx
```

13. Review and launch the EC2 Instance

14. Once Instance is on, check if the Nginx Web Server is working from the web browser.

15. Connect the Nginx Web Server from the terminal with `curl` command.


curl http://<IPADRESS>
