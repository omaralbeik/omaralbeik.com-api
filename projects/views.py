from rest_framework import viewsets
from rest_framework import permissions

from . import models, serializers


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        if self.request.auth:
            return models.Project.objects.all()
        else:
            return models.Project.visible.all()
