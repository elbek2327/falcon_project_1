from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product, Images, Customers
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from shop.forms import CustomersModelForm



# Create your views here.
def index(request):
    categories = Category.objects.all()
    # Fetch all categories from the database
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(request, 'shop/index.html', context)


def product_details_html(request):
    return render(request, 'shop/product-details.html')


def product_details(request, product_id: int | None = None):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'shop/product-details.html', context)


def product_list_html(request):
    return render(request, 'shop/product-list.html')


def product_list(request, category_id: int | None = None):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category_id=category_id)
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'shop/product-list.html', context)


def product_images(request, product_id: int | None = None, category_id: int | None = None):
    product = get_object_or_404(Product, id=product_id)
    images = Images.objects.filter(product=product)

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'product': product,
        'images': images,
        'products': products,
    }
    return render(request, 'shop/product-list.html', context)


def e_customers_view(request):
    customers = Customers.objects.all()

    context = {
        'customers': customers,
    }
    return render(request, 'shop/customers.html', context)


def customer_details_view(request, customer_id: int | None = None):
    customer = Customers.objects.get(id=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'shop/customer_details.html', context)


def customers_add(request):
    form = CustomersModelForm()
    if request.method == 'POST':
        try:
            form = CustomersModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=True)
                return redirect('e_customers')
        except Exception as e:
            print(f"Error while adding user {e}")
    context = {
        'form': form,
    }
    return render(request, 'shop/customer_create.html', context)


# customer update view
def customer_update(request, customer_id: int | None = None):
    customer = Customers.objects.get(id=customer_id)
    form = CustomersModelForm(request.POST or None, instance=customer)
    if request.method == 'POST':
        try:
            form = CustomersModelForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('e_customers')

        except ObjectDoesNotExist:
            print("Object DoesNotExist")
    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'shop/customer_update.html', context)


# customer delete view
def customer_delete(request, customer_id):
    if request.method == 'POST':
        try:
            customer = Customers.objects.get(id=customer_id)
            customer.delete()
            return redirect(
                reverse('e_customers'))  # yangicha "shop/customers.html" ni orniga url nami bilan direct qiladi
        except ObjectDoesNotExist:
            return render(request, 'shop/customers.html', {'error': 'Customer not found'})
        except Exception as e:
            print(f"Error deleting customer: {e}")
            return render(request, 'shop/customers.html', {'error': 'Error deleting customer'})
    return redirect(reverse('e_customers'))
