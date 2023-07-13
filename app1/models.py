from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from app2.models import *
from django.urls import reverse

class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='pro')
    profile_pic=models.ImageField(upload_to='user',blank=True)
    description=models.CharField(max_length=200,blank=True)
    Address=models.TextField(max_length=200,blank=True,default='null')
    pincode=models.IntegerField(blank=True,default=1)
    


class Orderes(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ordercus')
    customer=models.CharField(max_length=100,default='no')
    product_id=models.ForeignKey(Upload_product,on_delete=models.CASCADE)
    how_many=models.IntegerField()
    total=models.IntegerField()
    dateandtime=models.DateTimeField(auto_now=True)
    product_request=models.BooleanField(default=True)
    product_accepted=models.BooleanField(default=False)
    riched=models.BooleanField(default=False)
    taken=models.BooleanField(default=False)
    cancel=models.BooleanField(default=False)



    def get_absolute_url(self):

        return reverse('order',kwargs={'pk':self.pk})


    '''def __str__(self):
        return str(self.product_id)'''

    
    
