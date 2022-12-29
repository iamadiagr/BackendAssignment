
# Backend Assignment

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.


## Aim of the project

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

The server fetches latest videos async after every 1 minute and saves it to the database.

This project is completely based on Django.

## Task queue and message broker used

Used [Celery](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) to fetch videos after every 60 seconds using YouTube data v3 API

Used [Redis](https://redis.io/) as a message broker.

## Setup Guide

- Clone this project
- As this project is based in Django, you need to have a proper python setup, [refer this](https://www.python.org/)
- Create and activate your virtual environment
- Go to the project using terminal and install all the dependencies using `pip install requirements.txt`
- Inside the setting.py file, fill the variable YOUTUBE_API_KEYS the API Key available.
- Migrate all your models into the database using 
```
    python manage.py makemigrations
    python manage.py sqlmigrate project 001
    python manage.py migrate
```
- Run the server using `python manage.py runserver`
- Run celery `celery -A project worker --pool=solo -l info` - Separate terminal tab
- Run celery async process using `celery -A project beat -l info` - Separate terminal tab
