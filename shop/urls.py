
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('product/details/', views.product_details, name='product_details'),
    path('product/list/', views.product_list, name='product_list'),
    path('products-of-category/<int:category_id>/', views.index, name='product_of_category'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
