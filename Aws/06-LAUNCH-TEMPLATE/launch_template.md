# Hands-on EC2: Creating an Instance with Launch Template and Versioning

Purpose of the this hands-on training is to give the students understanding of how to create Launch Template on AWS Console with `user data` and how to version Launch Templates.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- create and configure Launch Templates.

- modify Launch Template with versioning.

## Outline

- Part 1 - Creating Launch Templates

- Part 2 - Modifying Launch Templates

## Part 1 - Creating Launch Templates

### Step 1: Create Security Group

1. Create a Security Group to be used in Launch Template.


Launch_Temp_Sec_group: SSH 22, HTTP 80 ----> anywhere(0.0.0.0/0)


### STEP 2: Create Launch Template

2. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

3. On the navigation pane, under `INSTANCES`, choose `Launch Templates`.

4. Click on `Create launch template`.

5. Enter a name and provide a description for the initial version of the launch template.


Name                         : MyLaunchTemplate
Template version description : Origin


6. Autoscaling Guidance


Keep it as default


7. Template Tags


Keep it as is


8. Source Template :


Keep it as is


9. Amazon machine image (AMI)

Click Quick Start
Amazon Linux 2023 AMI (HVM), SSD Volume Type
ami-0df8c184d5f6ae949

10. Instance Type


t2.micro


11. Key pair

Please select your key pair (pem key) that is created before

Example: firstkey.pem


12. Network settings

Subnet: Don't include ..


13. Security groups


Security Group Name: Launch_Temp_Sec_group


14. Storage (volumes)


we keep it as is  (Volume 1 (AMI Root) (8 GiB, EBS, General purpose SSD (gp2)))


15. Resource tags


Key             : Name
Value           : Webserver-Origin
Resource type   : Instance


16. Network interfaces


Keep it as is


17. Advance details


Keep it as is

18. Click Create Launch Template


### Step 3: Create an Instance with Launch Template

18. Go to `Launch Template` Menu

19. Select `MyLaunchTemplate` ---> `Actions` ---> `Launch Instance from Template`

20. Enter number of instance as `1` and choose a subnet from Network Settings.

21. Keep the rest of settings as is and click the `Launch instance` at the bottom.

22. Go to EC2 Instance menu and show the created instance.

## Part 4 - Modifying Launch Template

### Step 1: Launch Template Version 2

23. Go to Launch Template menu on the left hand pane

24. Select template named `MyLaunchTemplate` ---> `Actions` ---> `Modify template (Create New Version)`

25. Template version description


V2 nginx


26. Key pair


Select your .pem file name


27. Resource tags


Key             : Name
Value           : V2 nginx
Resource type   : Instance


28. Go to `Advance Details` on the bottom and add the script given below into the `user data` field.

```bash
#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl enable nginx
systemctl start nginx
```

29. Click Create template version to create another template

30. Go to `Launch Template` Menu and click on `MyLaunchTemplate`.

31. Select version `2` from the `Versions` tab.


Version         : 2
Description     : V2 nginx


32. Select `Actions` ---> `Launch instance from template`.


Number of Instance : 1

Network settings: Select a subnet


33. Click the `launch Instance` button at the bottom.

34. Go to `Instance Menu` and show recently created EC2 instance.

35. Copy EC2's 'Public IP`, paste it in a browser and show 'nginx' webpage.

### Step 2: Launch Template Version 3

36. Go to `Launch Template` menu on the left hand pane.

37. Select template named `MyLaunchTemplate` ---> `Actions` ---> 'Modify template (Create New Version)'.

38.  Template version description


V3 nginx


39. Key pair


Select your .pem file name


40. Resource tags


Key             : Name
Value           : Webserver-V3
Resource type   : Instance


41. Go to `Advance Details` on the bottom and add the script given below into the `user data` field.

```bash
#! /bin/bash
dnf update -y
dnf install nginx -y
yum install git -y
systemctl start nginx
cd /usr/share/nginx/html
git clone https://github.com/techproedu/designer.git
chmod -R 777 /usr/share/nginx/html
rm index.html
cp -R ./designer/. .
systemctl restart nginx
systemctl enable nginx
```

42. Click Launch Template

43. Go to `Launch Template` Menu and click on `MyLaunchTemplate`.

44. Select version `3` from the `Versions` tab.


Version         : 3
Description     : V3 nginx


45. Select `Actions` ---> `Launch instance from template`.

Source template version:3
Number of Instance : 1
Network Settings: Select a subnet


46. Click the `launch Instance` button at the bottom.

47. Go to `Instance Menu` and show recently created EC2 instance.

48. Copy EC2's `Public IP`, paste it in a browser and show `nginx` webpage with `Designer` web site image.