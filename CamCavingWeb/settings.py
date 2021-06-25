"""
Django settings for CamCavingWeb project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ji7t3y^b!-a9(v*6(cj&+l-hs_f6ge0f1*_w8g#bf$xr*b#e5'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['localhost', 'caving.soc.srcf.net']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'UserPortal',
    'Blog',
    'Bank',
    'Gear',
    'cookielaw',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CamCavingWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'CamCavingWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

from CamCavingWeb import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.NAME,
        'USER': config.USER,
        'PASSWORD': config.PASSWORD,
        'HOST': config.HOST,
        'PORT': config.PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

REMOTE_MEDIA_URL = "http://cucc.survex.com/media/"


DEBUG = os.environ['DJANGO_DEBUG'] == 'TRUE'
if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'Media')
    # STATIC_ROOT = os.path.join(BASE_DIR, 'Static')
    STATIC_ROOT_DIR = os.path.join(BASE_DIR, 'Static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "Static"),
    ]
    SSH_PATH = os.path.join(os.path.expanduser("~"), ".ssh")
else:
    STATIC_ROOT = '/societies/caving/public_html/'
    STATIC_URL = '/'
    MEDIA_ROOT = '/societies/caving/public_html/Media/'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    STATIC_ROOT_DIR = STATIC_ROOT
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "Static"),
        os.path.join(BASE_DIR, "Archive"),
    ]
    SSH_PATH = "/societies/caving/.ssh"

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
            },
        },
        'handlers': {
            # Send all messages to console
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
            # Send info messages to syslog
            # 'syslog':{
            #     'level':'INFO',
            #     'class': 'logging.handlers.SysLogHandler',
            #     'facility': SysLogHandler.LOG_LOCAL2,
            #     'address': '/dev/log',
            #     'formatter': 'verbose',
            # },
            # # Warning messages are sent to admin emails
            # 'mail_admins': {
            #     'level': 'WARNING',
            #     'filters': ['require_debug_false'],
            #     'class': 'django.utils.log.AdminEmailHandler',
            # },
            # # critical errors are logged to sentry
            # 'sentry': {
            #     'level': 'ERROR',
            #     'filters': ['require_debug_false'],
            #     'class': 'raven.contrib.django.handlers.SentryHandler',
            # },
        },
        'loggers': {
            # This is the "catch all" logger
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }

X_FRAME_OPTIONS = 'DENY'



MEDIA_URL = '/Media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "SentMail")
EMAIL_HOST = 'mail.gandi.net'
EMAIL_HOST_USER = 'info@camcaving.uk'
EMAIL_HOST_PASSWORD = 'CUCCiagc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'CUCC Server <info@camcaving.uk>'

AUTH_USER_MODEL = 'UserPortal.CustomUser'
LOGIN_REDIRECT_URL = 'UserPortalDashboard'
LOGOUT_REDIRECT_URL = 'Home'