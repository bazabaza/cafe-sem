from django.urls import path

from clientes import views, views_cuenta

urlpatterns=[
    path('cuenta/iniciar_sesion', views_cuenta.iniciar_sesion, name='iniciar-session'),
    path('cuenta/verificar_contrasenia', views_cuenta.verificar_contrasenia, name='verificar-contrasenia'),
    path('cuenta/view', views_cuenta.view_cuenta, name='view-cuenta'),
]
