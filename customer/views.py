from django.shortcuts import render
from .models import Product, Transaction

#my views are  home page, view product, buy product, receipt page
# Create your views here.
def homepage(request):
    allProducts = Product.objects.all()
    context = {}
    context("allProducts") = allProducts
    return render(request, "home.html", context)

def viewProduct(request, product_id):
    Selected_product = Product.objects.get(id=product_id)
    context ={}
    context("product") = Selected_product
    return render(request, "buy.html", context)

def BuyProduct(request, product_id):
    Selected_product = Product.objects.get(id=product_id)
    context ={}
    context("product") = Selected_product
    return render(request, "buy.html", context)

def SearchProduct(request):
    if request.method == "POST":
        pass

def ReceiptProduct(request, product_id):
    Selected_product = Product.objects.get(id=product_id)
    context ={}
    context("product") = Selected_product
    return render(request, "buy.html", context)


