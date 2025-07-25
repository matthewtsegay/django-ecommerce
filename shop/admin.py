from django.contrib import admin
from .models import Order,OrderItem,Item

# Register your models here.

admin.site.register(Order)
   
    
     
admin.site.register(OrderItem)
    
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id","title","price")
    
admin.site.register(Item,ItemAdmin)
