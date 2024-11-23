from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Invoice(models.Model):
        username=models.CharField(max_length=20,null=True,blank=True) 
        email=models.EmailField(null=True,blank=True) 
        invoice_date=models.DateField(null=True,blank=True) 
        invoice_number=models.IntegerField(max_length=10,null=True,blank=True) 
        state=models.CharField(max_length=10,null=True,blank=True) 
        user=models.ForeignKey(User,related_name="create_invoice",on_delete=models.DO_NOTHING)

        def __str__(self):
                return self.email