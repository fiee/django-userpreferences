from django.conf import settings
from django.contrib.auth import get_user_model

SEPARATOR = getattr(settings, 'PREFERENCES_SEPARATOR', '/')

try:
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User