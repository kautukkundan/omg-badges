from django.contrib import admin

from events.models import *

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields=('sessionId', 'name', 'track', 'start', 'end', 'badge', 'archived',)
    list_display=('sessionId', 'name', 'track', 'start', 'end', 'badge', 'total_attendees', 'archived',)

    def total_attendees(self, obj):
        return obj.person_session.count()

@admin.register(SessionCountSpecial)
class SessionAdmin(admin.ModelAdmin):
    fields=('count', 'badge', 'archived',)
    list_display=('count', 'badge', 'archived',)

@admin.register(PersonSession)
class PersonSessionAdmin(admin.ModelAdmin):
    fields=('archived', 'session', 'user',)
    list_display=('user', 'archived', 'session_count', 'created_at', 'updated_at',)

    def session_count(self, obj):
        return obj.session.count()
