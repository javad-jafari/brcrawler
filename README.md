
# brcrawler

This web service is a simple crawler to get data from 
Tehran Securities Exchange Technology Management Co
and use **celery** , **celery beat** .

implement periodic task in three ways and two resolution
second, minute.

for minute resolution , **crantab** from schedule module used
but ,second try an custom decorator to check time limition
in fact , assuming that our periodic task should work on 
saturday until wendsday every 1 , 10, 60 second(s) between
8:30 am - 12:30 am


# install and using app

clone project from github

make virtualenv and activate it :
```
source venv/bin/actiate
```

install requierments from req.text :
```
pip install -r req.text
```

run celery and celery beat and redis (use as a broker )

```
linux >> celery -A proj worker -l info
```
```
windows >> celery -A proj worker -l info --pool=solo
```

```
celery -A proj beat -l info
```

run django on 8000:

```
python manage.py runserver
```
## migrations django and celery beat

for better using of app should migrate to settle models in db
some of them are for Clusters and some of them are about
celery beat

## database 

default backend dbms is sqlite3 but can use any of rdbms
like ; postgres, mysql, mariadb


## Broker

In this proj ,using **redis** as broker but can use other famuse 
brokers , rabbitmq ,...

## .env file 

have to touch a .env file in root of proj and set these data :

SECRET_KEY 
DEBUG 
ALLOWED_HOSTS 
CELERY_BROKER_URL
CELERY_RESULT_BACKEND
CELERY_ACCEPT_CONTENT
CELERY_TASK_SERIALIZER
CELERY_RESULT_SERIALIZER
CELERY_TIMEZONE 

## issues or pull requests

if you're going to make it better , you can do this .



