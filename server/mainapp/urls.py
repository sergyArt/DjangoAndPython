from django.urls import path

from .views import index, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', index),
    path('contacts/', contacts),

]