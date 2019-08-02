from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from rest_framework.routers import SimpleRouter

from blog import views as blogViews
from projects import views as projectsViews
from snippets import views as snippetsViews
from contents import views as contentsViews
from contact import views as contactViews

from omaralbeik import server_variables as sv

admin.sites.AdminSite.site_header = sv.ADMIN_HEADER
admin.sites.AdminSite.site_title = sv.ADMIN_TITLE
admin.sites.AdminSite.index_title = sv.ADMIN_PAGE_TITLE
admin.sites.AdminSite.site_url = sv.CLIENT_PROD_URL

app_name = "omaralbeik"


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r"blog", blogViews.PostViewSet)
router.register(r"projects", projectsViews.ProjectViewSet)
router.register(r"technologies", projectsViews.TechnologyViewSet)
router.register(r"snippets", snippetsViews.SnippetViewSet)
router.register(r"languages", snippetsViews.ProgrammingLanguageViewSet)
router.register(r"contents", contentsViews.ContentViewSet)
router.register(r"contact", contactViews.MessageViewSet)

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
