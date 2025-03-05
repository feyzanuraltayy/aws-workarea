# Hands-on Route 53- 02

Purpose of the this hands-on training is to creating a DNS record sets and implement Route 53 routing policies. 


## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- create record sets

- manage the domain name routing

- implement routing policies in different use case

- use active-passive architecture in local vpc

## Outline

- Part 1 - Prep.

- Part 2 - Creating a fail-over routing policies

- Part 3 - Creating a geolocation routing policies

- Part 4- Creating Private Hosted Zone and records

## Part 1 - Part 1 - Prep.

### STEP 1: Create Sec.Group:
```bash
   Route 53 Sec: In bound : "SSH 22, HTTP 80, HTTPS 443  > anywhere(0:/00000)"
```
### STEP 2: Create Instances:

- We'll totally create "4 Linux" instances and "1 Windows" instance.
   
#### 1. Create EC2 in default VPC as named  "N.virginia"
```bash
Region: "N.Virginia"
VPC: Default VPC
Subnet: PublicA
Sec Group: "Route 53 Sec"

user data: 

#!/bin/bash

yum update -y
yum install -y httpd
yum install -y wget
cd /var/www/html
wget https://raw.githubusercontent.com/techproedu/norhvirginia/main/index.html
wget https://raw.githubusercontent.com/techproedu/norhvirginia/main/northvirginia.gif
systemctl start httpd
systemctl enable httpd
```

#### 2. Create EC2 in default VPC as named "Tokyo"

```bash
Region: "N.Virginia"
VPC: Default VPC
Subnet: PublicA
Sec Group: "Route 53 Sec"

user data:

#!/bin/bash

yum update -y
yum install -y httpd
yum install -y wget
cd /var/www/html
wget https://raw.githubusercontent.com/techproedu/tokyo/main/index.html
wget https://raw.githubusercontent.com/techproedu/tokyo/main/tokyo.jpg
systemctl start httpd
systemctl enable httpd

```

#### 3. Create EC2 in default VPC as named "Paris"

 ```bash 
Region: "N.Virginia"
VPC: Default VPC
Subnet: PublicA
Sec Group: "Route 53 Sec"

user data:

#!/bin/bash

yum update -y
yum install -y httpd
yum install -y wget
cd /var/www/html
wget https://raw.githubusercontent.com/techproedu/paris/main/index.html
wget https://raw.githubusercontent.com/techproedu/paris/main/paris.jpg
systemctl start httpd
systemctl enable httpd
```

#### 4. Create EC2 instance in "myVPC" named "Local"

```bash 
Region: "N.Virginia"
VPC: myVPC
Subnet: PublicA
Sec Group: ssh-http---->0.0.0.0/0

user data:

#!/bin/bash

yum update -y
yum install -y httpd
yum install -y wget
chkconfig httpd on
cd /var/www/html
wget https://raw.githubusercontent.com/techproedu/local/main/index.html
wget https://raw.githubusercontent.com/techproedu/local/main/local.jpg
service httpd start

```

#### 5. Create "Windows" instance in "myVPC" named "Windows"

```bash 
AMI: 2016 Base
Region: "N.Virginia"
VPC: myVPC
Subnet: PublicA
Sec Group: RDP---->0.0.0.0/0
```

### STEP 3: Create a Static WebSite:

 1. Create Static WebSite / "www.[your sub-domain name]"
 
  - Go to S3 service and create a bucket with sub-domain name: "www.[your sub-domain name]"
  - Public Access "Enabled"
  - Upload Files named "index.html" and "error.jpg"
  - Permissions>>> Bucket Policy >>> Paste bucket Policy
```bash
{
    "Version": "2012-10-17", 
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::don't forget to change me/*"
        }
    ]
}

```
  - Properties>>> Set Static Web Site >>> Enable >>> Index document : index.html 
   
## Part 2 - Creating fail-over routing policies

### STEP 1 : Create health check for "N. Virginia" instance

- Go to left hand pane and click the Health check menu 

- Click Create Health check button

- Configure Health Check

```bash 
1. Name: firsthealthcheck

Resource            : Endpoint

Specify endpoint by : IP address

Protocol            : HTTP

IP address          : N.Virginia IP address

Hostname:           : -

Port                : 80

Path                : leave it as /

Advanced Configuration 

Request Interval    :  Standard (30seconds)

Failure Threshold   : 3

Explain Response Time:

Failure = Time Interval * Threshold. If its a standard 30 seconds check then three checks is actually equal to 90 seconds. So be careful of how these two different settings interact each other.

String Matching     : No 

Latency Graphs:     : Keep it as is

Invert Health Check Status: Keep it as is

Disable Health Check:
Explain: If you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Invert health check status.

Health Checker Regions: Keep it as default

click create and show that the status is unhealthy approximately after 90 seconds the instance healthcheck will turned into the "healthy" from "unhealthy"
```
### Step 2: Create A record for  "N. Virginia" instance IP - Primary record

- Got to the hosted zone and select the public hosted zone of our domain name

- Clear all the record sets except NS and SOA

- Click create record

- select "Failover" as a routing policy

- click next

```bash
Record Name :"www"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - enter IP IP address of N.Virginia 
Routing: "Failover"
Failover record type    : Primary
Health check            : firsthealthcheck
Record ID               : Failover Scenario-primary
```
- click "Add another record" button

### Step 3: Create A record for S3 website endpoint - Secondary record

- Click create record

- select "Failover" as a routing policy

- click next

```bash
Record Name :"www"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Alias to S3 website endpoint"
  - N.Virginia(us-east-1)
  - Choose your S3 bucket named "www.[your sub-domain name].net"
Routing: "Failover" 
Failover record type    : Secondary
Health check            : keep it as is
Record ID               : Failover Scenario-secondary
```
- click "create records" button

- Go to browser and show the web page with N.Virginia instance content 

- Stop the N.Virginia instance

- check the healtcheck status and wait until it appears as unhealthy

- go to the browser and show the web site content turned into S3 bucket content with the help of the failover record


## Part 3 - Creating Geolocation routing policies

### STEP 1 :Create Geolocation record for Tokyo

- Click create record

- select "Geolocation" as a routing policy

- click next

```bash
Record Name :"geo"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - "IP of Tokyo Instance"
Routing: "Geolocation" 
Location               :
  - Countries Japan
Health check            : Keep it as is
Record ID               : Geolocation Scenario-Tokyo
```
- click "Add another record" button


### STEP 2 : Create geolocation record for Europe

```bash
Record Name :"geo"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - "IP of Geo-Paris Instance"
Routing: "Geolocation "
Location               :
  - Countinent : Europe
Health check            : Keep it as is
Record ID               : Geolocation Scenario-Europe
```

- click "Add another record" button

### STEP 3 : Create geolocation record for others

```bash
Record Name :"geo"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - "IP of N.Virginia"
Routing: "Geolocation"  
Location               : Select Default option
Health check           : Keep it as is
Record ID              : Geolocation Scenario-Others
```
- click "create records" button

- change the IP of your computer via VPN and see the Japon page.(proton vpn download and install)

- change the IP of your computer via VPN and see the Europe page.

- Send the DNS to students try for US and show them different web page based on location.

## Part 4 - Creating Private Hosted Zone and DNS Records 

### STEP 1: Creating Private Hosted Zone

- go to the dashboard and click on "Hosted Zones"
- Click "Create Hosted Zone"

```bash
   Domain name: the same name of your domain(techprodevops.com)
   Description: ---
   Type       :Private hosted zone
   VPCs to associate with the hosted zone
     Region : N.Virginia
     VPC ID : myVPC
  Tags:---

```
- Click on "create Hosted Zone"

- Show that NS and SOA records automatically created. 

### STEP 2: Creating in A record with "www" in Private Hosted Zone

- Go  to "PRIVATE" Hosted Zone 
- Create A record in "PRIVATE" Hosted Zone 
```bash
Record Name :"www"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - enter IP address of "Local" 
Routing: "Simple"
```
### STEP 3: Creating in A record with "www" in Public Hosted Zone

- Go  to "PUBLIC" Hosted Zone 
- Create A record in "PUBLIC" Hosted Zone 
```bash
Record Name :"www"
Record Type : A
TTL:"60"
Value/Route traffic to : 
  - "Ip address or another value depending on the record type"
    - enter IP IP address of "N.Virginia" 
Routing: "Simple"
```
- go to "Windows" instance and connect it with RDP
- open the Internet Explorer of "Windows" instance 
- type "www.techprodevops.com". show which content is seen "local instance content" in VPC 
- go to the public browser than type browser: "www.techprodevops.com" than show that, N.Virginia instance is seen on public internet.

### STEP 4: Cleaning 
- Delete Instances
- Delete bucket 
- Delete A records if they exist 
- Delete the HEALTH CHECK
