from rest_framework import serializers
from .models import User, UserManager



class RegisterSerializer(serializers.ModelSerializer):
       class Meta:
        model = User
        fields = ['username', 'email', 'password']
 
        def validate(self, attrs):
            return attrs
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
        def Admin_create(self,validate_data):
            return User.objects.create_admin(**validate_data)