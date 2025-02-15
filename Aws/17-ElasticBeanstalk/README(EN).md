## Part 1 - Launch an Application

- First, download the `php-v1.zip` and `php-v2.zip` files from GitHub and share them via Slack.

- Navigate to the `Elastic Beanstalk` service in the AWS console.

- Click on `Create Application`.

- Keep the `Environment tier` as `Web server environment`.

- Enter the application name as `MySampleApp`. (You can add application tags if necessary.)

- For the platform, select `PHP`, for the Platform Branch select `PHP 8.2 running on 64bit Amazon Linux 2023`, and for Platform Version select `(Recommended)`.

- For the application code, choose the `Upload your code` option.

- Enter `mysampleapp-source-V1` as the version label and select `Local file`. Then, click on `Choose File` and upload the `php-v1.zip` file.

- Leave the presets as default: `Single instance (free tier eligible)`.

- Click `Next`.

- On the "Configure service access" page:

```bash
- Service role ------ Create and use new service role
- EC2 key pair ------ Select a key.
- EC2 instance profile ------- Create a new profile (IAM role creation required). Select the following policies:

AWSElasticBeanstalkWebTier
AWSElasticBeanstalkWorkerTier
AWSElasticBeanstalkMulticontainerDocker
```
- Click `Next` or skip to review directly.

- Click `Submit` to create the environment.

- Wait for Elastic Beanstalk to create the environment for the application. Show the created resources listed in the console.

- Once the environment is created, click on the provided URL (Application URL) and display the web page.

- Show the `Application` and `Environment` menus on the left sidebar, explain them, and navigate through sections like `Configuration` and `Monitoring`.

- In the AWS console, navigate to the `EC2` service and show the resources created by Elastic Beanstalk:
  - Instances
  - Load Balancers
  - Auto Scaling Groups (ASG)
  - CloudFormation
  - S3 bucket

## Part 2 - Update the Application

### Step 1 - Update the Application

- Navigate to the `Elastic Beanstalk` service in the AWS console.

- Click on `Mysampleapp-env` from the left sidebar and select `Upload and deploy` to update the application. (Alternatively, you can click on `Application versions` in the left menu, upload a new version, and deploy it manually.)

```bash
- Choose file           : php-v2.zip
- Version label         : mysampleapp-source-V2
```
- Wait for Elastic Beanstalk to update the application.

- Once the update is complete, click on the provided URL (Application URL) and display the updated web page.

- Navigate to `Mysampleapp` >> `Application versions` and show that we have one application but two versions.

### Step 2 - Connect to the EC2 instance hosting the App

- Navigate to the `EC2` service in the AWS console.

- Copy the public IP of the instance (`Launched by Elastic Beanstalk`).

- Open your terminal and connect to the instance.

### Step 3 - Scale the Application

- Navigate to `Mysampleapp-env` from the left sidebar and select `Configuration`.

- In the `Instance traffic and scaling` section, click `Edit` to change the auto-scaling group metrics.

```bash
Instances Min: 2
          Max: 4
```

- Click `Apply` to complete the process.

- Revert back to version 1.

- Select `Application versions` from the left menu.

- Choose `mysampleapp-source-V1`, go to `Actions`, and select `Deploy`.

## Part 3 - Terminate the Environment

### Step 1 - Terminate the Environment

- Navigate to the `Elastic Beanstalk` service in the AWS console.

- From the left sidebar, click on `Mysampleapp-env`, go to `Actions`, and select `Terminate environment`. (Alternatively, you can go to `Environments`, select `Mysampleapp-env`, and then click `Actions` > `Terminate environment`.)

- Read the confirmation message, enter the environment name in the box, and click `Terminate`.

- Wait for Elastic Beanstalk to terminate the environment and display events in `Recent events`.

### Step 2 - Restore Environment

- Click `Environments` from the left menu, select the terminated `Mysampleapp-env`, and click `Actions` > `Restore`.
  *Note: The terminated environment remains visible for about an hour.*

- Show that the environment is redeployed and functioning again.

### Step 3 - Delete Application

- Click `Applications` from the left sidebar, select `MySampleApp`, and from the `Actions` menu, choose `Delete application`.

- Enter the application name to confirm, then click `Delete`.

- Wait for the deletion process to complete and show that both the environment and application are removed.

- Explain deployment strategies:

https://blog.shikisoft.com/which_elastic_beanstalk_deployment_should_you_use/

