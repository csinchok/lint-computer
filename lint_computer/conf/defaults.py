from django.conf.global_settings import *  # noqa

import hashlib
import os
import os.path
import socket
import sys

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = ()

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

APPEND_SLASH = False

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))

sys.path.insert(0, os.path.normpath(os.path.join(PROJECT_ROOT, os.pardir)))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lint.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_SUBJECT_PREFIX = '[Lint Computer] '

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

USE_TZ = True

# Make this unique, and don't share it with anybody.
KEY_COMPONENT = ")*)&8a^6)6%72e@-ne5(-!8a(vv#)kv)eyg&@m=zd^pl!7=y@".encode("utf-8")
SECRET_KEY = hashlib.md5(socket.gethostname().encode("utf-8") + KEY_COMPONENT).hexdigest()

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'betty.conf.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'lint_computer.core'
)

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"

STATIC_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, 'static'))
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

CLONE_DIRECTORY = os.path.join(PROJECT_ROOT, '..', 'clones')
