from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {'products': products})
    
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    product_images = ProductImages.objects.filter(product=id)
    return render(request, "products/product_detail.html", {'product': product, 'product_images':product_images})
