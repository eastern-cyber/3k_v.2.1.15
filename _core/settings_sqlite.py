from .settings import *

# Override to use SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/easterncyber/kokkokkok-auth-api/db.sqlite3',
    }
}
