"""
WSGI config for the hire99 project.

It tells the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Added for Heroku deployment
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hire99.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
