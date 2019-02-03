from django.shortcuts import render
import json
# Create your views here.

def catalog(request):
    return render(request, 'products/catalog.html')

def catalogstar(request):
    content_data = get_data('star')
    return render(
        request,
        'products/catalog/star.html',
        content_data
    )

def catalogsnowflake(request):
    content_data = get_data('snowflake')
    return render(
        request,
        'products/catalog/snowflake.html',
        content_data
    )


def get_data(data_name):
    with open('data.json', 'r') as f:
        line = f.read()

    try:
        data = json.loads(line)
        return data[data_name]
    except Exception as e:
        print('Error is: ', e)
