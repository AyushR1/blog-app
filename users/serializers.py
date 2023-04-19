from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerialiser(serializers.Serializer):
    username = serializers.CharField(max_length = 255, min_length = 3)
    password = serializers.CharField(min_length = 8, write_only = True)

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError({'username': ('Username is already taken')})
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 255, min_length = 3)  
    password = serializers.CharField(min_length = 8, write_only = True)

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': ('Username is not found')})
        return data
    
    def get_jwt_token(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if not user:
            return {'password': ('Invalid credentials')}
        
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
