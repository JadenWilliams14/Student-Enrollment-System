# Student-Enrollment-System

## How to build and run the application
1. Make sure that you have Docker Engine and Dcocker Compose V2 installed on your machine and open docker desktop
2. Navigate to the terminal path that contains your 'myproject' folder
3. Run `docker compose build`
4. Run `docker compose up -d`

## How to set up .env file
1. Copy the information in env.example and paste it into a .env file at the same level
2. Replace all of the variables besides DEBUG with values relevant to your set-up
   
   a. If you need a secret_key generate one using `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` in terminal

   b. Replace database information with your corresponding database and user information

   c. You will need to get Google_Client information through google

## How to run migrations
 - Type `docker compose exec web python manage.py migrate` into terminal

## How to access the running application
1. You will need to create a superuser for the application in order to use CRUD operations on the model objects

   a. Type `docker ps` to see the name of the containers

   b. Run `docker exec -it <container_name> bash` on the web container (for me it was django_web)

   c. Within the bash type `python manage.py createsuperuser` and go through the steps to create user
3. In a browser type `localhost:8000/myapp` into the address bar
4. This will redirect you to the login page where you can login using your newly created user
5. Now you have access to the application and can add new students using the webpage
6. To access the api go to `localhost:8000/api/students/` 
