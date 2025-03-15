from django.contrib import admin
from django.contrib.auth.models import Group

from shop.models import Product,Category, Images

admin.site.unregister(Group)






@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'quantity' )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image' )

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'image' )
