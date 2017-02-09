from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.submit, name='submit'),
    url(r'^success/', views.success, name='success'),
]
