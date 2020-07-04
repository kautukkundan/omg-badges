from rest_framework import serializers

from core.models import *

# class PersonSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonSession
#         fields = (
#             'email',
#             'session'
#         )


# class EmailOnlySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonBadge
#         fields = (
#             'email',
#         )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
        )


# class EmailUIDSerializerB(serializers.ModelSerializer):
#     class Meta:
#         model = EmailUID
#         fields = (
#             'email',
#             'id'
#         )