from .base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '134.209.150.112', 'badges.dscomg.com',]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'https://dscomg.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}