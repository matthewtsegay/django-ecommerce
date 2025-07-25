from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Item


def product(request):
    datas = Item.object.all()
    return render(request ,'shop/product.html',{'datas':datas})

def checkout(request):
    return render(request ,'shop/checkout.html')


def home(request):
    datas = Item.objects.all()
    return render(request,'shop/home.html',{'datas':datas})