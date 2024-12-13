from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser (**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"
