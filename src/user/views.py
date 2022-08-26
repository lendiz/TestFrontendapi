from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model

from . import serializers

UserModel = get_user_model()


class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CreateUserSerializer
    permission_classes = [AllowAny]

    http_method_names = ["post"]


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = serializers.RetrieveUserSerializer
    lookup_field = "pk"

    def get_object(self, *args, **kwargs):
        return self.request.user
