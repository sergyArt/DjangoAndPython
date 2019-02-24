from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Description, Package, Category
from django.views.generic import ListView
from baketapp.models import Baket
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
# Create your views here.

class RestProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 2
    login_url = reverse_lazy('accounts:login')

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                    'image': itm.image.url if itm.image else None
                }, queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestProductListView, self).get_context_data(**kwargs)

        data = {}

        page = context.get('page_obj')
        route_url = reverse('rest_products:list')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number()}'


        return data


    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 2
    login_url = reverse_lazy('accounts:login')


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

