from django.urls import path

import baketapp.views as baketapp

app_name = 'baketapp'

urlpatterns = [
    path('', baketapp.baket, name='view'),
    path('add/<int:pk>/', baketapp.baket_add, name='add'),
    path('remove/<int:pk>/', baketapp.baket_remove, name='remove'),
]
