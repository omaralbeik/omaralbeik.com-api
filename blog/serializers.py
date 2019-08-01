from rest_framework import serializers
import markdown2
from .models import Post
from omaralbeik import urls


class PostSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    website_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "cover_image_url",
            "cover_image_credit_badge",
            "summary",
            "html_text",
            "date_published",
            "website_url",
            "tags",
        )

    # return post's web URL.
    def get_website_url(self, post):
        return "{}/blog/{}".format(urls.prod_url, post.slug)

    # return post's text as HTML
    def get_html_text(self, post):
        return markdown2.markdown(
            post.text, extras=["target-blank-links", "fenced-code-blocks"]
        )

    # return post's tags.
    def get_tags(self, post):
        return post.tags.all().values("name", "slug")

