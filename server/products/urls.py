from django.urls import path

from .views import catalog, product_detail_view

urlpatterns = [
    path('', catalog),
    path('<int:idx>/', product_detail_view),
]