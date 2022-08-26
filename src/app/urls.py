from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'', views.EmailLogViewSet, basename='email-log-view')

urlpatterns = router.urls
