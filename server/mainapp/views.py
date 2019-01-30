from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')

def catalogsnowflake(request):
    return render(request, 'catalog/snowflake.html')

def catalogstar(request):
    return render(request, 'catalog/star.html')