# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += (
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
