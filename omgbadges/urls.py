from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/badges/', RetrieveBadgesForEmail.as_view()),
    path('api/collection/<str:uid>/', RetrieveBadgesForPublic.as_view()),
    path('api/session/', MarkPresenceForSession.as_view()),
    path('api/email_listxyzabc/', EmailList.as_view()),
    path('api/email_listuuid/', EmailListUUID.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)