from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status

from core.serializers import *
from core.models import *

class RetrieveBadgesForEmail(APIView):
    def get(self, request, format=None):
        email = request.query_params.get('email')
        data = get_list_or_404(PersonBadge, pk=email)

        serializer = PersonBadgeSerializer(data, many=True)
        return Response(serializer.data[0])

class MarkPresenceForSession(APIView):
    def post(self, request):
        email = request.data["email"]
        session = request.data["session"]
        badgeEarned = False
        sessionExists = False

        try:
            get_object_or_404(Session, pk=session)
        except Http404:
            return Response({'error': 'session does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            obj = get_object_or_404(PersonSession, pk=email)
            sessionExists = True
            obj.session.add(session)
            serialized = PersonSessionSerializer(obj)

            serializer = PersonSessionSerializer(obj, data=serialized.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Http404:
            serializer = PersonSessionSerializer(data={'email': email, 'session': [session]})
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not sessionExists:
            obj = get_object_or_404(PersonSession, pk=email)

        if (session=='D0S0'):
            badgeEarned = grantBadge('newperson', email)
            if badgeEarned: 
                return Response({'success': 'User registered!', 'badgeEarned': True}, status=status.HTTP_201_CREATED)
            return Response({'success': 'User registered!', 'badgeEarned': False}, status=status.HTTP_201_CREATED)

        sessionCount = obj.session.all().count()
        if (sessionCount == 2):
            badgeEarned = grantBadge('session1', email)
        elif (sessionCount == 5):
            badgeEarned = grantBadge('session5', email)
        elif (sessionCount == 10):
            badgeEarned = grantBadge('session10', email)
        elif (sessionCount == 20):
            badgeEarned = grantBadge('session20', email)
        elif (sessionCount == 27):
            badgeEarned = grantBadge('sessionAll', email)

        sessionType = Session.objects.get(pk=session).stack
        if sessionType:
            badgeEarned = grantBadge(sessionType, email)

        response = {'email': email, 'success': True, 'badgeEarned': badgeEarned, 'count': sessionCount, 'sessionType': sessionType}
        return Response(response, status=status.HTTP_201_CREATED)


def grantBadge(badgeId, email):
    earned = PersonBadge.objects.filter(pk=email, badge__in=[badgeId])
    if len(earned)!=0:
        return False

    try:
        obj = get_object_or_404(PersonBadge, pk=email)
        obj.badge.add(badgeId)
        serialized = PersonBadgeGrantSerializer(obj)

        serializer = PersonBadgeGrantSerializer(obj, data=serialized.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Http404:
        serializer = PersonBadgeGrantSerializer(data={'email': email, 'badge': [badgeId]})
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return True
