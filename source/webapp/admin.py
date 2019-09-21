from django.contrib import admin
from webapp.models import Guestbook

class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'text', 'status', 'created_at']
    list_filter = ['author']
    list_display_links = ['pk', 'text']
    search_fields = ['author', 'text']
    fields = ['author', 'text', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']



admin.site.register(Guestbook, GuestbookAdmin)