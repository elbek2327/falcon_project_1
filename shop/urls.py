
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



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
