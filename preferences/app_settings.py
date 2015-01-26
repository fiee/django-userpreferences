from django.conf import settings

SEPARATOR = getattr(settings, 'PREFERENCES_SEPARATOR', '/')

try:
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User