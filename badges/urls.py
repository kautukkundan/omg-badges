from django.urls import path

from badges.views import GetOrCreateBadge, GetPublicProfile

urlpatterns = [
    path('', GetOrCreateBadge.as_view()),
    path('/collection/<str:uid>/', GetPublicProfile.as_view()),
]