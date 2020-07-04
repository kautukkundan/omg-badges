from django.urls import path

from events.views import GetOrMarkSession, GetPublicSessions

urlpatterns = [
    path('', GetOrMarkSession.as_view()),
    path('collection/<str:uid>/', GetPublicSessions.as_view()),
]