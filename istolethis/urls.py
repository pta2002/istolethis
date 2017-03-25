from django.conf.urls import url, include
from . import views

app_name = 'istole'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^play/(?P<id>\d*[1-9]\d*)/$', views.play, name='play'),
    url(r'^manage/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        views.manage, name='manage'),
    url(r'^manage/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/stop/$',
        views.stop, name='stop'),
]
