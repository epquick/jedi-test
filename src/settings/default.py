#! /usr/bin/env python2.7
import os
import sys

# Django settings for ProjectName project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = not DEBUG

ALLOWED_HOSTS = ['*']

# Absolute paths for where the project and templates are stored.
ABS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABS_TEMPLATES_PATH = os.path.join(ABS_ROOT, 'templates')

# add root directory to PYTHONPATH
# if not ABS_ROOT in sys.path:
#     sys.path.insert(0, ABS_ROOT)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/root_admin/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ABS_ROOT, 'static-collected')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(ABS_ROOT, 'static/'),
)
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(ABS_ROOT, 'media')

# The URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'

# Additional locations of static files
STATICFILES_DIRS = (
    #'%s/static-assets' % ABSOLUTE_PROJECT_ROOT,
)

ADMINS = (
    ('Your Name', 'admin@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'compressor.finders.CompressorFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '!!! paste your own secret key here !!!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ip_log.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/root_admin/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ABS_TEMPLATES_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
)

# django
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ip_log',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres-host',
        'PORT': 5432,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ABS_ROOT, 'iplog.log'),
            'maxBytes': 1024 * 1024 * 5, # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

IP_LOG_DEFAULT_LIMIT = 1000
IP_LOG_MAX_LIMIT = 1000


   
