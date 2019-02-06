from django.contrib import admin

from .models import Product, Description, Package

# Register your models here.

admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Description)

