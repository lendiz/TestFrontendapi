from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.permissions import IsAuthenticated

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Testing Emails API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[IsAuthenticated],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/users/", include("user.urls")),
    path("api/emails/", include("app.urls")),
]
