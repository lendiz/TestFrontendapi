from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from . import serializers
from . import models


class EmailLogViewSet(ModelViewSet):
    queryset = models.EmailLog.objects.all()
    serializer_class = serializers.EmailLogSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("recipient", "subject", "message")
    ordering_fields = ("id",)

    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return super().get_queryset().filter(sender=self.request.user)
