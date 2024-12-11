from django.shortcuts import render
from carrito.models import Carrito, Pedido
from productos.views import listadoProductos


def index(request):
    return render(request, "carrito.html")

def detalleCarrito(request):
    c = Carrito()
    #id = request.GET["idPedido"]
    id = 1
    info = c.detallePedido(id)
    envio = c.idsEnvio(id)

    contexto = {
        'listadoCompra': info,
        'datosDireccion': envio
    }

    return render(request, "carrito.html", contexto)

def direccionEnvio(request):
    c = Carrito()

    #idCliente = request.GET["idCliente"]
    idPedido = request.GET["idPedido"]
    #dirDefecto = request.GET["dir"]

    direccionActual = c.getDatosDireccionActual(idPedido)

    #todasDirecciones = c.getTodasDirecciones(idCliente)

    contexto = {
        'datosDireccion': direccionActual,
    }

    return render(request, "direccionEnvio.html", contexto)

def pedidosAdmin(request):
    p = Pedido()
    pedidos=p.pedidosAdmin()

    contexto = {
        'listadoPedidos': pedidos
    }
    print(listadoProductos)
    return render(request, "listaPedidosAdmin.html", contexto)