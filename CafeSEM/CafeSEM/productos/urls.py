from django.urls import path

from productos import views

urlpatterns=[
    path('',views.index,name='index'),
    path('productos', views.listadoProductos, name='listadoProductos'),
    path('menu', views.menu, name='menu')
]