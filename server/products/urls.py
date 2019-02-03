from django.urls import path

from .views import catalog, catalogstar, catalogsnowflake

urlpatterns = [
    path('', catalog),
    path('snowflake/', catalogsnowflake),
    path('star/', catalogstar),

]