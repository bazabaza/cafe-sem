from django.shortcuts import render
from productos.models import Producto, Categoria

def index(request):
    return render(request, "home.html")

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
    listadoProductos = p.listadoGestionProductos()
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
    imagen = request.POST['imagen']



    p = Producto()
    p.altaProducto(nombre,precio,stock,imagen,descripcion, categoria)

    listadoProductos = p.listadoProductos()
    c = Categoria()
    listadoCategorias = c.listadoCategorias()
    contexto = {
        'listadoProductos': listadoProductos,
        'listadoCategorias': listadoCategorias
    }

    return render(request, "gestionProductos.html", contexto)

def bajaProducto(request):
    p = Producto()
    id = request.GET["id"]
    p.bajaProducto(id)

    listadoProductos = p.listadoGestionProductos()
    c = Categoria()
    listadoCategorias = c.listadoCategorias()
    contexto = {
        'listadoProductos': listadoProductos,
        'listadoCategorias': listadoCategorias
    }

    return render(request, "gestionProductos.html", contexto)

def modificarProducto(request):
    p = Producto()
    id = request.GET["id"]
    print(id)
    info = p.detalleProducto(id)
    c = Categoria()
    categorias= c.listadoCategorias()

    contexto = {
        'producto': info,
        'listadoCategorias': categorias
    }

    return render(request, "modificarProducto.html", contexto)

def modificarProductoDatos(request):
    idProd = request.POST['id_prod']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    stock = request.POST['stock']
    descripcion = request.POST['descripcion']
    categoria = request.POST['categoria']
    imagen = request.POST['imagen']

    p = Producto()
    p.modificarProducto(nombre, precio, stock, imagen, descripcion, categoria, idProd, )

    listadoProductos = p.listadoGestionProductos()
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
