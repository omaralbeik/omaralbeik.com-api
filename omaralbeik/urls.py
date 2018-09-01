from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from rest_framework import routers

from blog import views as bv
from projects import views as pv
from about import views as av

app_name = "omaralbeik"

router = routers.SimpleRouter()

router.register(r'blog', bv.PostViewSet)
router.register(r'projects', pv.ProjectViewSet)
router.register(r'about', av.AboutSlideViewSet)

urlpatterns = [
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
]

# Django should not serve media files in production,
# they should be served by server instead

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]