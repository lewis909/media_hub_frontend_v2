from django.conf.urls import url
from django.views.generic import ListView
from asset_db.models import Profiles

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Profiles.objects.all().order_by("id"), template_name='submit/submit.html')),
]
