# -*- coding: utf-8 -*-
"""
DEBUG=True to run project in development mode.
DEBUG=False to run project in production mode,
"""
DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    from conf.dev import *
else:
    from conf.prod import *

