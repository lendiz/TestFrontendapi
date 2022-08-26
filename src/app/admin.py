from django.contrib import admin

from . import models


@admin.register(models.EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "recipient", "subject")
    search_fields = ("id", "sender__email", "recipient", "subject", "message")
    ordering = ("-id",)
