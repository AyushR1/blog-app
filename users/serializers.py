from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerialiser(serializers.Serializer):
    username = serializers.CharField(max_length = 255, min_length = 3)
    password = serializers.CharField(min_length = 8, write_only = True)

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError({'username': ('Username is already taken')})
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
