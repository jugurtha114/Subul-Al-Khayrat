import django_heroku
######################### Production Settings #####################
import dj_database_url
from .settings import *
from pathlib import Path
import os


DEBUG = True# False
TEMPLATE_DEBUG = True#  False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'subul-el-khayarat.herokuapp.com']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES['default'] = dj_database_url.config()

django_heroku.settings(locals())
