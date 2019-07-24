from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def Productlist(request):
    mydict={'product':Product.objects.all()}
    return render(request,'shop/product.html',mydict)

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = ceil(n/4)
    params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'shop/index.html',params)

def About(request):
    return render(request,'shop/about.html')

def Contact(request):
    return HttpResponse('Contact inside shop')

def Tracker(request):
    return HttpResponse('Tracker inside shop')

def Search(request):
    return HttpResponse('Search inside shop')

def Productview(request):
    return HttpResponse('Product View inside shop')

def Checkout(request):
    return HttpResponse('Checkout inside shop')