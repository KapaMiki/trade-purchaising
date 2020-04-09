from rest_framework.validators import ValidationError, UniqueValidator
from rest_framework import serializers
from .models import User





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
        fields = ('username',
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
    first_name = serializers.CharField(min_length=2)
    last_name = serializers.CharField(min_length=2)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

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