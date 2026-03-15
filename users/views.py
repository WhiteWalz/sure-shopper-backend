from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import CreationSerializer

# Create your views here.
class CreateView(generics.CreateAPIView):
    # Logic for user creation
    queryset = get_user_model().objects.all()
    serializer_class = CreationSerializer
    permission_classes = [permissions.AllowAny]