from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title", "summary", "text", "tags__name",)

    def get_post(self, request, pk=None):
        try:  # retrieve post by primary key
            pk = int(pk)
            return get_object_or_404(self.get_queryset(), pk=pk)
        except:  # retrieve post by slug
            return get_object_or_404(self.get_queryset().filter(slug=pk))

    def get_queryset(self):
        if self.request.auth:
            return models.Post.objects.all()
        else:
            return models.Post.visible.all()

    def retrieve(self, request, pk=None):
        post = self.get_post(request, pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    # detail route to return related posts for a post
    # .../blog/[post_id]|[post_slug]/related
    @action(detail=True, methods=["get"])
    def related(self, request, pk=None):
        post = self.get_post(request, pk)
        page = self.paginate_queryset(post.related.all())
        serializer = serializers.PostSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
