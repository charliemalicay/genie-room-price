# django-room-price-genie

## Requirements
- [ ] [Python-3 or higher](https://www.python.org/)
- [ ] [pipenv](https://pipenv.pypa.io/en/latest/installation.html)
- [ ] [MySQL](https://dev.mysql.com/)

## Install Packages
```
pipenv install
```

## Configuration
### .env file
```
# Django settings
SECRET_KEY=[django-secret-key]
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# MySQL settings
MYSQL_ROOT_PASSWORD=[database-root-password]
MYSQL_DATABASE=[database-name]
MYSQL_USER=[database-username]
MYSQL_PASSWORD=[database-password]
MYSQL_PORT=[database-port]
```

## Initialize

```
cd src
cd genie_project
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py loaddata data.json
```

## Run Project
```
pipenv run python manage.py runserver
```

## Access Swagger this API
```
GET
http://127.0.0.1:8000/dashboard?hotel_id={hotel id}&period_month={month}&period_day={day}&period_year={year}
http://127.0.0.1:8000/events?hotel_id={hotel id}&rpg_status={1 or 2}&room_id={room id}&updated__gte={timestamp from}&updated__lte={timestamp to}&night_of_stay__gte={night of stay from}&night_of_stay__lte={night of stay to}

POST
http://127.0.0.1:8000/events/

JSON BODY

{
    "room_id": "2",
	"night_of_stay": "2024-10-24", 
	"rpg_status": 1, 
	"timestamp": "2024-10-24T12:42:33Z", 
	"hotel_id": 3009
}
```
