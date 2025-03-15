from django.shortcuts import render
from shop.models import Category, Product
# Create your views here.

def index(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    context = {
        'categories': categories,
    }
    return render(request, 'shop/index.html', context)





def product_details(request):
    return  render(request, 'shop/product-details.html')

def product_list(request):
    return render(request, 'shop/product-list.html')



