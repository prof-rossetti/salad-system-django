# Salad System (Django Implementation)

## Usage

```` sh
git clone git@github.com:gwu-business/salad-system-django.git
cd salad-system-django/
````

Install package dependencies.

```` sh
pip install -r requirements.txt
````

Setup the database.

```` sh
mysql -uroot -p -e "DROP DATABASE IF EXISTS salad_system_db; CREATE DATABASE salad_system_db;"
python manage.py migrate
````

Run a local web server and visit http://localhost:8000/ in a browser.

```` sh
python manage.py runserver
````
