from django.conf.urls import patterns, include, url
from django.contrib import admin
from battles.pacific.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marinewar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'main/$', MainView.as_view()),
)
