from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Content


@admin.register(Content)
class ContentAdmin(MarkdownxModelAdmin):
    search_fields = ("title", "slug", "summary",)
    list_display = (
        "title",
        "slug",
        "date_created",
    )

    class Media:
        css = {"all": ("markdownx.css",)}
