from django.shortcuts import render

from .models import Product, Description, Package
# Create your views here.

def catalog(request):
    data = Product.objects.all()
    return render(request,
                  'products/catalog.html',
                  {'object_list': data}
                  )

def product_detail_view(request, idx):

    data = Product.objects.get(pk=idx)
    data_description = Description.objects.get(pk=idx)
    data_package = Package.objects.get(pk=idx)

    return render(
        request,
        'products/prod.html',
        {'object_data': data,
         'object_description': data_description,
         'object_package': data_package
        }
    )


