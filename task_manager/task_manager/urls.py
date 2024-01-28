from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
from .settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", views.home, name="home"),
        path("task/", include("task.urls")),
    ]
    + static(MEDIA_URL, document_root=MEDIA_ROOT)
    + static(STATIC_URL, document_root=STATIC_ROOT)
)

admin.site.site_header = "Task Manager Admin"
admin.site.site_title = "Task Manager Admin"
