from django.urls import path

from clientes import views

urlpatterns=[
    path('',views.index,name='index'),
    path('productos', views.listadoProductos, name='listadoProductos')
]
