from django.db.models import query
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from bonds.models import Bond
from bonds.serializers import BondSerializer
from bonds.serializers import BondDollarSerializer
from bonds.serializers import DollarSerializer
from bonds.services import get_dollar_info



class BondUserList(generics.ListAPIView):
    """ 
    Retrieve the bought or not sold bonds of the logged user 
    The bond prices are got in national currency (MXN)
    """
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = request.data
            queryset = self.get_queryset().filter(Q(seller=user) | Q(buyer=user)).order_by('id','buyer')
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondSaleOrderUserList(generics.ListAPIView):
    """ 
    Retrieve the bonds sale orders of the logged user
    The bond prices are got in national currency (MXN)
    """
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = request.data
            queryset = self.get_queryset().exclude(buyer__isnull=False).filter(seller=user)
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondBuyOrderUserList(generics.ListAPIView):
    """ 
    Retrieve the bonds buy orders of the logged user
    The bond prices are got in national currency (MXN)
    """
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            queryset = self.get_queryset().exclude(buyer__isnull=True).filter(buyer=user)
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondForSaleList(generics.ListAPIView):
    """ 
    Retrieve the bonds sale orders of any user
    The bond prices are got in national currency (MXN)
    """
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        try:
            user = request.user
            data = request.data
            queryset = self.get_queryset().exclude(seller=user).filter(buyer__isnull=True)
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondCreateSaleOrder(generics.CreateAPIView):
    """ 
    Create bond sale orders 
    The bond prices are set in national currency (MXN)
    """
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(seller=user)
            message = {'massage':'The sale order has been successfully created'}
            return Response(message, status=status.HTTP_201_CREATED)
        
        # message = {'massage':'The sale order has been rejected'}
        message = serializer.errors
        return Response(message, status=status.HTTP_400_BAD_REQUEST)    


class BondBuyOrder(generics.RetrieveUpdateAPIView):
    """ 
    Execute a buy order from bond for sale
    """
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, pk):
        try:
            user = request.user
            bond = Bond.objects.get(id=pk)
        except:
            message = { 'detail': 'The bond buy order has not been completed' }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        if bond.buyer is not None:
            message = {'detail': 'The bond already has been bought'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        if bond.seller != user:
            bond.buyer = user
            bond.save()
            message = { 'detail': 'The bond has been bought' }
            return Response(message, status=status.HTTP_200_OK)

        message = {'detail': 'The user cannot buy its own bonds'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondForSaleOrderListUSD(generics.ListAPIView):
    """ 
    Retrieve the bonds sale orders of any user 
    The bond prices are got in US dollar currency (USD)
    """
    queryset = Bond.objects.all()
    serializer_class = BondDollarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        try:
            user = request.user
            queryset = self.get_queryset().exclude(seller=user).filter(buyer__isnull=True)
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            message = {'message':'The bonds list cannot be displayed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class BondDollarInfo(APIView):
    """ 
    Get the value of USD currency
    """
    serializer_class = BondDollarSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Bond.objects.all()

    def get(self, request):
        try:
            data = get_dollar_info()
            # dollar = float(data['dato'])
            # print(Bond.objects.all())
            serializer = DollarSerializer({
                'value': data['dato'],
                'date': data['fecha']
            }, many=False)

            return Response(serializer.data)
        except:
            message = { 'detail': 'Money conversion could not be done. Try it later' }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)