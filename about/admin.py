from django.contrib import admin
from.models import AboutPage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ('title', 'mission', 'history')
    list_filter = ('updated_on',)
    # These will be the fields in the form that is created with summernote.
    fields = ('title', 'mission', 'history', 'why_shop_here')
    readonly_fields = ('updated_on',)
    # Using Summernote for the entry.
    summernote_fields = ('mission', 'history', 'why_shop_here')