from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.authtoken import views

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', views.obtain_auth_token),
    path('api/badges/', include('badges.urls'))
    # path('api/session/', MarkPresenceForSession.as_view()),
    # path('api/email_listxyzabc/', EmailList.as_view()),
    # path('api/email_listuuid/', EmailListUUID.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)