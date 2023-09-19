from django.db import models
from Home.models import *
from django.urls import reverse
from Home.views import *

# Create your models here.
class CartList(models.Model):
    cart_id = models.CharField(max_length=200,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id    

class Items(models.Model):
    prdt = models.ForeignKey(products,on_delete=models.CASCADE)   
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)  
    qnty = models.IntegerField()
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return str(self.prdt)
    
    def total(self):
        return self.prdt.p_price*self.qnty