
from rest_framework import serializers 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Serializes a user """

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fullname',
            'username',
            'password'            
        )
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        """ Create and return a new user """
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            fullname = validated_data['fullname'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """ Handle updating user account """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'fullname',
            'username',
            'token'
        ]
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data