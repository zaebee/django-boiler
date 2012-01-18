handler500 = 'views.server_error'
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'extra_context': {'section': 'main'}, 'template': 'default.html'}),
    (r'^fluid/$', 'direct_to_template', {'extra_context': {'section': 'main'}, 'template': 'fluid.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT,'show_indexes': True}),
)
