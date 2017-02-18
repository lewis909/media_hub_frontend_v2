from django.conf.urls import url
from django.views.generic import ListView, DetailView
from asset_db.models import AssetMetadata, Task
from .views import AssetView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=AssetMetadata.objects.all().order_by("id"), paginate_by=50, template_name='assets_db/assets.html')),
    url(r'^(?P<pk>\d+)$', AssetView.as_view(template_name='assets_db/asset_info.html'), name='AssetView'),
    url(r'^task/$', ListView.as_view(queryset=Task.objects.all().order_by("-id"), paginate_by=50, template_name='assets_db/task.html'), name='task')
]