#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn -w 2 oidoypaz.wsgi:application -b 0.0.0.0:8000  --log-level error --keep-alive 200 --env DJANGO_SETTINGS_MODULE=oidoypaz.settings
