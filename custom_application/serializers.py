from rest_framework import serializers
from .models import CstApplication
from user.serializers import UserSerializer


class CstApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    is_picked = serializers.ReadOnlyField()

    class Meta:
        model = CstApplication
        fields = ['image', 'id', 'user', 'size', 'personal_info_agreed', 'text_agreed', 'is_picked']

