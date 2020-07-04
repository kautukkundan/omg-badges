from rest_framework import serializers

from badges.models import *

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = (
            'badgeId',
            'name',
            'image',
        )


class PersonBadgeSerializer(serializers.ModelSerializer):
    
    badges = serializers.SerializerMethodField(source='get_badges')

    def get_badges(self, obj):
        return BadgeSerializer(obj.badge.filter(archived=False), many=True, read_only=False).data

    class Meta:
        model = PersonBadge
        fields = (
            'badges',
        )


class PersonBadgeGrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonBadge
        fields = (
            'user',
            'badge'
        )