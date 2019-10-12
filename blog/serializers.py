from rest_framework import serializers
import markdown2
import readtime
from .models import Post
from omaralbeik import server_variables as sv


class PostSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    website_url = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()
    read_time = serializers.SerializerMethodField()

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
            "read_time",
            "tags",
            "meta",
        )

    # return post's web URL.
    def get_website_url(self, post):
        return "{}/blog/{}".format(sv.CLIENT_PROD_URL, post.slug)

    # return post's text as HTML
    def get_html_text(self, post):
        return markdown2.markdown(
            post.text, extras=["target-blank-links", "fenced-code-blocks"]
        )

    # return post's tags.
    def get_tags(self, post):
        return post.tags.all().values("name", "slug")

    # return post's meta fields.
    def get_meta(self, post):
        return {
            "title": post.title,
            "description": post.summary,
            "keywords": ", ".join([tag.name for tag in post.tags.all()]),
            "canonical": self.get_website_url(post),
        }
    
    # return post's estimated read time.
    def get_read_time(self, post):
        return readtime.of_markdown(post.text).text
