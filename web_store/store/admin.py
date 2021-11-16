from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'name', 'slug', 'image', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'slug')
    list_display_links = ('id', 'model')
    search_fields = ('brand', 'model')
    prepopulated_fields = {'slug': ('brand', 'model')}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class ProductToPhoneAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'phone_id')
    list_display_links = ('product_id',)


class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'weight')
    list_display_links = ('id',)
    search_fields = ('weight',)


class PropertyToProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'property_id')
    list_display_links = ('product_id',)


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'quantity')
    list_display_links = ('id',)
    search_fields = ('product_id',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id')
    list_display_links = ('id',)


class ProductToCartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'product_id')
    list_display_links = ('cart_id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(ProductToPhone, ProductToPhoneAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(PropertyToProduct, PropertyToProductAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ProductToCart, ProductToCartAdmin)
