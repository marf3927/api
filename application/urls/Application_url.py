from rest_framework.routers import DefaultRouter

from application import views

router = DefaultRouter()
router.register('', views.ApplicationsViewSet)

urlpatterns = router.urls