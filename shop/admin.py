from django.contrib import admin
from django.contrib.auth.models import Group

from shop.models import Product,Category, Images

admin.site.unregister(Group)

admin.site.register(Category)



# class ProductResource(resources.ModelResource):
#     class Meta:
#         model = Product
#
#
# @admin.register(Product)
# class ProductModelAdmin( admin.ModelAdmin):
#     resource_class = ProductResource
#     list_display = ['id','name','price','image','category']
#     search_fields = ['name','description']
#     list_filter = [ 'category']
#

admin.site.register(Product)
admin.site.register(Images)