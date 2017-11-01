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
    url(r'^login', views.login, name='login'),
    url(r'^project_list_display', views.project_list_display, name='project_list_display'),
    url(r'^project_card_display', views.project_card_display, name='project_card_display'),
    url(r'^user_info_submit', views.user_info_submit, name='user_info_submit'),
]
