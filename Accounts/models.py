from django.db import models
from django.urls import reverse

# Create your models here.
class UserAccount(models.Model):
    u_name=models.CharField(max_length=250)
    u_password=models.CharField(max_length=12)
    u_repassword=models.CharField(max_length=12)
    u_mail=models.CharField(max_length=30)