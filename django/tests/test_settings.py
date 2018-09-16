SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'core',
    'tests',
    'django.contrib.contenttypes',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ':memory:',
    }
}

TEST_RUNNER = "redgreenunittest.django.runner.RedGreenDiscoverRunner"

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
