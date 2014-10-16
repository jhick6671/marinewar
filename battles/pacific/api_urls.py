from django.conf.urls import patterns, include, url
from battles.pacific import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^pacific$', json_views.BattleCollection.as_view(), name='Pacific'),

)
