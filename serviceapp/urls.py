from django.conf.urls import url
from .import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^rewardstyle/$', views.rewardstyle, name='rewardstyle'),
  url(r'^admin/', admin.site.urls),
]


