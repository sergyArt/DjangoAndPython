from django.shortcuts import render, get_object_or_404
from .models import Product, Description, Package, Category
from baketapp.models import Baket
# Create your views here.

def catalog(request):
    baket = []
    if request.user.is_authenticated:
        baket = Baket.objects.filter(user=request.user)
        

    data = Product.objects.all()

    return render(request,
                    'products/catalog.html',
                     {'object_list': data,
                      'baket': baket
                      }
                  )

def product_detail_view(request, idx):


    category_name = Category.objects.get(product=idx)

    data = Product.objects.get(pk=idx)
    data_description = Description.objects.get(pk=idx)
    data_package = Package.objects.get(pk=idx)

    return render(
        request,
        'products/prod.html',
        {'object_data': data,
         'object_description': data_description,
         'object_package': data_package,
         'object_category': category_name


        }
    )
#'object_category': category_name

def product_category_show(request, idcat):

    data = Product.objects.filter(category_id=idcat)
    data_category_name = get_object_or_404(Category, pk=idcat)

    print(data)
    print(data_category_name)

    return render(
        request,
        'products/category_list.html',
        {'object_data': data,
         'object_category': data_category_name
         }
    )

