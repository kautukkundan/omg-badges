from rest_framework import serializers

from core.models import *

class PersonSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonSession
        fields = (
            'email',
            'session'
        )


class EmailOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonBadge
        fields = (
            'email',
        )

class PersonBadgeGrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonBadge
        fields = (
            'email',
            'badge'
        )


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
            'email',
            'badges',
        )


class EmailUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUID
        fields = (
            'email',
        )


class EmailUIDSerializerB(serializers.ModelSerializer):
    class Meta:
        model = EmailUID
        fields = (
            'email',
            'id'
        )