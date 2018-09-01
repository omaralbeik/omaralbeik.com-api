from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Project

# register post model with admin dashboard.
admin.site.register(Project)
