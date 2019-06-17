from rest_framework import serializers

from .models import Project, Technology


class TechnologySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Technology
        fields = (
            'id',
            'name',
            'slug',
            'icon_url'
        )


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'slug',
            'logo_url',
            'summary',
            'is_published',
            'date_published',
            'url_name',
            'url',
            'tags',
            'technologies'
        )

    # return project's tags.
    def get_tags(self, project):
        return project.tags.all().values('name', 'slug')

    # return project's technologies.
    def get_technologies(self, project):
        return project.technologies.all().values('name', 'slug', 'icon_url')