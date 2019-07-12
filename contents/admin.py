from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Content


@admin.register(Content)
class ContentAdmin(MarkdownxModelAdmin):
  class Media:
    css = {
      'all': ('markdownx.css')
    }