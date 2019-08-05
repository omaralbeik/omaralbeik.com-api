from rest_framework import serializers
import markdown2
from .models import Content
from omaralbeik import server_variables as sv


class ContentSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    html_text = serializers.SerializerMethodField()
    website_url = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            "id",
            "title",
            "slug",
            "image_url",
            "summary",
            "text",
            "html_text",
            "website_url",
            "tags",
            "meta",
        )

    # return content's web URL.
    def get_website_url(self, content):
        return "{}/{}/".format(sv.CLIENT_PROD_URL, content.slug)

    # return content's text as HTML
    def get_html_text(self, content):
        return markdown2.markdown(
            content.text, extras=["target-blank-links", "fenced-code-blocks"]
        )

    # return content's tags.
    def get_tags(self, content):
        return content.tags.all().values("name", "slug")

    # return content's meta fields.
    def get_meta(self, content):
        return {
            "title": content.title,
            "description": content.summary,
            "keywords": ", ".join([tag.name for tag in content.tags.all()]),
            "canonical": self.get_website_url(content),
        }
