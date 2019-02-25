from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from accounts.models import AccountUser
from products.models import Product, Category
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserCreateView, ProductCreateView, CategoryCreateView
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def show_options(request):
    title = 'Админка/выбор опции'

    content = {
        'title': title,
    }

    return render(request, 'adminapp/base.html', content)

class UserCreateView(ListView):
    model = AccountUser
    template_name = 'adminapp/users_test.html'

class UserAddView(CreateView):
    model = AccountUser
    template_name = 'adminapp/users_cr.html'

def user_create(request):
    form = UserCreateView()
    success_url = reverse_lazy('adminapp:user_read')
    if request.method == 'POST':
        form = UserCreateView(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/create_user.html', {'form': form})


def user_read(request):
    title = 'админка/пользователи '

    objects = AccountUser.objects.all()

    content = {
        'title': title,
        'objects': objects
    }

    return render(request, 'adminapp/users.html', content)

def user_update(request, pk):
    obj = get_object_or_404(AccountUser, pk=pk)
    form = UserCreateView(instance=obj)
    success_url = reverse_lazy('adminapp:user_read')

    if request.method == 'POST':
        form = UserCreateView(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/update_user.html', {'form': form})


def user_delete(request, pk):
    obj = get_object_or_404(AccountUser, pk=pk)
    success_url = reverse_lazy('adminapp:user_read')
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/delete_user.html', {'obj': obj})


def category_read(request):
    title = 'админка/категории'

    objects = Category.objects.all()

    content = {
        'title': title,
        'objects': objects
    }

    return render(request, 'adminapp/category.html', content)

def category_create(request):
    form = CategoryCreateView()
    success_url = reverse_lazy('adminapp:category_read')
    if request.method == 'POST':
        form = CategoryCreateView(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/create_category.html', {'form': form})

def category_update(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    form = CategoryCreateView(instance=obj)
    success_url = reverse_lazy('adminapp:category_read')

    if request.method == 'POST':
        form = CategoryCreateView(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/update_category.html', {'form': form})

def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    success_url = reverse_lazy('adminapp:category_read')
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/delete_category.html', {'obj': obj})

def product_read(request):
    title = 'админка/продукты'

    objects = Product.objects.all()

    content = {
        'title': title,
        'objects': objects
    }

    return render(request, 'adminapp/product.html', content)

def product_create(request):
    form = ProductCreateView()
    success_url = reverse_lazy('adminapp:product_read')
    if request.method == 'POST':
        form = ProductCreateView(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/create_product.html', {'form': form})


def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductCreateView(instance=obj)
    success_url = reverse_lazy('adminapp:product_read')

    if request.method == 'POST':
        form = ProductCreateView(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/update_product.html', {'form': form})

def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('adminapp:product_read')
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(success_url)

    return render(request, 'adminapp/delete_product.html', {'obj': obj})