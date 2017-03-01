from django.db import models


class SystemBlog(models.Model):

    title = models.CharField(max_length=256)
    post_date = models.DateTimeField(null=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
