from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

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
            'tags'
        )

    # return project's tags.
    def get_tags(self, post):
        return post.tags.all().values('name', 'slug')