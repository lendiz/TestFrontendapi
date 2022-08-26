from rest_framework import serializers

from . import models


class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailLog
        fields = ('id', 'sender', 'recipient', 'subject', 'message')
