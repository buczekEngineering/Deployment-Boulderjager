#!/bin/sh

python /app/manage.py migrate --no-input
python /app/manage.py collectstatic --no-input

cd /app
ls
gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8000