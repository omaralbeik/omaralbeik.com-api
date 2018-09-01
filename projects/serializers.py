from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'summary',
            'is_published',
            'date_published',
            'url_name',
            'url',
        )