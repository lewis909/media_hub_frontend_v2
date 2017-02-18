from .models import AssetMetadata
from django.views.generic import DetailView


class AssetView(DetailView):
    model = AssetMetadata