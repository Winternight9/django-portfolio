# django-portfolio
Software Architecture Portfolio Assignment#1

---

## Supakorn Tangpremsri 6110545651

---
## **Prerequisite**
- `Python (ver.3.7 or newer)` [download site](https://www.python.org/downloads/)
- `Python modules listed in ` [requirement file](requirements.txt)

---
## **Installation**

First create .env file containing these following configs:
```
SECRET_KEY =YOURSECRETKEY
```

Second create and activate virtual environment (optional):
```
virtualenv venv
source venv/bin/activate
```

Next install required packages using the following command:
```
pip install -r requirements.txt 
```

Create the migration file using the following command:
```
python manage.py makemigrations
```

Create the database using the following command:
```
python manage.py migrate
```

Collects static files from each of your applications
```
python manage.py collectstatic
```

## **Runing Locally**

Use the following command to run the app locally:

p.s. default port is 8000

```
python manage.py runserver
```