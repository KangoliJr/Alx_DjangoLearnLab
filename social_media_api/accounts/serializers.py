from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only= True)
    confirm_password = serializers.CharField(write_only= True)
    bio = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'email':{'required':True},
        }
        
    def validate(self, data):
        if data['password'] !=data['confirm_password']:
            raise serializers.ValidationError({"password":"password does not match"})
        return data
    def create(self,validated_data):
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        bio=validated_data.get('bio', '')
        
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password,
            bio=bio
        )
        
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return data
        raise serializers.ValidationError("Invalid Credentials")