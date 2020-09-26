from .base import *
import mimetypes
mimetypes.init()
mimetypes.types_map['.css'] =  'text/css'

DEBUG = False
ALLOWED_HOSTS = ['localhost', 'badges.dscnitrourkela.tech', 'live.dscnitrourkela.tech',]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'https://badges.dscnitrourkela.tech',
    'https://live.dscnitrourkela.tech'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'databases', 'db.sqlite3'),
    }
}