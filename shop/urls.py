
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('product/details/<int:product_id>', views.product_details, name='product_details'),
    path('product/details/html/', views.product_details_html, name='product_details_html'),
    path('products-of-category/<int:category_id>/', views.product_list, name='product_list'),
    path('product/list/html/', views.product_list_html, name='product_list_html'),
    path('products-of-category/<int:category_id>/', views.index, name='product_of_category'),
    path('product/images/<int:product_id>/', views.product_images, name='product_images'),
    path('e_customers/',views.e_customers_view, name='e_customers'),
    path('customer_add/', views.customers_add, name='customers_add'),
    path('customer_details/<int:customer_id>/', views.customer_details_view, name='customer_details'),
    path('customer_update/<int:customer_id>', views.customer_update, name='customer_update'),
    path('customer_delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
