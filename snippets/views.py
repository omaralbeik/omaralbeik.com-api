from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route
from . import models, serializers


class SnippetViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get_snippet(self, request, pk=None):
        try: # retrieve snippet by primary key
            pk = int(pk)
            return get_object_or_404(self.get_queryset(), pk=pk)
        except: # retrieve snippet by slug
            return get_object_or_404(self.get_queryset().filter(slug=pk))

    def get_queryset(self):
        if self.request.auth:
            return models.Snippet.objects.all()
        else:
            return models.Snippet.visible.all()

    def retrieve(self, request, pk=None):
        snippet = self.get_snippet(request, pk)
        serializer = self.get_serializer(snippet)
        return Response(serializer.data)


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ProgrammingLanguage.objects.all()
    serializer_class = serializers.ProgrammingLanguageSerializer

    def get_language(self, request, pk=None):
        try: # retrieve language by primary key
            pk = int(pk)
            return get_object_or_404(self.get_queryset(), pk=pk)
        except: # retrieve language by slug
            return get_object_or_404(self.get_queryset().filter(slug=pk))

    def retrieve(self, request, pk=None):
        language = self.get_language(request, pk)
        serializer = self.get_serializer(language)
        return Response(serializer.data)

    # detail route to return all snippets for a language
    # .../languages/[language_id]|[language_slug]/snippets
    @detail_route(methods=['get'])
    def snippets(self, request, pk=None):
        language = self.get_language(request, pk)
        snippets = models.Snippet.visible.filter(language=language)
        page = self.paginate_queryset(snippets)
        serializer = serializers.SnippetSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
