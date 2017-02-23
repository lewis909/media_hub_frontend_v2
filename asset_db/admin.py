from django.contrib import admin
from asset_db.models import AssetMetadata, Profiles, Task, FileRepo
from system_blog.models import SystemBlog

admin.site.register(AssetMetadata)
admin.site.register(Profiles)
admin.site.register(Task)
admin.site.register(FileRepo)
admin.site.register(SystemBlog)
