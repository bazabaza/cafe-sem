from django.urls import path

from clientes import views, views_cuenta

urlpatterns=[
    path('cuenta/iniciar_sesion', views_cuenta.iniciar_sesion, name='iniciar-session'),
    path('cuenta/verificar_contrasenia', views_cuenta.verificar_contrasenia, name='verificar-contrasenia'),
    path('cuenta/view', views_cuenta.view_cuenta, name='view-cuenta'),
    path('cuenta/add_direccion_forma', views_cuenta.add_direccion_forma, name='add-direccion-forma'),
    path('cuenta/add_direccion', views_cuenta.add_direccion, name='add-direccion'),
    path('cuenta/logout', views_cuenta.logout, name='logout'),
    path('cuenta/eliminar_direccion', views_cuenta.eliminar_direccion, name='eliminar-direccion'),
    path('registro/formularioResgistro', views_cuenta.formularioRegistro, name='eliminar-direccion'),
]
