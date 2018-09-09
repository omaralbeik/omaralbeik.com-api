from rest_framework import serializers
import markdown2
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            'id',
            'title',
            'slug',
            'image_url',
            'text',
            'html_text'
        )

    # return post's text as HTML
    def get_html_text(self, post):
        return markdown2.markdown(post.text, extras=['target-blank-links', 'fenced-code-blocks', ])
