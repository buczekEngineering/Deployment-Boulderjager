#!/bin/sh

python /app/manage.py migrate --no-input
python /app/manage.py collectstatic --no-input

cd /app


echo "SUPER_USER_NAME: $SUPER_USER_NAME"
echo "SUPER_USER_PASSWORD: $SUPER_USER_PASSWORD"
echo "SUPER_USER_EMAIL: $SUPER_USER_EMAIL"

DJANGO_SUPERUSER_USERNAME=$SUPER_USER_NAME \
DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD \
DJANGO_SUPERUSER_EMAIL=$SUPER_USER_EMAIL \
python manage.py createsuperuser --noinput

gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8000