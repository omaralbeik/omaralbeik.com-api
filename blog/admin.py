from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post


@admin.register(Post)
class BlogAdmin(MarkdownxModelAdmin):

  class Media:
    css = {
      'all': ('markdownx.css', )
    }