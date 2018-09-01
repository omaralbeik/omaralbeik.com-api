from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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


    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try: # retrieve post by primary key
            pk = int(pk)
            post = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(post)
            return Response(serializer.data)

        except: # retrieve post by slug
            post = get_object_or_404(queryset.filter(slug=pk))
            serializer = self.get_serializer(post)
            return Response(serializer.data)