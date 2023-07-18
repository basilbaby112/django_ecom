from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def store(request):
    product=Product.objects.all()
    context={
        'products':product
    }
    return render(request,'pages/store.html',context)

def cart(request):
    return render(request,'pages/cart.html')

def checkout(request):
    return render(request,'pages/checkout.html')
