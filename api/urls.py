from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', include('user.urls.Me_url')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
