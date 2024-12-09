from django.shortcuts import render
from clientes.models import Producto

def index(request):
    return render(request, "index.html")

def listadoProductos(request):
    p = Producto()
    listado = p.listadoProductos()

    contexto = {
        'listado': listado
    }

    return render(request, "listadoProductos.html", contexto)
