
from rest_framework import serializers 
from users import models


class UserSerializer(serializers.ModelSerializer):
    """ Serializes a user """

    class Meta:
        model = models.User
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
        user = models.User.objects.create_user(
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
