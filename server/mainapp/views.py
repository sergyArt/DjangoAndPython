from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'mainapp/index.html',
        {
            'page_describe':'Магазин новогодних украшений "CrismasDecoration"',
            'tagline':'Игрушка каждому!'
        }
    )


def contacts(request):
    return render(request, 'mainapp/contacts.html')
