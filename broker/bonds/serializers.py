from decimal import Decimal

from rest_framework import serializers 

from bonds.models import Bond
from bonds.services import get_dollar_value
from users.serializers import UserSerializer


class BondSerializer(serializers.ModelSerializer):
    """ Serializes a bond in national currency (MXN)  """
    seller = UserSerializer(many=False, read_only=True)
    buyer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Bond
        fields = '__all__'

    def to_representation(self, instance):
        data = super(BondSerializer, self).to_representation(instance=instance)
        tmp_price = "${:,.4f} MXN".format(Decimal(data['bond_price']))
        data['bond_price'] = tmp_price
        return data


class BondDollarSerializer(serializers.ModelSerializer):
    """ Serializes a bond in US currency (USD)  """
    seller = UserSerializer(many=False, read_only=True)
    buyer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Bond
        fields = '__all__'

    def to_representation(self, instance):
        data=super(BondDollarSerializer, self).to_representation(instance)
        dollar = get_dollar_value()
        price = "${:,.4f} USD".format(Decimal(data['bond_price'])/Decimal(dollar))
        data['bond_price'] = price 
        return data

    
class DollarSerializer(serializers.Serializer):
    """ Serializes dollar information from Banxico """
    date = serializers.CharField(max_length=64)
    value = serializers.DecimalField(max_digits=6, decimal_places=4)



