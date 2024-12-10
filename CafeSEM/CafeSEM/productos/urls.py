from django.urls import path

from productos import views

urlpatterns=[
    path('',views.index,name='index'),
    path('productos', views.listadoProductos, name='listadoProductos'),
    path('gestionproductos', views.gestionProductos, name='gestionProductos'),
    path('guardarproductos', views.guardarProducto, name='gestionProductos'),
    path('detalle', views.detalleProducto, name="detalleProducto"),
    path('menu', views.menu, name='menu')
]