Setting up / Required installs
Install Python (I happen to be using 3.10.5)
Install Django: 'pip install Django'
Install Mysql: https://dev.mysql.com/downloads/installer/ + 'pip install mysqlclient'
Install Bootstrap v5: 'pip install django-bootstrap-v5'
Create the user and table following the commands in settings.py
Create migrations: 'python .\manage.py makemigrations' and 'python manage.py migrate'
Start the server with 'python manage.py runserver'
Go to 'http://localhost:8000/projects/', check that it says "Welcome to the Lassonde Capstone Inventory Database" and an entry is created in the DB
