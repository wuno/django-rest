from django.conf.urls import url
from .import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^tmdb/$', views.tmdb, name='tmdb'),
  url(r'^rewardstyle/$', views.rewardstyle, name='rewardstyle'),
  url(r'^github/$', views.github, name='github'),
]