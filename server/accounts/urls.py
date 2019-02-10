from django.urls import path

import accounts.views as accounts

app_name = 'accounts'

urlpatterns = [
    path('login/', accounts.login, name='login'),
    path('logout/', accounts.logout, name='logout'),
]