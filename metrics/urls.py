from django.conf.urls import url
from .views import task_metrics

urlpatterns = [
    url(r'^$', task_metrics, name='metrics'),
]