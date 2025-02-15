# Hands-on RDS : Configuring and Connecting RDS with Console and Workbench

Purpose of the this hands-on training is to configure RDS Instance via AWS Management Console and connect from MySQL Workbench.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- learn how to set configuration of RDS Instance on console.

- learn how to connect to RDS via workbench.

- learn how to manipulate RDS Instance.

## Outline

- Part 1 - Creating RDS Instance on AWS Management Console

- Part 2 - Configuring MySQL Workbench to connect to the RDS Instance

- Part 3 - Manipulating RDS Instance

## Part 1 - Creating RDS Instance on AWS Management Console

- First, create Security Group for RDS service. Select EC2 dashboard. Select Security Groups from the left-hand menu.
```text
Security Group Name: techproed_db_sg
Description: techproed_db_sg
VPC: Default
Inbound Rules:
    - Type: MYSQL/AURORA ---> Source: MyIP
Outbound Rules: Keep it as it is



-  Go to the Amazon RDS Service and select Database section from the left-hand menu, click databases and then click Creating Database.

- Choose a database creation method.

```

Create Database

Standard Create
```

- Engine option

```
MySQL
```

- Version

```
8.0.35
```

- Template

```
Free tier
```

- Settings

```
DB instance identifier: RDS-mysql
Master username: admin
Master password: Techpro12345
```

- DB instance Class

```
Burstable classes (includes t classes) : db.t2.micro
```

- Storage

```
Storage type          : ssd
Storage size          : default 20GiB
Storage autoscaling   : unchecked(tiki kaldir)
```

- Availability & durability

```
We can not select any option for free tier
```

- Connectivity

```bash
VPC                           : Default VPC

Click Additional Connectivity Configuration;

Subnet group                  : Default VPC
*Publicly accessible          : ***Yes  # Normalde biz bunu public yapmayiz denemek icin ancak normalde private olacak bu
Existing VPC security groups  : Select security group named techproed_db_sg
Availability Zone             : No preference

Click Additional Connectivity Configuration;
Database port                 : 3306(Bu degisebilir sonradan, DB yi olusturmadan tekrar kontrol et)
```

- Database authentication options

```
Database authentication options: Password authentication
```
Monitoring  : Unchecked
- Additional configuration

```
Initial DB name                   : techproeducation
DB parameter group & option group : default.mysql8.0
Automatic backups                 : enable
Backup retention period           : 7 days (Explain how)

Backup Window:      No preference
Copy tags to snapshots:     Secili kalsin

Log exports : Unchecked
```
```bash
Maintenance

  # Burada hani mesela MySQL icin ana version 8, minor version 0.23 tu ya hani, minor versiyonu otomatik olarak update edeyim mi diye soruyor.
  - Enable auto minor version upgrade: Enable auto minor version upgrade 

  # maintanance ile back up ayni tarih ve saatte olmasin cakisir
  - Maintenance window :    No preference

Deletion protection: *Enabled # Yanlislikla silmeyelim diye
```

- Estimated monthly costs
Show that when you select `production` instead of `Free Tier Template` it charges you.

- Click `Create Database` button. Burasi biraz zaman alabilir.

- Go to database menu and select `RDS-mysql` database and show and explain sub-sections (Connectivity & Security(Bunun altinda bir endpoint var, sonrasinda portu olan 3306 gorunebilir), Monitoring etc.)


## Part 2 - Configuring MySQL Workbench to connect to the RDS Instance

- First, go to the Amazon RDS Service, select `Database` section from the left-hand menu, click databases and select `RDS-mysql`. Then, copy the `endpoint` at the bottom of the page.

- Open the MySQL Workbench and click `+` to configure a new MySQL connection.

On the page opened, we'll set up a new connection:

```text
1. Connection Name   : RDS-Mysql.

2. Host Name         : Paste the endpoint of the database that you have copied 
                       and leave the port as is, 3306

3. Username          : admin
Here we enter the user name that we determined while creating the DB instance.
                      So we enter "admin" as a username.

4. Password          : Techpro12345
                      
                     - Click the `Store in Valut` and enter the password that you determined as "Techpro12345" while creating the DB Instance.

5. Test Connection   : Before you connect DB Instance, test the connection whether it works properly.
                       So, click `Test Connection` tab.

6. If the connection is set properly, you'll see the successfully message

7. Then click `OK` to complete the configuration
```

## Part 3 - Manipulating RDS Instance

- Show `techproeducation` database that is created together with RDS DB instance creation.

- Create a new database from "Schema" tab

- To modify the database, first, we need to create a new table. So, click the `techproeducation` schema (or your schema's name). Right-click the `Table` option, then select the `Create Table`, and enter `Personal_Info` as table name.

```text
1. First Row: Type `ID_number` into the first line. 
              ID number is an integer, so the system automatically assign Integer value to the Datatype column.
              Explain the Primary Key, choose the ID_number as a Primary Key, and check the PK box.

3. Second Row: type Name into the second row.VARCHAR(45)

4. Third Row: type Surname into the third row.VARCHAR(45)

5. Fourth Row: type Gender into the fourth row.VARCHAR(45)

6. Fifth Row : type Salary into the fifth row.VARCHAR(45)

After that click `Apply` at the bottom of the row.

Then a window that shows the review of the table pops up on the screen. Click Apply, if it's OK.
```
- Add another table via SQL command:

```sql
CREATE TABLE `techproeducation`.`Personal_Info` (
  `ID_number` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Surname` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `Age` INT NULL,
  `Department` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_number`));
```

- Then refresh the "Table" tab to see newly created tables 

- Add data to the "Personal_Info" table as shown below:

```sql
INSERT INTO techproeducation.Personal_Info
(ID_number, Name, Surname, Gender)
VALUES
('1234','Nedim','techproeducation','Male'), ('56789','Ekrem','techproeducation','Male'), ('007','Refia','techproeducation','Female');
```

- Write a query to show all data in the `Personal_Info` table

```sql
SELECT * FROM techproeducation.Personal_Info;
```
**1. Creating a Database:**

```sql
CREATE DATABASE School;
```

**2. Switch to the `School` database:**

```sql
USE School;
```

**3. Creating a Table - `Students`:**

```sql
CREATE TABLE Students (
    studentID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    age INT,
    gradeLevel VARCHAR(50)
);
```

**4. Inserting data into the `Students` table:**

```sql
INSERT INTO Students (firstName, lastName, age, gradeLevel)
VALUES ('John', 'Doe', 18, 'Senior'),
       ('Jane', 'Smith', 17, 'Junior'),
       ('Tom', 'Brown', 16, 'Sophomore');
```

**5. Selecting data from the `Students` table:**

```sql
SELECT * FROM Students;
```

This will show all students in the table.

**6. Using `WHERE` clause to filter data:**

```sql
SELECT * FROM Students WHERE gradeLevel='Senior';
```

This will only show students who are in the 'Senior' grade level.

**7. Using `WHERE` with multiple conditions:**

```sql
SELECT * FROM Students WHERE age > 16 AND gradeLevel='Senior';
```

This will show students who are older than 16 and are in the 'Senior' grade level.

You can build on these basics by exploring more advanced queries and SQL functionalities such as JOINs, GROUP BY, ORDER BY, etc.
- Delete the table 

Show that there is no delete option . Instead, we'll use "Drop"


- Try to delete RDS and show that RDS instance can not be deleted because of the `Deletion Protection`.

- Modify DB instance for "Disabling Deletion Protection"

- Try to delete RDS and show that RDS instance again.

   -Show that "Create final snapshot?" option should be "Unchecked"
       
              "I acknowledge...." flag is "Checked"

 - Type "delete me" nad Click "Delete".

 - Show that Automated Backups are deleted also.
