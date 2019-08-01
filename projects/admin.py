from django.contrib import admin
from .models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ("name", "slug",)
    list_display = (
        "name",
        "slug",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name", "slug", "summary", "technologies", "tags",)
    list_filter = ("technologies__name", "tags__name", "is_published",)
    list_display = (
        "name",
        "slug",
        "summary",
        "date_created",
        "date_published",
        "is_published",
    )
