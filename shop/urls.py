from django.urls import path
from .views import home,product,checkout


app_name = 'shop'

urlpatterns = [
    path('', home ,name='home'),
    path('product/',product,name='product'),
    path('checkout/',checkout,name='checkout')
    
]