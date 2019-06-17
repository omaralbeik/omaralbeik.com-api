from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Project, Technology

admin.site.register(Project)
admin.site.register(Technology)
