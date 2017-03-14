from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_task, name='user_task'),
    url(r'^update/$', views.user_task_update, name='user_task'),
]
