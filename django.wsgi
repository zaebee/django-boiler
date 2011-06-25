#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
# По умолчанию используется версия Django 1.2.5,
# если вы хотите использовать другие версии, закомментируйте строку ниже и раскомментируйте нужную вам версию.
sys.path.insert(0, '/opt/django-1.2/lib/python2.5/site-packages')

# Раскомментировать для версии Django 1.3
# sys.path.insert(0, '/opt/django-1.3/lib/python2.5/site-packages')

# Если закомментировать все версии, будет использоваться версия, установленная на сервере.

# Добавьте нужные вам пути поиска.
# Если вы получаете ошибку 500 Internal Server Error,
# скорее всего проблема именно в путях поиска.

sys.path.insert(0, PROJECT_PATH)
sys.path.insert(0, os.path.join(PROJECT_PATH, 'apps'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# ------ Ниже этой линии изменения скорее всего не нужны --------

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
