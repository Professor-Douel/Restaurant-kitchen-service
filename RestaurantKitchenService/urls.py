from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from service.views import RegisterView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    path(
        "",
        include(
            "service.urls",
            namespace="service"
        )
    ),
    path(
        "accounts/",
        include(
            "django.contrib.auth.urls"
        )
    ),
    path(
        "accounts/register/",
        RegisterView.as_view(),
        name='register'
    ),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
