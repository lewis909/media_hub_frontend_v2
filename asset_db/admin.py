from django.contrib import admin
from asset_db.models import AssetMetadata, Profiles, Task, FileRepo

admin.site.register(AssetMetadata)
admin.site.register(Profiles)
admin.site.register(Task)
admin.site.register(FileRepo)
