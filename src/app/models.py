from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()


class EmailLog(models.Model):
    sender = models.ForeignKey(
        to=user_model,
        on_delete=models.CASCADE,
        related_name="emails",
        verbose_name='Sender'
    )
    recipient = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    message = models.TextField(max_length=5000, verbose_name='Message')

    def __str__(self):
        return f'Message ID {self.pk}'

    class Meta:
        verbose_name = 'Email Log'
        verbose_name_plural = 'Email Logs'
