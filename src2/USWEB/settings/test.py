from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_app_db',
        'USER': 'djangouser',
        'PASSWORD': 'djangouser',
        'HOST': 'usc-12-1303',
        'PORT': '5432'
    }
}
