from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '88_jowmp#hf%=3dc2^x^0w@)7squ!f*k)$i_po3#+fw&b-h#^e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
