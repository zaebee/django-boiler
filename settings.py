# Django settings for project project.
import os
import sys

from genericpath import isfile

ugettext = lambda s: s

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('apps'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEFAULT_CHARSET = 'utf-8'

ADMINS = (
    #('zae', 'sinezub@yandex.ru'),
)

MANAGERS = ADMINS
SERVER_EMAIL = 'errors@rpoject.local'

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

STATIC_ROOT = rel('/static/')
STATIC_URL = '/static/'

MEDIA_ROOT = rel('/media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_DIRS = (
    rel('templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',

    'ajax_validation',
    'django_extensions',
    'django_assets',
    'djangosphinx',
    'local',
    'markitup',
    'markdown',
    'pagination',
    'sorl.thumbnail',
    'taggit',

)


MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_AUTO_PREVIEW = 'auto_preview'
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'

ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.dashboard.CustomIndexDashboard'

DEFAULT_FROM_EMAIL = 'no-reply@zaebee.ru'


if isfile(rel('conf/settings_local.py')):
    from conf.settings_local import *
if isfile(rel('conf/local_settings.py')):
    from conf.local_settings import *
