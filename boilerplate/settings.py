"""
Django settings for cmdb project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, 'logs')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = []

INSTALLED_APPS = (
	'admin_view_permission',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'massadmin',
	'simple_history',
	'hydro',
	'rest_framework',
	'nested_inline',
	'import_export',
	'tagging',
	'tagging_autocomplete',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.RemoteUserMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'simple_history.middleware.HistoryRequestMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'boilerplate.web_auth_backend.HydroRemoteUserBackend',
)

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions, or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissions',
		'rest_framework.permissions.IsAuthenticated',
	]
}

REST_FRAMEWORK_EXTENSIONS = {
	'DEFAULT_USE_CACHE': 'default',
	'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 15
}

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211',
	}
}

ROOT_URLCONF = 'boilerplate.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'TEMPLATE_DEBUG' : False,
		'OPTIONS': {
			'debug': False,
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
			],

			'libraries': {
				'viewtag': 'hydro.templatetags.viewtag',
			}
		},
	},
]


WSGI_APPLICATION = 'boilerplate.wsgi.application'

USE_TZ = True
TIME_ZONE = 'America/New_York'

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en-us'

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
			'datefmt': "%d/%b/%Y %H:%M:%S"
		},
	},
	'handlers': {
		'null': {
			'level': 'DEBUG',
			'class': 'logging.NullHandler',
		},
		'statuslogfile': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(LOG_DIR, 'status.log'),
			'maxBytes': 50000,
			'backupCount': 2,
			'formatter': 'standard',
		},
		'dblogfile': {
			'level': 'INFO',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(LOG_DIR, 'db_sql.log'),
			'maxBytes': 50000,
			'backupCount': 2,
			'formatter': 'standard',
		},
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'standard'
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console'],
			'propagate': True,
			'level': 'WARN',
		},
		'django.db.backends': {
			'handlers': ['dblogfile'],
			'level': 'DEBUG',
			'propagate': False,
		},
		'status': {
			'handlers': ['console', 'statuslogfile'],
			'level': 'DEBUG',
		}
	}
}

from boilerplate.settings_secret import *
