from __future__ import absolute_import, print_function, unicode_literals

import os

from django.core.wsgi import get_wsgi_application


BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'preferences',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

SECRET_KEY = 'testsecretkey'

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
application = get_wsgi_application()
