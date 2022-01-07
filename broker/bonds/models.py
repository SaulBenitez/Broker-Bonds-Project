from django.db import models
from django.core.validators import DecimalValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

from users.models import User

class Bond(models.Model):

    id = models.AutoField(primary_key=True)
    bond_name = models.CharField(unique=True, validators=[MinLengthValidator(3)], max_length=40)
    bond_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], default=1)
    bond_price = models.DecimalField(max_digits=13, decimal_places=4, validators=[MaxValueValidator(100000000), MinValueValidator(1)], default=0.0000)
    seller = models.ForeignKey(User, on_delete=CASCADE, related_name='seller')
    buyer = models.ForeignKey(User, on_delete=CASCADE, related_name='buyer', blank=True, null=True)

    def __str__(self):
        return f'{self.bond_name}, {self.seller}'