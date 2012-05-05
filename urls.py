handler500 = 'views.server_error'
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/v1/', include('fiber.api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'extra_context': {'section': 'main'}, 'template': 'default.html'}),
    (r'^fluid/$', 'direct_to_template', {'extra_context': {'section': 'main'}, 'template': 'fluid.html'}),
)

#rosetta urls
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^rosetta/', include('rosetta.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT,'show_indexes': True}),
        (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}),
)

urlpatterns += patterns('',
    (r'', 'fiber.views.page'),
)
