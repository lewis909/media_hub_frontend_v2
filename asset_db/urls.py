from django.conf.urls import url
from .views import AssetView, task_status, assets_in_repo, file_list

urlpatterns = [
    url(r'^(?P<pk>\d+)$', AssetView.as_view(template_name='assets_db/asset_info.html'), name='AssetView'),
    url(r'^task/$', task_status, name='task'),
    url(r'^file_list/$',file_list , name='file_list'),
    url(r'^$', assets_in_repo, name='repo'),
]