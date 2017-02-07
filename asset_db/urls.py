from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from asset_db.models import AssetMetadata

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=AssetMetadata.objects.all().order_by("id")[:10], template_name='assets_db/assets.html'))
]