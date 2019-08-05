from django.db import models
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager


class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=255, default="", blank=True)
    text = MarkdownxField()
    image_url = models.URLField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created"]
