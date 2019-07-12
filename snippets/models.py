from django.db import models
from markdownx.models import MarkdownxField


class SnippetManager(models.Manager):
    def get_queryset(self):
        return super(SnippetManager, self).get_queryset().filter(is_published=True)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    icon_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    text = MarkdownxField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateField(blank=True, null=True)

    language = models.ForeignKey('ProgrammingLanguage', on_delete=models.CASCADE)

    objects = models.Manager()
    visible = SnippetManager()

    def __str__(self):
        return self.name if self.is_published else "[DRAFT] " + self.name

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created']
