from rest_framework import serializers
from .models import User

<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class AdminUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        user.is_staff = True  
        user.save()
        if password:
            user.set_password(password)
            user.save()
        return user
=======

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
>>>>>>> d4b30990d1f4c30bb086f2dc6b0cd641d04a4b40
