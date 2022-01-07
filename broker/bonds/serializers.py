from rest_framework import serializers 

from bonds.models import Bond
from users.serializers import UserSerializer


class BondSerializer(serializers.ModelSerializer):

    seller = UserSerializer(many=False, read_only=True)
    buyer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Bond
        # fields = '__all__'
        fields = (
            'id',
            'bond_name',
            'bond_no',
            'bond_price',
            'seller',
            'buyer'
        )
    
    # def create(self, validated_data):



