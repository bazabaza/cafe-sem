from django.urls import path

from productos import views

urlpatterns=[
    path('',views.index,name='index'),
    path('productos', views.listadoProductos, name='listadoProductos'),
    path('gestionproductos', views.gestionProductos, name='gestionProductos'),
    path('guardarproductos', views.guardarProducto, name='gestionProductos'),
    path('detalle', views.detalleProducto, name="detalleProducto"),
    path('baja', views.bajaProducto, name="bajaProducto"),
    path('modificarProducto', views.modificarProducto, name="detalleProducto"),
    path('modificarProductoDatos', views.modificarProductoDatos, name="detalleProducto"),
    path('menu', views.menu, name='menu'),
    path('listado', views.listadoRecetas, name='listadoRecetas'),
    path('elaboracion', views.detalleReceta, name='detalleReceta')
]