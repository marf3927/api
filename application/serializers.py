from rest_framework import serializers
from .models import Application, User
from user.serializers import UserSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    is_picked = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = ['id', 'user', 'size', 'personal_info_agreed', 'text_agreed', 'is_picked']

