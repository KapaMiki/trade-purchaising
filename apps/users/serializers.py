from rest_framework.validators import ValidationError, UniqueValidator
from rest_framework import serializers
from .models import User
from django.shortcuts import get_object_or_404





class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label='Email',
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(label='Password', min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'middle_name',
                  'email',
                  'phone',
                  'birthday',
                  'country',
                  'city',
                  'gender',
                  'avatar',
                  'IIN',
                  'is_businessman')


class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, allow_null=True)
    last_name = serializers.CharField(min_length=2, allow_null=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(allow_null=True)
    avatar = serializers.ImageField()

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'middle_name',
                  'phone',
                  'email',
                  'birthday',
                  'city',
                  'is_businessman',
                  'avatar',)


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        user = get_object_or_404(User, username=username)
        return username