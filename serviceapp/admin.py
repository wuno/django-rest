from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_id', 'product_name', 'product_url', 'advertiser', 'designer', 'image_url', 'price', 'commission')

admin.site.register(Product)


