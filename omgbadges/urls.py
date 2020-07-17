from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
import rest_framework_social_oauth2.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework_social_oauth2.urls')),
    path('api/badges', include('badges.urls')),
    path('api/sessions', include('events.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
