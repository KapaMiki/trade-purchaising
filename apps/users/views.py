from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import (
   ListAPIView,
   RetrieveAPIView,
   DestroyAPIView,
   CreateAPIView,
   RetrieveUpdateAPIView,)
from .serializers import (
    UserCreateSerializer,
    UserProfileSerializer,
    UserUpdateSerializer,)






class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response(status=status.HTTP_201_CREATED, data={
            'data':serializer.validated_data,
            'token':token.key
        })

class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
