from django.shortcuts import render
from productos.models import Producto, Categoria

def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def listadoProductos(request):
    p = Producto()
    listado = p.listadoProductos()

    contexto = {
        'listado': listado
    }

    return render(request, "listadoProductos.html", contexto)

def gestionProductos(request):
    p = Producto()
    listadoProductos = p.listadoProductos()
    c = Categoria()
    listadoCategorias=c.listadoCategorias()
    contexto = {
        'listadoProductos': listadoProductos,
        'listadoCategorias': listadoCategorias
    }

    return render(request, "gestionProductos.html", contexto)

def guardarProducto(request):

    nombre=request.POST['nombre']
    precio = request.POST['precio']
    stock = request.POST['stock']
    descripcion = request.POST['descripcion']
    categoria = request.POST['categoria']



    p = Producto()
    p.altaProducto(nombre,precio,stock,'www.ase.es',descripcion, categoria)

    listadoProductos = p.listadoProductos()
    c = Categoria()
    listadoCategorias = c.listadoCategorias()
    contexto = {
        'listadoProductos': listadoProductos,
        'listadoCategorias': listadoCategorias
    }

    return render(request, "gestionProductos.html", contexto)

def detalleProducto(request):
    p = Producto()
    id = request.GET["id"]
    info = p.detalleProducto(id)

    contexto = {
        'producto': info
    }

    return render(request, "detalleProducto.html", contexto)
