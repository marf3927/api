from rest_framework.routers import DefaultRouter

from custom_application import views

router = DefaultRouter()
router.register('', views.CstApplicationsViewSet)

urlpatterns = router.urls