import os
from django.core.wsgi import get_wsgi_application


BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.admin',
    'preferences',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # first makes sense
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                #'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                #'django.template.context_processors.media',
                'django.template.context_processors.static',
                #'django.template.context_processors.tz'
            ),
        },
    },
]


SECRET_KEY = 'testsecretkey'

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
application = get_wsgi_application()
