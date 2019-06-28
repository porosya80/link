from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .routers import router

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("bot/", include("bot.urls")),
    path("", include("links.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
