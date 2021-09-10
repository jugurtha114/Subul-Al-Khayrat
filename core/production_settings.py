
######################### Production Settings #####################
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-85n^9r3d3-msw$@^&646kvy+njhx=#fi--9^7nbgytmsz08u6^'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'subul_al_khayarat_db', # le nom de notre base de donnees creee precedemment
        'USER': 'jugu', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': '01140114',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}