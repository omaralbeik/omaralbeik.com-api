from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post


@admin.register(Post)
class BlogAdmin(MarkdownxModelAdmin):
    search_fields = ("title", "summary", "text", "tags",)
    list_filter = ("tags__name", "is_published",)
    list_display = (
        "title",
        "slug",
        "summary",
        "date_created",
        "date_published",
        "is_published",
    )

    class Media:
        css = {"all": ("markdownx.css",)}
