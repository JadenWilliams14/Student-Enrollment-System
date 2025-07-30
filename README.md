# Student-Enrollment-System

## AWS deployment process
1. With an AWS account, you will need to set up an IAM role to allow for EC2 instance to pull images from ECR later
2. Create an ECR repository
3. Authenticate Docker to ECR (Locally)
4. Build, Tag, Push Image from Local to ECR
5. Lauch and Configure EC2 Instance
6. Modify docker-compose.yml and .env files
7. Pull ECR Image
8. Run application on EC2

### Key AWS services used
1. IAM Role: Securely manage identities and access to AWS services and resources
   a. Navigate to IAM -> Roles -> Create role in the AWS Console
   b. Select AWS service as the trusted entity type and choose EC2 as the use case.
   c. Add Permission AmazonEC2ContainerRegistryReadOnly
2. ECR: Easily store, share, and deploy your container software anywhere
   a. Naviage to Elastic Container Registry in AWS Console
   b. Create a repository with visibility as Private and a descriptive name like: my-django-app
3. EC2: Create, manage, and monitor virtual servers in the cloud
   a. Navigate to EC2 -> Instances -> Launch instances
   b. Give the image a Name, Os, and Instance type: django-deployment-server, Amazon Linux 2023 AMI, t2.micro
   c. Provide/Create Key pair and security group rules
   d. Set IAM role created and Launch instance

### Steps to push docker image to ECR
1. Open local termnial
2. Run AWS CLI command provided by ECR
3. Build the image `docker compose build web`
4. Tag the image using the ECR repository URI
5. Push the tagged image to ECR

### Steps to set up EC2 instance
1. Open local terminal
2. connect to EC2 via SSH `ssh -i /path/to/your-key.pem ec2-user@<public_ip_or_dns>`
3. Install Docker and Dcoker Compose V2 on EC2 
```
sudo yum update -y
sudo yum install -y docker docker-compose-plugin # Installs Docker Engine and Compose V2 plugin
sudo systemctl start docker 
sudo systemctl enable docker # Optional: start docker on boot
sudo usermod -aG docker ec2-user # Add user to docker group
newgrp docker # Activate group changes without logout/login (or exit and reconnect SSH)
# Verify installation
docker --version
docker compose version
```
4. Copy docker-compose.yml and .env files from local machine to EC2 `scp -i /path/to/your-key.pem docker-compose.yml .env <user>@<public_ip_or_dns>` 
5. Modify docker-compose.yml and .env files by SSH into EC2 instance and typing `nano <file_name>` to edit them

### Modifications to docker-compose.yml and .env
1. nano docker-compose.yml
```
version: '3.8'
services:
 web:
   # Use the image from ECR instead of building locally
   image: <aws_account_id>.dkr.ecr.<region>[.amazonaws.com/](https://.amazonaws.com/)<your_repo_name>:latest 
   container_name: django_web
   # Command just starts Gunicorn; migrations run separately
   command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
   # volumes: # REMOVE or comment out the local code mount
   #  - .:/app 
   ports:
     # Map host port 8000 to container port 8000 (Gunicorn)
     - "8000:8000" 
   env_file:
     - .env 
   depends_on:
     - db 

 db:
   image: postgres:16-alpine
   container_name: postgres_db
   volumes:
     - postgres_data:/var/lib/postgresql/data/ 
   env_file:
     - .env 
   # No ports needed here for web service access

volumes:
 postgres_data:
```
2. nano .env
```
SECRET_KEY='your_PRODUCTION_secret_key_here'
DEBUG=False # IMPORTANT: Set to False for production
DATABASE_URL='postgres://your_db_user:your_db_password@db:5432/your_db_name' 
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password

# Add your EC2 public IP and/or DNS name
ALLOWED_HOSTS=your_ec2_public_ip,your_ec2_public_dns_name
# Also add CSRF_TRUSTED_ORIGINS for Django 4.1+ when accessing via IP/DNS
# Use https if you set up HTTPS later
CSRF_TRUSTED_ORIGINS=http://your_ec2_public_ip,http://your_ec2_public_dns_name
```

### How to run application on EC2
1. Pull ECR Image
2. Start Containers `docker compose up -d`
3. Check status and Logs `docker compose ps` and `docker compose logs -f web`
4. Run Migrations `docker compose exec web python manage.py migrate`
5. Open web browser and navigate to `http://<your_ec2_public_ip>:8000` using public ip from EC2 instance
