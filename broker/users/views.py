from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.serializers import UserSerializer, UserTokenObtainPairSerializer
from users import serializers
from users import models


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

class UserLoginApiView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """  
        Handle creating and updating profiles 
    """
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    # For permison access
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserRegisterAPIView(APIView):
    """  
        Handle creating profiles 
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    """ 
    Handle reading, updating, and deleting users
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)