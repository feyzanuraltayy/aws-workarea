# Hands-on Apache : How to Install Apache Web Server on EC2 Linux 2023

## Outline

- Part 1 - Getting to know the Apache Web Server

- Part 2 - Launching an Amazon Linux 2023 EC2 instance and Connect with SSH

- Part 3 - Installing and Configuring Apache Web Server to Run `Hello World` Page

- Part 4 - Automation of Web Server Installation through Bash Script

## Part 1 - Getting to know the Apache Web Server


The Apache HTTP Server, known as Apache, is a free and open-source cross-platform web server software, which is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

## Part 2 - Launching an Amazon Linux 2023 EC2 instance and Connect with SSH

1. Launch an Amazon EC2 instance with setting seen below: 

AMI: "Amazon Linux 2023"
Instance Type : "t2micro"
Region: "N.Virginia"
VPC: "Default VPC"
Securtiy Group: "0.0.0.0/0-----> Port 22"

2. Connect to your instance with SSH.


ssh -i .....pem ec2-user@


## Part 3 - Installing and Configuring Apache Web Server to Run `designer` Web Page

# STEP_1_ Default Apache Web Server

3. Update the installed packages and package cache on your instance.

`` bash
sudo dnf update -y
```

4. Install the Apache Web Server

```bash
sudo dnf install httpd -y
```

5. Check status of the Apache Web Server. show that it is not running(Red). After that Start the Apache Web Server.

```bash
sudo systemctl status httpd
sudo systemctl start httpd
```

6. Check status of the Apache Web Server.Show that it is running (Green)

```bash
sudo systemctl status httpd
```
7. Enable the Apache Web Server to survive the restarts then Check from browser with DNS/ PublicIP. Can you see the page?  

- Since the security group is available only for SSH and we try on browser which is HTTP, port 80, we cannot view unless we add HTTP add port 80.

Modify the Security Group and add HTTP port 80 than check again.


Securtiy Group: "0.0.0.0/0-----> Port 80"

# STEP_2_ Basic Customization of  Apache Web Server

8. Set permission of the files and folders under `/var/www/html/` folder to everyone.

```bash
sudo chmod -R 777 /var/www/html


9. Go to the /var/www/html and use ``git clone`for web site.

```bash
sudo yum install git -y
git clone https://github.com/techproedu/designer.git
cp -R ./designer/. /var/www/html
cd /var/www/html
```

10. Restart the httpd server and `check` from browser.

```bash
sudo systemctl restart httpd
```

11. Check if the Web Server is working properly from the browser.

## Part 4 - Automation of Web Server Installation through Bash Script

18. Configure an Amazon EC2 instance with AMI as `Amazon Linux 2023`, instance type as `t2.micro`, default VPC security group which allows connections from anywhere and any port.

19. Configure instance to automate web server installation with `user data` script.

```bash
#!/bin/bash
dnf update -y
dnf install httpd -y 
dnf install git -y
systemctl start httpd
systemctl enable httpd
cd /home/ec2-user
git clone https://github.com/techproedu/designer.git
sudo chmod -R 777 /var/www/html
cp -R ./designer/. /var/www/html
sudo systemctl restart httpd
```


20. Review and launch the EC2 Instance

21. Once Instance is on, check if the Apache Web Server is working from the web browser.

22. Connect the Apache Web Server from the local terminal with `curl` command.


- curl http://<IPADRESS>

