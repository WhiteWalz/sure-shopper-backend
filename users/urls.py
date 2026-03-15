from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
import users.views as uviews

urlpatterns = [
    path('create/', uviews.CreateView.as_view(), name='register'),
]