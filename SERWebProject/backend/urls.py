from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^project_list_display', views.project_list_display, name='project_list_display'),
    url(r'^project_card_display', views.project_card_display, name='project_card_display'),
    url(r'^user_info_submit', views.user_info_submit, name='user_info_submit'),
    url(r'^user_info_request', views.user_info_request, name='user_info_request'),
    url(r'^project_info_request/(?P<project_id>[0-9]+)', views.project_info_request, name='project_info_request'),
    url(r'^project_register/(?P<user_id>[0-9]+)/(?P<project_id>[0-9]+)', views.project_register, name='project_register'),
]
