from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', include('user.urls.Me_url')),
    path('applications/', include('application.urls.Application_url')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
