from .view import image_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', include('user.urls.Me_url')),
    path('applications/', include('application.urls.Application_url')),
    path('cstapplications/', include('custom_application.urls.CstApplication_url')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('media/uploads/items_image/<str:file_name>', image_view),
]
