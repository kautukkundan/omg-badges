from django.contrib import admin

from core.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields=('archived', 'user',)
    list_display=('id', 'user', 'created_at', 'updated_at',)
