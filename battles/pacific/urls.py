from django.conf.urls import patterns, url, include
from battles.pacific import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'main', views.MainView.as_view(), name="main"),
    url(r'warmap/$', views.CampaignMapView.as_view(), name="war_maps"),
    url(r'history', views.HistoryView.as_view(), name="history"),
    url(r'battle/(?P<pk>\d+)/$', views.BattleMapView.as_view(), name="battle"),\
    url(r'links', views.LinkView.as_view(), name="links"),

)
