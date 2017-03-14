from django.conf.urls import url
from .views import task_metrics, task_metrics_update

urlpatterns = [
    url(r'^$', task_metrics, name='metrics'),
    url(r'^update/$', task_metrics_update, name='metrics_update'),
]