from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    search_fields = ("name", "email", "phone", "country", "city", "subject", "message",)
    list_display = ("subject", "name", "email", "date_created", "is_read",)
    list_filter = ("country", "city",)
    readonly_fields = (
        "name",
        "email",
        "phone",
        "country",
        "city",
        "subject",
        "message",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Message, MessageAdmin)