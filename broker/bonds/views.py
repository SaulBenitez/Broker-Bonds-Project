from django.db.models import query
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

from bonds.models import Bond
from bonds.serializers import BondSerializer


class BondSellList(generics.ListAPIView):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer

    def get(self, request):
        
        try:
            user = request.user
            data = request.data
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
       

class BondCreateSellOrder(generics.CreateAPIView):
    '''
    Handle creation of bound sell orders 
    '''
    serializer_class = BondSerializer

    def post(self, request):
        user = request.user
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save(seller=user)
            message = {'massage':'The sell order has been successfully created'}
            return Response(message, status=status.HTTP_201_CREATED)
        
        message = {'massage':'The sell order has been rejected'}
        return Response(message.update(serializer.errors), status=status.HTTP_400_BAD_REQUEST)    
