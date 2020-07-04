from rest_framework import serializers

from events.models import *

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = (
            'sessionId',
            'name',
            'start',
            'end'
        )


class PersonSessionSerializer(serializers.ModelSerializer):
    
    sessions = serializers.SerializerMethodField(source='get_sessions')

    def get_sessions(self, obj):
        return SessionSerializer(obj.session.filter(archived=False), many=True, read_only=False).data

    class Meta:
        model = PersonSession
        fields = (
            'sessions',
        )


class PersonSessionAttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonSession
        fields = (
            'user',
            'session'
        )