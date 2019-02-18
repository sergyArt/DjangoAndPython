from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from baketapp.models import Baket
from products.models import Product
# Create your views here.


def baket(request):

    baket_user = Baket.objects.filter(user=request.user)

    user_sum_prod = quantity_product(baket_user)

    content = {'baket_user': baket_user,
               'user_sum_prod': user_sum_prod
               }
    return render(request, 'baketapp/baket.html', content)

def quantity_product(baket_user):
    sum_product = 0
    for i in baket_user:
        sum_product += i.quantity
    return sum_product

def baket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    baket = Baket.objects.filter(user=request.user, product=product).first()

    if not baket:
        baket = Baket(user=request.user, product=product)

    baket.quantity += 1
    baket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def baket_remove(request, pk):

    remove_product = get_object_or_404(Baket, product_id=pk)
    if not remove_product:
        baket_user = Baket.objects.filter(user=request.user)
        content = {'baket_user': baket_user}
        return render(request, 'baketapp/baket.html', content)
    remove_product.delete()
    return HttpResponseRedirect('/baket/')
