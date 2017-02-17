from django.conf.urls import url
from django.views.generic import ListView
from asset_db.models import AssetMetadata, Task

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=AssetMetadata.objects.all().order_by("id"), template_name='assets_db/assets.html')),
    url(r'^task/$', ListView.as_view(queryset=Task.objects.all().order_by("-id"), paginate_by=50, template_name='assets_db/task.html'), name='task')
]