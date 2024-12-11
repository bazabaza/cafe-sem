from django.urls import path

from carrito import views

urlpatterns=[
    #path('',views.index,name='index'),
    path('',views.detalleCarrito, name='detalleCarrito'),
    path('direccionEnvio', views.direccionEnvio, name='direccionEnvio'),
    path('pedidos', views.pedidosAdmin, name='pedidosAdmin'),
    path('cambiarDireccionEnvio', views.cambiarDireccionEnvio, name='cambiarDireccionEnvio'),
    path('terminarPedido', views.terminarPedido, name='terminarPedido'),
    path('addProductoCarrito', views.addProductoCarrito, name='addProductoCarrito')

]