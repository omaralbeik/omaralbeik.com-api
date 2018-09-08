from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()
    image_url = models.URLField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created', ]
