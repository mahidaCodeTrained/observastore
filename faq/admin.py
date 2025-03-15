from django.contrib import admin
from .models import Faq


@admin.register(Faq)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)
