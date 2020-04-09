from django.urls import path
from .views import (
    UserCreateAPIView,
    UserProfileAPIView,
    UserUpdateAPIView)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create_url'),
    path('token/', obtain_auth_token, name='user_token_url'),
    path('profile/', UserProfileAPIView.as_view(), name='user_profile_url'),
    path('update/', UserUpdateAPIView.as_view(), name='user_update_url')
]
