from config.settings.common import *

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app_name',
        'USER': 'app_name',
        'PASSWORD': 'development',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
