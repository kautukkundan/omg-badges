from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']

CORS_ORIGIN_WHITELIST =['http://localhost:3000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'databases', 'db.sqlite3'),
    }
}