"""
Views for the user API
"""
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from user.api.serializers import UserSerializer
from core.models import StudentRecord

from rest_framework import  permissions, viewsets, generics, permissions


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user. """
        return self.request.user