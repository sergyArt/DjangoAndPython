from django.contrib import admin

from .models import Product, Description, Package, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Description)
admin.site.register(Category)

