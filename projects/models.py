from django.db import models


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset().filter(is_published=True)


class Project(models.Model):
    name = models.CharField(max_length=255)

    summary = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)

    url_name = models.CharField(max_length=50, default='Website')
    url = models.URLField()

    # API will not serve the post unless published is set to True
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True)

    objects = models.Manager()
    visible = ProjectManager()

    def __str__(self):
        return self.name if self.is_published else  "[DRAFT] " + self.name

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]
