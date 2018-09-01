from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post

# register post model with admin dashboard with markdown support
admin.site.register(Post, MarkdownxModelAdmin)
