from rest_framework import viewsets
from rest_framework import permissions

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        if self.request.auth:
            return models.Post.objects.all()
        else:
            return models.Post.visible.all()
