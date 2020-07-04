from django.contrib import admin

from events.models import *

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields=('sessionId', 'name', 'start', 'end', 'badge', 'archived',)
    list_display=('sessionId', 'name', 'start', 'end', 'badge', 'archived',)

@admin.register(SessionCountSpecial)
class SessionAdmin(admin.ModelAdmin):
    fields=('count', 'badge', 'archived',)
    list_display=('count', 'badge', 'archived',)

@admin.register(PersonSession)
class PersonSessionAdmin(admin.ModelAdmin):
    fields=('archived', 'session', 'user',)
    list_display=('user', 'archived', 'created_at', 'updated_at',)
