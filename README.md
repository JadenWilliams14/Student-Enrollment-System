# Student-Enrollment-System

## How to set up the project

1. Navigate to the 'myproject' folder in terminal after downloading
2. Create a virtual environment: PS> `python -m venv venv` and then `source venv/bin/activate` or `venv\Scripts\activate`
3. PS> `pip install -r requiremnts.txt`

## How to create .env file

1. Adjust the env.example file from GitHub Repository and save it as .env
2. Within the '' from SECRET_KEY, add your SECRET_KEY or create one using PS> `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` and input what is displayed in terminal for it
3. Replace the DATABASE_URL variable with one that has a DB_USER and password for that user that has access to a DB_NAME that you provide. You will have connect to this database using a HOST and PORT that you will also provide.

## How to run migrations

1. PS> `python manage.py makemigrations myapp`
2. PS> `python manage.py migrate`
3. PS> `python manage.py createsuperuser`
4. PS> `python manage.py runserver`
   now if you go to '{development server}/admin' in a browser you can add and edit data to the Database.
