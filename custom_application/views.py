from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CstApplicationSerializer
from .models import CstApplication


class PostOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in 'POST'


class CstApplicationsViewSet(viewsets.ModelViewSet):

    serializer_class = CstApplicationSerializer
    queryset = CstApplication.objects.all()
    permission_classes = [IsAdminUser | PostOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True)
    def applying(self, request, *args, **kwargs):
        application = self.get_object()
        if application.personal_info_agreed or application.text_agreed:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(status=status.HTTP_400_BAD_REQUEST)

