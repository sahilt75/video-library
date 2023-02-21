from django.db import models
from django.utils.html import format_html


class Video(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=200, null=False)
    channel = models.CharField(max_length=100, null=False)
    thumbnail = models.CharField(max_length=100, null=False)
    published_at = models.DateTimeField('date published', null=False)

    class Meta:
        indexes = [
            models.Index(fields=['-published_at',]),
        ]