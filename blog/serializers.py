from rest_framework import serializers
import markdown2

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'cover_image_url',
            'summary',
            'text',
            'html_text',
            'is_published',
            'date_published',
        )

    # return post's text as HTML
    def get_html_text(self, post):
        return markdown2.markdown(post.text, extras=['target-blank-links', 'fenced-code-blocks', ])
