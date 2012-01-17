#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, PROJECT_PATH)
sys.path.insert(0, os.path.join(PROJECT_PATH, 'apps'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# ------ Ниже этой линии изменения скорее всего не нужны --------

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
