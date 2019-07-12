from rest_framework import serializers
import markdown2
from .models import ProgrammingLanguage, Snippet


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProgrammingLanguage
        fields = (
            'id',
            'name',
            'slug',
            'icon_url'
        )


class SnippetSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = (
            'id',
            'name',
            'slug',
            'summary',
            'html_text',
            'date_published',
            'language'
        )

    # return snippet as HTML
    def get_html_text(self, snippet):
        return markdown2.markdown(snippet.text, extras=['fenced-code-blocks'])

    # return snippet's language.
    def get_language(self, snippet):
        serializer = ProgrammingLanguageSerializer(snippet.language)
        return serializer.data
