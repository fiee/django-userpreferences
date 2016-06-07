from django.conf import settings

SEPARATOR = getattr(settings, 'PREFERENCES_SEPARATOR', '/')
INDEX_VIEW_ENABLED = getattr(settings, 'PREFERENCES_INDEX_VIEW_ENABLED', True)

try:
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User
