# Django settings for project project.
import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('zae', 'sinezub@yandex.ru'),
)

MANAGERS = ADMINS
SERVER_EMAIL = 'errors@rpoject.local'
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
SITE_ID = 1
USE_I18N = True

STATIC_ROOT = MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')
MEDIA_URL = '/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
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
    'tagging',
    'tinymce',

)


TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "fullscreen,images,preview",
    'theme_advanced_buttons1': "images,bold,italic,underline,formatselect,link,unlink,justifyleft,justifycenter,justifyright,pasteword,pastetext,image,|,bullist,numlist,|,undo,redo,|,preview,code,fullscreen",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'language': "ru",
    'external_image_list_url': 'images/',
    'external_link_list_url': 'links/',
}

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_AUTO_PREVIEW = 'auto_preview'
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'

ADMIN_TOOLS_INDEX_DASHBOARD = 'conf.dashboard.CustomIndexDashboard'

SPHINX_API_VERSION = 0x116

DEFAULT_FROM_EMAIL = 'no-reply@zaebee.ru'

from conf.run import *
