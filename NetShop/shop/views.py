from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews
    })

def payment(request, id):
    product = Product.objects.filter(id=id).first()

    return render(request, 'payment.html', {
        'product': product
    })