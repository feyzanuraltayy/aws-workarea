# Hands-on ASG & ALB : Configuring Application Load Balancer (ALB) with Auto Scaling Group (ASG) using Launch Template

Purpose of the this hands-on training is to give the students basic knowledge of how to configure AWS Load Balancers with Auto Scaling Group and Launch Template.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- create and configure a load balancer with Target Group.

- create and configure Auto Scaling Group with Launch Template.

- add policy to Auto Scaling Group.

- add Cloudwatch alarm.

## Outline

- Part 1 - Create Security Group

- Part 2 - Create Target Group

- Part 3 - Create Application Load Balancer

- Part 4 - Create Launch Template

- Part 5 - Create Auto Scaling Group

- Part 6 - Create Auto Scaling Policy

## Part 1 - Create a Security Group

- Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

- Choose the Security Groups on left-hand menu

- Click the `Create Security Group`.

```text
Security Group Name  : ASGSecGroup
Description          : ASG Security Group
VPC                  : Default VPC
Inbound Rules:
    - Type: SSH ----> Source: Anywhere
    - Type: HTTP ---> Source: Anywhere
Outbound Rules: Keep it as default
Tag:
    - Key   : Name
      Value : ASGSecGroup
```

- Click `Create Security Group` button.

## Part 2 - Create Target Group

- Go to `Target Groups` section under the Load Balancing part on left-hand menu and select `Target Group`

- Click `Create Target Group` button

  - Basic configuration

    ```text
    Choose a target type    : Instances
    Give Target Groups Name : MyTargetGroup
    Protocol                : HTTP
    Port                    : 80
    VPC                     : Default VPC
    ```

  - Health checks

    ```text
    Health check protocol   : HTTP
    Health check path       : /
    ```

  - Advance health check settings

    ```text
    Port                    : Traffic port
    Healthy threshold       : 3
    Unhealthy threshold     : 2
    Timeout                 : 5 seconds
    Interval                : 10 seconds
    Success codes           : 200
    ```

  - Tags

    ```text
    Key                     : Name
    Value                   : MyTargetGroup
    ```

- Click next

- Unlike Application Load Balancer hands-on, do not register any instances into the target group.

- Click `Create Target Group` button.

## Part 3 - Create Application Load Balancer

Go to the Load Balancing section on left-hand menu and select `Load Balancers`.

- Click `Create Load Balancer` tab.

- Select the `Application Load Balancer` option.

- Step 1: Configure Load Balancer

```text
Name            : MyALBforAutoScaling

Scheme: Internet-facing
IP address type: IPv4

- Step 2: Network Mapping

Choose default VPC
Availability Zones          : Choose all AZ's

- Step 3: Configure Security Groups

- Select an existing  >>>> security group.

Name            :  ASGSecGroup
  

- Step 4: Listeners and Routing: 
A listener is a process that checks for connection requests, using the protocol and port that you configured.

Load Balancer Protocol      : HTTP
Load Balancer Port          : 80
Default action Forward to: Select your Target Group
PS : MyTargetGroup that we created for Application Load Balancer. It will be same both for Application Load Balancer and Auto Scaling


- Step 5:

Add-on services             : Keep it as default

- Step 6:

Tags                        :
    - Key   : Name
    - Value : MyALBforAutoScaling
```

- Review and if everything is ok, click the `Create` button.

```text
Successfully created load balancer!
```

- Please wait for changing the state from `provisioning` to `active`.

## Part 4 - Create Launch Template

- Select `Launch template` from the left-hand menu and then click `Create Launch template` to start.

- Launch Template Name

```text
Launch template name            : MyTemplate_Auto_scaling
Template version description    : MyTemplate_Auto_scaling
```

- Amazon Machine Image (AMI)

```text
Amazon Linux 2023 AMI (HVM), SSD Volume Type,(us-east-1)
```

- Instance Type

```text
t2.micro
```

- Key Pair

```text
Please select your key pair (pem key) that is created before
Example: <keyname>.pem
```

- Network settings

```text
Network Platform : Virtual Private Cloud (VPC)
```

- Security groups

```text
Please select security group named ASGSecGroup
```

- Storage (volumes)

```text
Keep it as default (Volume 1 (AMI Root) (8 GiB, EBS, General purpose SSD (gp2)))
```

- Resource tags

```text
Key             : Name
Value           : Auto_Scaling
Resource type   : Instance
```

- Network interfaces

```text
Keep it as it is
```

- Within `Advanced details` section, we will just use `user data` settings. Please paste the script below into the `user data` field.

```bash
#!/bin/bash
#update os
yum update -y
#install apache server
yum install -y httpd
# get private ip address of ec2 instance using instance metadata
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& PRIVATE_IP=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-ipv4`
# get public ip address of ec2 instance using instance metadata
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& PUBLIC_IP=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4` 
# get date and time of server
DATE_TIME=`date`
# set all permissions
chmod -R 777 /var/www/html
# create a custom index.html file
echo "<html>
<head>
    <title> Application Load Balancer</title>
</head>
<body>
    <h1>Testing Application Load Balancer</h1>
    <h2>Congratulations! You have created an instance from Launch Template</h2>
    <h3>This web server is launched from the launch template by AWS-SEVOPS B303</h3>
    <p>This instance is created at <b>$DATE_TIME</b></p>
    <p>Private IP address of this instance is <b>$PRIVATE_IP</b></p>
    <p>Public IP address of this instance is <b>$PUBLIC_IP</b></p>
</body>
</html>" > /var/www/html/index.html
# start apache server
systemctl start httpd
systemctl enable httpd
```

- Click Create Launch template

## Part 5 - Create Auto Scaling Group (Create an Auto Scaling Group that keeps the target group in initial size)

- EC2 AWS Management console, select Auto Scaling Group from the left-hand menu and then click Create Auto Scaling Group

```text
Name: First-AS-Group
```

Step 1: Choose launch template or launch configuration:

- Switch to the `Launch template`, select newly created launch template and click `Next` to continue.

Step 2: Configure settings:

- Network

```text
VPC         : Default VPC
Subnets     : Select all Subnets
```

Step 3: Configure advanced options:

- Select  >>>> `Attach to an existing load balancer` option

- Click Choose from your load balancer target groups and find Target Group: `MyTargetGroup`

- Leave VPC Lattice as is (No VPC Lattice)

- Health Checks


```text
EC2 Health checks is always enabled

Additional Health Check type           : Click Turn on ELB health checks (Recommended)
Health check grace period   : 200 seconds
```

- Additional Settings : Keep it as default

Step 4: Configure group size and scaling policies:

- Group size

```text
Desired capacity        : 1
Minimum capacity        : 1
Maximum capacity        : 1
```

- Scaling policies

```text
None
```

- Instance scale-in protection

Leave as is
```text
Do not check
```

Step 5: Add notifications:

- Skip Notification

Step 6: Add Tags

```text
Key     : Name
Value:  : Autoscaling
```

Step 7: Review and create Auto Scaling Group.

- Right click the `Instance` tap on left hand menu and open in new window and show the sub-sections and also show there is 1 instance created by auto scaling group,

- Right click the `Target Group` tap on left hand menu and open in new windows show the sub-sections and details. In Target Menu, show that the instance seems healthy based on rules that we set before.

- Right click the `Load Balancing` tap on left hand menu and open in new window show the sub-sections and details.


- Explain the sub-menu of ASG

- Change the configuration of Autoscaling Group

Step 1:

- Go to Auto Scaling Groups and check the `ALBforAutoScaling` flag

- Click `Edit` Tab

- Change Values of Group Size

```text
Desired capacity    : 2
Minimum capacity    : 1
Maximum capacity    : 4
```

- Keep the rest of settings as default

- Click `Update`

Step 2:

- Show the changes in `instance number`, `activity tab` and `target group`.

- Go to `Instance Tab` on left hand-menu and show instances created by auto scaling group.

- Go to `Load Balancers` on the left-hand menu and copy Load Balancer DNS. Then paste it to browser, refresh the page and show the differences, like IP and dates.

Step 3: Observe that Autoscaling keeps the target group in initial size.

- Go to `Instance Tab` >>>>>>> stop one of the instance.

- Go to `Target Group` on left-hand menu and click `MyTargetGroup`---> `Targets`.

- Show the status of the stopped instance and refresh it. It probably takes a while to create a new instance by Auto Scaling.


## Part 6 - Create Auto Scaling Policy

- Go to `Auto Scaling Groups` --> click `First-AS-Group` --> `Automatic Scaling` 

- Explain the Policy Types

Step 1: Select `Create dynamic scaling policy` 

Policy Type >>>> Simple Scaling 

```text
Scaling Policy Name : First Scaling Policy-Add
```

- Click Create a CloudWatch Alarm

- Select Metric ---> `EC2` --> By Auto Scaling Group --> `First-AS-Group` and **`CPUUtilization`**

- Statistic: Average

- Metric --> Period: 1 minute

- Conditions -->

```text
Threshold Type "Static"

Whenever CPUUtilization is...:  Greater

Enter 60 as threshold value
```

- Click `Next`

- Click Notification >>> `Remove` tab at the top of the page and do not set any Notification, Autoscaling and EC2 Action

- Click `Next`

- Add name and description

```text
Alarm name                      : Auto Scaling-Add
Alarm description - optional    : Auto Scaling-Add
```

- Click `Next`, Review and Create alarm

- Click `Create a CloudWatch alarm`

- Go back to Autoscaling page and refresh the cloudwatch alarm

- Select `Auto Scaling-Add` as Cloudwatch Alarm

- Take the Action :

```text
Add --- 1 ---- Capacity Unit
An Then wait   : 200
```

- Click Create

Step 2: Create `Remove-Policy`;

- Click `Add Policy`

- Select Policy Type >>> `Simple Scaling` 

```text
Scaling Policy Name : First Scaling Policy-Remove
```

- Click `Create a CloudWatch alarm`

- Select Metric ---> `EC2` --> By Auto Scaling Group --> `First-AS-Group` and CPUUtilization

- Metric --> Period: 1 minute

- Conditions -->

```text
Threshold Type "Static"

Select Lower

Enter 30 as threshold value
```

- Click `Next`

- Add name and description

```text
Alarm name                      : Auto Scaling-Remove
Alarm description - optional    : Auto Scaling-Remove
```

- Click `Next`, Review and Create Alarm

- Go back to Autoscaling page and refresh the Cloudwatch Alarm

- Select `Auto Scaling-Remove` as Cloudwatch Alarm

- Take the Action :

```text
Remove --- 1 ---- Capacity Unit
An Then wait   : 200
```
Click Create

Step 3: Testing

- Go to Instance Menu

- Select one of the Auto Scaling Instance and connect with SSH

- Download `stress tool`

```bash
sudo yum install -y stress
stress --cpu 80 --timeout 20000   
```

- Click the instance's Monitoring Tab and show the effect of `stress tool` on CPU Utilization

- Show newly created instance based on `add-policy`

- Go to instance terminal and stop `stress tool` with `CTRL-C`

- Show the removed instance after `stress tool` stops based on `remove-policy`

- Delete the Simple Policies

Step 4: Create Step Scaling Policy

- Go to `Auto Scaling Groups` --> click `First-AS-Group` --> `Automatic Scaling` 

- Click Create `Dynamic Scaling Policy`;

- Select `Step Scaling` as Policy Type

- Name :
```text
Step Policy Name : First Step Policy-Add
```
- Select `Auto Scaling-Add` as Cloudwatch Alarm

- Take the Action : 

```text
Add --- 1 ---- Capacity Unit ----when 60---    <=    CPUUtilization 90


Clic "Add step"

Add ----2 -----Capacity Unit ----when 90 ----  <= Infinity

An Then wait   : 200
```
Click Create.

- Create `Remove-Policy`;

- Name :
```text
Step Policy Name : First Step Policy-Remove
```

- Select `Step Scaling` as Policy Type

- Select `Auto Scaling-Remove` as Cloudwatch Alarm

- Take the Action :

```text
Remove --- 1 ---- Capacity Unit
An Then wait   : 200
```

- Use the stress tool on EC2 Instances

- Stop the stress tool with CTRL + C

- Delete the Step Polices




- Step 5: Show target Tracing Policy

- Go to `Auto Scaling Groups` --> click `First-AS-Group` --> `Automatic Scaling` 

- Click Create Dynamic Scaling Policy;


```text
Policy Type         : Target Tracking Policy
Scaling Policy Name : First Target Tracking
Target value        : 60
Instances need      : 200 sec
```
Use the stress tool on EC2 Instances to observe results


- Stop the stress tool with CTRL + C

- Delete the Target Tracking  Policy

- Delete Auto-scaling group and Load Balancer

