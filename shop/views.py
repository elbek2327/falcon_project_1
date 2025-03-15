from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, Images
# Create your views here.

def index(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    context = {
        'categories': categories,
    }
    return render(request, 'shop/index.html', context)





def product_details(request, product_id:int | None = None):
    product = Product.objects.get(id=product_id)

    context = {
        'product': product,
    }

    return  render(request, 'shop/product-details.html', context)

def product_list(request, category_id :int | None = None):
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'shop/product-list.html', context={'products': products, 'categories': categories})

def product_images(request, product_id:int | None = None):
    product = get_object_or_404(Product, id=product_id)
    images = Images.objects.filter(product=product)

    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'shop/product-list.html', context)
