from django.contrib import admin

from core.models import *

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    fields=('badgeId', 'archived',)
    list_display=('badgeId', 'archived', 'created_at', 'updated_at',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields=('sessionId', 'archived',)
    list_display=('sessionId', 'archived', 'created_at', 'updated_at',)

@admin.register(PersonBadge)
class PersonBadgeAdmin(admin.ModelAdmin):
    fields=('archived', 'badge', 'email',)
    list_display=('email', 'archived', 'created_at', 'updated_at',)

@admin.register(PersonSession)
class PersonSessionAdmin(admin.ModelAdmin):
    fields=('archived', 'session', 'email',)
    list_display=('email', 'archived', 'created_at', 'updated_at',)