from django.db import models
from taggit.managers import TaggableManager


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset().filter(is_published=True)


class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    icon_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    logo_url = models.URLField(blank=True, null=True)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    url_name = models.CharField(max_length=50, default="Website")
    url = models.URLField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    tags = TaggableManager(blank=True)

    objects = models.Manager()
    visible = ProjectManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-is_published", "-date_published", "-date_created"]
