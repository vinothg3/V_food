from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User

    
class Upload_product(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product')
    product_id=models.AutoField( primary_key=True)
    product_type=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_descrition=models.CharField(max_length=200)
    product_image=models.ImageField(upload_to='upload_product')

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return str(self.product_id)
   

class customorder(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    ordercustomer=models.CharField(max_length=100,default='None')
    product_id=models.ForeignKey(Upload_product,on_delete=models.CASCADE)
    how_many=models.IntegerField()
    total=models.IntegerField()
    dateandtime=models.DateTimeField(auto_now_add=True)
    prime_pk=models.IntegerField(default=0)
    orderconform=models.BooleanField(default=False)
    

    

    def __str__(self):

        return str(self.product_id)