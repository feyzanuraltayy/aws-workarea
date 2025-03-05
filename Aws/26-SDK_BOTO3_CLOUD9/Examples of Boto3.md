
```bash
pip install boto3
```

### Example 1: List S3 Buckets
This example lists all the S3 buckets in your account.

```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print("Existing buckets:")
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```

### Example 2: Create an S3 Bucket
This example creates an S3 bucket (Note: S3 bucket names must be globally unique).

```python
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='your-unique-bucket-name')
```
### Example 3: Creating S3 Buckets simultaneously:
```python
import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Create a new bucket
names = ['ali', 'mehmet', 'omer']

for name in names:
    # Bucket names must be unique, you may need to add some uniqueness to the names
    bucket_name = f"{name}-unique-suffix-here"  
    s3.create_bucket(Bucket=bucket_name)
```


### Example 4: Upload a File to S3 Bucket
This example uploads a file to an S3 bucket.


```python
import boto3

s3 = boto3.client('s3')
s3.upload_file('your-local-file.txt', 'your-bucket-name', 'your-s3-object-name.txt')
```
### Example 5: Deleting S3 Buckets

```python
import boto3
# Initialize a session using Amazon S3
s3 = boto3.resource('s3')

# Specify the bucket name
bucket_name = 'your-bucket-name'

# Fetch the bucket
bucket = s3.Bucket(bucket_name)

# Step 1: Delete all objects in the bucket
for obj in bucket.objects.all():
    obj.delete()

# Step 2: Delete the bucket
bucket.delete()

# Confirm that the bucket has been deleted
print(f"Bucket {bucket_name} and all its objects have been deleted.")
```

```python
import boto3

# Initialize a session using Amazon S3
s3 = boto3.resource('s3')

# List all bucket names
bucket_list = [bucket.name for bucket in s3.buckets.all()]
print("Bucket list:", bucket_list)

# Loop to iterate through all buckets
for bucket_name in bucket_list:
    # Initialize the S3 bucket resource
    bucket = s3.Bucket(bucket_name)

    # Delete all objects in the bucket
    for key in bucket.objects.all():
        key.delete()
    print(f"Deleted all objects from bucket {bucket_name}")

    # Delete the bucket itself
    bucket.delete()
    print(f"Deleted bucket {bucket_name}")

```

### Example 6: List EC2 Instances
This example lists all EC2 instances in your account.

```python
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("ID: {}, State: {}, Type: {}".format(
            instance['InstanceId'],
            instance['State']['Name'],
            instance['InstanceType']))
```
### Example 7: Launch an EC2 Instance
```python
import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Instance configuration specifications
instance = ec2.create_instances(
    ImageId='ami-0f409bae3775dc8e5',  # Use an actual AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='rahmatullah_key'  # Use your actual key pair name
)

print(f"Launched instance with ID {instance[0].id}")
```

### Example 8: Start an EC2 Instance
This example starts an EC2 instance.

```python
import boto3

ec2 = boto3.client('ec2')
ec2.start_instances(InstanceIds=['your-instance-id'])
```

### Example 9: Stop instances
```python
import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Initialize EC2 client
client = boto3.client('ec2')

# Get list of all running instances
running_instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# List to store instances to stop
instances_to_stop = []

# Loop through all running instances
for instance in running_instances:
    # Assume it's not a Cloud9 instance
    is_cloud9 = False

    # Check each tag to see if this is a Cloud9 instance
    for tag in instance.tags or []:
        if tag['Key'] == 'aws:cloud9:environment':
            is_cloud9 = True
            break

    # If it's not a Cloud9 instance, add it to the list of instances to stop
    if not is_cloud9:
        instances_to_stop.append(instance.id)

# Stop instances
if instances_to_stop:
    client.stop_instances(InstanceIds=instances_to_stop)
    print(f"Stopped instances: {instances_to_stop}")
else:
    print("No instances to stop.")
```
### Example 10: Terminating instances with exceptions
```python
import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Initialize EC2 client
client = boto3.client('ec2')

# Get list of all instances (you can also filter by only running instances if you prefer)
instances = ec2.instances.all()

# List to store instances to terminate
instances_to_terminate = []

# Loop through all instances
for instance in instances:
    # Assume it's not a Cloud9 instance
    is_cloud9 = False

    # Check each tag to see if this is a Cloud9 instance
    for tag in instance.tags or []:
        if tag['Key'] == 'aws:cloud9:environment':
            is_cloud9 = True
            break

    # If it's not a Cloud9 instance, add it to the list of instances to terminate
    if not is_cloud9:
        instances_to_terminate.append(instance.id)

# Terminate instances
if instances_to_terminate:
    client.terminate_instances(InstanceIds=instances_to_terminate)
    print(f"Terminated instances: {instances_to_terminate}")
else:
    print("No instances to terminate.")
```
### Example 11: Terminating all instances
```python
import boto3

# Initialize EC2 client
client = boto3.client('ec2')

# Get list of all instance IDs
response = client.describe_instances()
instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# Terminate instances
if instance_ids:
    client.terminate_instances(InstanceIds=instance_ids)
    print(f"Terminated instances: {instance_ids}")
else:
    print("No instances to terminate.")
```