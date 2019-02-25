import adminapp.views as adminapp
from django.urls import path
from adminapp.views import UserCreateView, UserAddView
app_name = 'admin_app'


urlpatterns = [
    path('', adminapp.show_options, name='show_options'),

    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/read/', adminapp.user_read, name='user_read'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('user/show/', UserAddView.as_view(), name='show'),


    path('category/read/', adminapp.category_read, name='category_read'),
    path('category/create/', adminapp.category_create, name='category_create'),
    path('category/update/<int:pk>', adminapp.category_update, name='category_update'),
    path('category/delete/<int:pk>', adminapp.category_delete, name='category_delete'),

    path('product/read/', adminapp.product_read, name='product_read'),
    path('product/create/', adminapp.product_create, name='product_create'),
    path('product/update/<int:pk>', adminapp.product_update, name='product_update'),
    path('product/delete/<int:pk>', adminapp.product_delete, name='product_delete'),
]

