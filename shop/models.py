from django.db import models
from django.conf import settings
# Create your models here.

#CATAGORY_CHOICES = (
#   ('s','Shirt'),
#    ('sw','Sport wear'),
#    ('ow','OutWear')
#)
#LABEL_CHOICES = (
#    ('P','primary'),
#    ('S','secondary'),
#    ('D','danger')
#)
class Item(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    #catagory = models.CharField(choices= CATAGORY_CHOICES ,max_length=2 )
    #label = models.CharField(choices = LABEL_CHOICES,max_length=1)
    
    def __str__(self):
        return self.title
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
     
     
    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_data = models.DateTimeField(auto_now_add=True)
    ordered_data = models.DateTimeField()
    ordered = models.BooleanField(default = False)
    
    def __str__(self):
        return self.user.username
