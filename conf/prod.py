from settings import PROJECT_PATH

DATABASES = {
    'chikago': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '@v=SY{~0VM%x)nW;b"@!X/-10DCmmx7R9FhTpFy)'

CACHE_BACKEND = 'file://%s/tmp/django_cache?timeout=12000&max_entries=400' % PROJECT_PATH


#AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = False
