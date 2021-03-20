# -*- coding: utf-8 -*-
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'gunicorn',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_OIDOYPAZ'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ.get('DB_HOST', 'oidoypaz-postgresql'),
    }
}
