from django.contrib import admin
from django.utils.html import format_html

from badges.models import *

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    fields=('badgeId', 'name', 'image_tag', 'image', 'archived',)
    list_display=('badgeId', 'name', 'image_tag', 'total_given', 'created_at', 'updated_at', 'archived',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="150px" />'.format(obj.image.url))
        else:
            return 'No Image'

    def total_given(self, obj):
        return obj.person_badge.count()


@admin.register(PersonBadge)
class PersonBadgeAdmin(admin.ModelAdmin):
    fields=('badge', 'user', 'archived',)
    list_display=('user', 'badge_count', 'created_at', 'updated_at', 'archived',)

    def badge_count(self, obj):
        return obj.badge.count()