from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from asset_db.models import AssetMetadata, Task

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=AssetMetadata.objects.all().order_by("id")[:10], template_name='assets_db/assets.html')),
    url(r'^task/$', ListView.as_view(queryset=Task.objects.all().order_by("id")[:10], template_name='assets_db/task.html',), name='task')
]