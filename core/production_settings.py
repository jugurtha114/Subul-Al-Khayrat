import django_heroku
######################### Production Settings #####################
import dj_database_url
from .settings import *
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True# False
TEMPLATE_DEBUG = True#  False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'subul-el-khayarat.herokuapp.com']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jugu-rv85%(tt*w7&wo(xj+euzmr%!qc!3(5evtt$l8jvt@5la0e)=z'

DATABASES['default'] = dj_database_url.config()
