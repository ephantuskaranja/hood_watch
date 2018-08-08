from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^reports/$', views.get_reports, name='reports'),
    url(r'^recommendations/$', views.get_recommendations, name='recommendations'),
    url(r'^makeReport', views.makeReport, name='make-report'),
]