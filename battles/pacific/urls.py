from django.conf.urls import patterns, include, url
from battles.pacific import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'main/$', views.MainView.as_view()),
)
