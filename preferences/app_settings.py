from django.conf import settings

SEPARATOR = getattr(settings, 'PREFERENCES_SEPARATOR', '/')
STRICT_CHOICES = getattr(settings, 'PREFERENCES_STRICT_CHOICES', True)
