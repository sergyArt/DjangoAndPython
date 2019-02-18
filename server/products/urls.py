from django.urls import path

from .views import catalog, product_detail_view, product_category_show

#app_name='products'

urlpatterns = [
    path('', catalog),
    path('<int:idx>/', product_detail_view),
    path('categories/<int:idcat>/', product_category_show),
]