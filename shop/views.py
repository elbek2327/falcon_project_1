from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, Images
# Create your views here.

def index(request):
    categories = Category.objects.all()
    # Fetch all categories from the database
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/index.html', context)




def product_details_html(request):
    return render(request, 'shop/product-details.html')




def product_details(request, product_id:int | None = None):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return  render(request, 'shop/product-details.html', context)


def product_list_html(request):
    return render(request, 'shop/product-list.html')
def product_list(request, category_id :int | None = None):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category_id=category_id)

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'shop/product-list.html', context)


def product_images(request, product_id:int | None = None, category_id :int | None = None):
    product = get_object_or_404(Product, id=product_id)
    images = Images.objects.filter(product=product)

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else :
        products = Product.objects.all()

    context = {
        'product': product,
        'images': images,
        'products': products,
    }
    return render(request, 'shop/product-list.html', context)
