from django.db import models
from markdownx.models import MarkdownxField


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter(is_published=True)


class Post(models.Model):
    title = models.CharField(max_length=255)

    # used for url names
    slug = models.SlugField(max_length=255, unique=True)

    summary = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # markdown text, API will serve this as HTML!
    text = MarkdownxField()

    # API will not serve the post unless published is set to True
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True)

    objects = models.Manager()
    visible = PostManager()

    def __str__(self):
        return self.title if self.is_published else  "[DRAFT] " + self.title

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]
