from rest_framework import serializers
from .models import Project, Technology
from omaralbeik import server_variables as sv


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("id", "name", "slug", "icon_url",)


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    technologies = serializers.SerializerMethodField()
    website_url = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "slug",
            "logo_url",
            "summary",
            "is_published",
            "date_published",
            "url_name",
            "url",
            "tags",
            "website_url",
            "technologies",
            "meta",
        )

    # return project's web URL.
    def get_website_url(self, project):
        return "{}/projects".format(sv.CLIENT_PROD_URL)

    # return project's tags.
    def get_tags(self, project):
        return project.tags.all().values("name", "slug")

    # return project's technologies.
    def get_technologies(self, project):
        return project.technologies.all().values("name", "slug", "icon_url")

    # return project's meta fields.
    def get_meta(self, project):
        return {
            "title": project.name,
            "description": project.summary,
            "keywords": ", ".join([tag.name for tag in project.tags.all()]),
            "canonical": self.get_website_url(project),
        }
