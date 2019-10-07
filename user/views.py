from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from application.serializers import ApplicationSerializer
from application.models import Application

# Create your views here.


class MeView(mixins.UpdateModelMixin,
             generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        user.instagramId = request.data['instagramId']
        user.phoneNumber = request.data['phoneNumber']
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class MeApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [permissions.IsAuthenticated]