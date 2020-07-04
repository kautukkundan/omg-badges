from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from django.shortcuts import get_object_or_404
from django.http.response import Http404

from badges.models import PersonBadge
from core.models import Profile

from badges.serializers import PersonBadgeSerializer, PersonBadgeGrantSerializer
from core.serializers import ProfileSerializer

class GetOrCreateBadge(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def grantBadge(self, badgeId, user):
        """
        Checks if the person already has a particular badge.
        If not, then grants a new Badge

        returns True if new badge is called
        returns False if existing badge is called
        """

        earned = PersonBadge.objects.filter(user=user, badge__in=[badgeId])
        if len(earned)!=0:
            return False

        try:
            obj = get_object_or_404(PersonBadge, user=user)
            obj.badge.add(badgeId)

            serialized = PersonBadgeGrantSerializer(obj)

            serializer = PersonBadgeGrantSerializer(obj, data=serialized.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Http404:
            data = {"user": user.id, "badge": [badgeId]}
            serialized = PersonBadgeGrantSerializer(data=data)

            if serialized.is_valid():
                serialized.save()
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        return True


    def get(self, request, format=None):
        """
        Return UUID and badges array for a user.
        UUID can be used to display public profile.
        """

        user = request.user
        response_obj = {}

        try:
            data = get_object_or_404(PersonBadge, user=user)
            personBadgeSerialized = PersonBadgeSerializer(data)
            response_obj['badges'] = personBadgeSerialized.data['badges'] 
        except Http404:
            response_obj['badges'] = [] 

        profile = Profile.objects.filter(user=user).first()
        profileSerialized = ProfileSerializer(profile)
        
        response_obj['uuid'] = profileSerialized.data['id']

        return Response(response_obj)


    def post(self, request):
        """
        Handles request for creating new standalone badge
        which are not linked to a event session.
        """

        user = request.user 
        newbadge = request.data["badge"]

        badgeEarned = self.grantBadge(newbadge, user)    
        
        response = {'user': user.email, 'success': True, 'badgeEarned': badgeEarned, 'badge': newbadge}
        return Response(response, status=status.HTTP_201_CREATED)


class GetPublicProfile(APIView):
    """
    Retrieve public profile with the UUID sent
    Obscures the email ID to prevent private info leak
    but yet verify if it's the correct person's profile
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, uid, format=None):
        try:
            obj = get_object_or_404(Profile, pk=uid)

            data = get_object_or_404(PersonBadge, user=obj.user)
            serializer = PersonBadgeSerializer(data)

            response_obj = serializer.data
        
            email = obj.user.email
            split = email.split('@')
            joined = split[0][:3]+"*****@" + split[1]
            response_obj['email'] = joined
        
            return Response(response_obj)

        except Http404:
            return Response({'error': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
