from rest_framework import routers
from django.urls import path, include
from django.contrib.auth import views as django_auth_views

from . import views

router = routers.SimpleRouter()
router.register(r"", views.CreateUserViewSet, basename="create-user-view")


urlpatterns = [
    path("current/", views.CurrentUserView.as_view()),
    path(r"", include(router.urls)),
]
