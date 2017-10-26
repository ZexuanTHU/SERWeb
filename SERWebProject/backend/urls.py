from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^$', views.projreg, name='projreg'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<project_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<project_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login')
]
