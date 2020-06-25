from django.contrib import admin
from django.utils.html import format_html

from core.models import *

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    fields=('badgeId', 'name', 'image_tag', 'archived', 'image',)
    list_display=('badgeId', 'name', 'image_tag', 'archived', 'created_at', 'updated_at',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="150px" />'.format(obj.image.url))
        else:
            return 'No Image'

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields=('sessionId', 'name', 'stack', 'archived',)
    list_display=('sessionId', 'name', 'stack', 'archived', 'created_at', 'updated_at',)

@admin.register(PersonBadge)
class PersonBadgeAdmin(admin.ModelAdmin):
    fields=('archived', 'badge', 'email',)
    list_display=('email', 'archived', 'created_at', 'updated_at',)

@admin.register(PersonSession)
class PersonSessionAdmin(admin.ModelAdmin):
    fields=('archived', 'session', 'email',)
    list_display=('email', 'archived', 'created_at', 'updated_at',)
