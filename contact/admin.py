from django.contrib import admin
from .models import ContactRequest, Newsletter


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "store_good", "created_at", "responded")
    list_filter = ("responded", "created_at")
    search_fields = ("name", "email", "store_good__name", "message")
    ordering = ("-created_at",)


admin.site.register(Newsletter)
