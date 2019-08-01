from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from rest_framework.routers import SimpleRouter

from blog import views as bv
from projects import views as pv
from snippets import views as sv
from contents import views as cv
from contact import views as ctv

app_name = "omaralbeik"
prod_url = "https://omaralbeik.com"


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r"blog", bv.PostViewSet)
router.register(r"projects", pv.ProjectViewSet)
router.register(r"technologies", pv.TechnologyViewSet)
router.register(r"snippets", sv.SnippetViewSet)
router.register(r"languages", sv.ProgrammingLanguageViewSet)
router.register(r"contents", cv.ContentViewSet)
router.register(r"contact", ctv.MessageViewSet)

urlpatterns = [
    url(r"^markdownx/", include("markdownx.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^v1/", include(router.urls)),
]

# Django should not serve media files in production,
# they should be served by server instead

if settings.DEBUG:
    urlpatterns += [
        url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
    ]
