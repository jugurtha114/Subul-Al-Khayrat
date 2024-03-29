"""
Django settings for subul_al_khayrat project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-85n^9r3d3-msw$@^&646kvy+njhx=#fi--9^7nbgytmsz08u6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#--------------------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
#ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]
#--------------------------------------------------------------------

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    #django-autocomplete-light-3.8.2
    'dal',
    'dal_select2',
    ################################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party APPS
    'debug_toolbar',
    "django_bootstrap5",

    # Local APPS
    'apps.app',
    'apps.authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', ## added from volt
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #django toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',


    # Jugu Middleware
    #'apps.app.middleware.global_request_middleware.GlobalRequestMiddleware',
]



#ROOT_URLCONF = 'subul_al_khayrat.urls'
#-------------------------------------------------------------------------------
ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR_jugu = os.path.join(CORE_DIR, "core/templates")  # ROOT dir for templates
#-------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR_jugu],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI_APPLICATION = 'subul_al_khayrat.wsgi.application'
#WSGI_APPLICATION = 'application' to WSGI_APPLICATION = 'wsgi.application'
WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # on utilise l'adaptateur postgresql
        # le nom de notre base de donnees creee precedemment
        'NAME': 'subul_al_khayarat_db',
        'USER': 'jugu',  # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': '01140114',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(CORE_DIR, 'core/static'),) 
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
#LOGIN_REDIRECT_URL = '/login/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




if(not DEBUG):
    try:
        from .production_settings import *
    except ImportError:
        print('You are using production envirement !')


