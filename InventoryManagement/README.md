# Inventory Management System
Kiratech Backend Developer

## Setup Django and Database
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser account
```
python manage.py createsuperuser
```
Enter your username and password

## Load data
```
python manage.py loaddata supplier
```

## Run Server
```
python manage.py runserver
```

## Test
```
python manage.py test
```

## URLs
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/inventory/


### API Endpoints
- http://127.0.0.1:8000/api/inventory/
- http://127.0.0.1:8000/api/inventory/<id\>/
- http://127.0.0.1:8000/api/supplier/
- http://127.0.0.1:8000/api/supplier/<id\>/
