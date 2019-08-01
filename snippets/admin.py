from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import ProgrammingLanguage, Snippet


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    search_fields = ("name", "slug",)
    list_display = ("name", "slug",)

    class Media:
        css = {"all": ("markdownx.css",)}


@admin.register(Snippet)
class SnippetsAdmin(MarkdownxModelAdmin):
    search_fields = ("name", "slug", "summary", "text", "language",)
    list_filter = ("language__name", "is_published",)
    list_display = (
        "name",
        "slug",
        "summary",
        "date_created",
        "date_published",
        "is_published",
        "language",
    )

    class Media:
        css = {"all": ("markdownx.css",)}
