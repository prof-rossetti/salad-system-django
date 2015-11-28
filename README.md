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
python manage.py populate_database
````

Setup an admin user.

```` sh
python manage.py createsuperuser
````

Run a local web server and visit http://localhost:8000/ in a browser.

```` sh
python manage.py runserver
````

![a screenshot of an admin interface to add new records](screenshots/edit_menu_item.png)

![a screenshot of an admin interface to add new records](screenshots/menu_item_validations.png)

![a screenshot of an admin interface dropdown menu for assigning related records](screenshots/related_selections.png)

## Developing

Use an interactive console for development.

```` sh
python manage.py shell
````
