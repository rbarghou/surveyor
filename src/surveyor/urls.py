"""surveyor URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view


admin.autodiscover()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("survey.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token),
    path(
        "openapi/",
        get_schema_view(title="Surveyor", description="Surveyor Docs", version="0.1.0"),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
