import os
import sys
from pathlib import Path

import dj_database_url
import environ

CONFIG_DIR = Path(__file__).resolve().parent
BASE_DIR = CONFIG_DIR.parent


##########################################################################################
# Environment
# https://django-environ.readthedocs.io/en/latest/quickstart.html
##########################################################################################
env = environ.Env()

# Take environment variables from .env file (if it exists)
# That's why it is important to NOT version .env file
# (otherwise prod environment will get local env file values!)
environ.Env.read_env(os.path.join(CONFIG_DIR, ".env"))

##########################################################################################
# Security
##########################################################################################

SECRET_KEY = env("DJ_SECRET_KEY")
DEBUG = env("DJ_DEBUG", cast=bool)
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["*"]  # To edit according your hosting platform

##########################################################################################
# Apps definition
##########################################################################################

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
]

APP_FOLDER = "dj_apps"

# Create apps in dj_apps folder sothat they are automatically detected
MY_APPS = os.listdir(BASE_DIR / Path(APP_FOLDER))

# Adding apps to the path is required for auto import
for new_path in [APP_FOLDER] + [f"{APP_FOLDER}/{folder}" for folder in MY_APPS]:
    sys.path.insert(0, os.path.join(BASE_DIR, new_path))

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # to handle CORS with right headers
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"
WSGI_APPLICATION = "config.wsgi.application"


##########################################################################################
# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
##########################################################################################

DATABASES = {"default": dj_database_url.config(env="DJ_DATABASE_URL", conn_max_age=600)}

##########################################################################################
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
##########################################################################################

LANGUAGE_CODE = "fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_L10N = True
USE_TZ = True

##########################################################################################
# Templates (required for admin dashboard)
##########################################################################################

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

##########################################################################################
# Static files
# https://docs.djangoproject.com/en/dev/howto/static-files/
##########################################################################################

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

##########################################################################################
# Misc
##########################################################################################

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
