from django.urls import path

from .views import catalog, product_detail_view, product_category_show, ProductListView

#app_name='products'



urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:idx>/', product_detail_view),
    path('categories/<int:idcat>/', product_category_show),
]