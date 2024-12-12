from django.shortcuts import render
from carrito.models import Carrito, Pedido
from productos.views import listadoProductos
from clientes.models import Usuario
from productos.models import Producto


def index(request):
    return render(request, "carrito.html")

def getIdUsuario(request):
    email = request.COOKIES.get('email')
    u = Usuario()
    result = u.get_usuario(email)
    usuario = result.fetchone()
    return usuario[0]

def getIdPedido(id):
    c = Carrito()
    pedidos = c.getIdPedido(id)
    pedido = pedidos.fetchone()

    if pedido is None:

        return 0

    else:

        return pedido[0]

def detalleCarrito(request):
    idUsuario = getIdUsuario(request)
    idPedido = getIdPedido(idUsuario)

    print('vamos al detalle del carrito')
    #El cliente tiene pedido pendiente
    if idPedido > 0:
        # si: mostramos los datos del carrito
        ca = Carrito()
        info = ca.detallePedido(idPedido)
        envio = ca.idsEnvio(idPedido)

        print('Tenemos datos del carrito')

        contexto = {
            'listadoCompra': info,
            'datosDireccion': envio
        }

    else:
        print('no tenemos pedidos')
        # no: creamos un pedido
        u = Usuario()
        print('UsuarioId: ' + str(idUsuario))
        direcciones=u.get_direcciones_by_id(idUsuario)

        direccionEnvio=direcciones.fetchone()
        #cogemos una direccion por defecto
        if direccionEnvio is None:
            #redirigir a crear direccion CAMBIAR
            return render(request, "carrito.html")
        else:
            print('Entramos en el else')

            p = Pedido()
            p.altaPedido(idUsuario,direccionEnvio[0])

        ca = Carrito()
        info = ca.detallePedido(idPedido)
        envio = ca.idsEnvio(idPedido)

        print('Tenemos datos del carrito')

        contexto = {
            'listadoCompra': info,
            'datosDireccion': envio
        }

    return render(request, "carrito.html", contexto)

def detalleCarrito_ANT(request):
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

    idCliente = request.GET["idCliente"]
    idPedido = request.GET["idPedido"]
    dirDefecto = request.GET["dir"]

    direccionActual = c.getDatosDireccionActual(idPedido)
    todasDirecciones = c.getDirecciones(idCliente)

    contexto = {
        'datosDireccion': direccionActual,
        'todasDirecciones': todasDirecciones,
        'idCliente': idCliente,
        'idPedido': idPedido,
        'dirDefecto': dirDefecto
    }

    return render(request, "direccionEnvio.html", contexto)

def cambiarDireccionEnvio(request):
    c = Carrito()

    idCliente = request.POST["txtIdCliente"]
    idPedido = request.POST["txtIdPedido"]
    dirDefecto = request.POST["cmbDirecciones"]

    print("ID_Cliente: ", idCliente)
    print("IdPedido:" + idPedido)
    print("dirDefecto:" + dirDefecto)

    #Cambiamos la direccion
    nuevosDatos = (int(dirDefecto), int(idPedido))
    result = c.cambiarDireccion(nuevosDatos)

    ca = Carrito()

    direccionActual = ca.getDatosDireccionActual(idPedido)
    todasDirecciones = ca.getDirecciones(idCliente)

    contexto = {
        'datosDireccion': direccionActual,
        'todasDirecciones': todasDirecciones,
        'idCliente': idCliente,
        'idPedido': idPedido,
        'dirDefecto': dirDefecto,
        'resultado': result
    }

    return render(request, "direccionEnvio.html", contexto)

def terminarPedido(request):
    idPedido = request.POST["txtIdPedido"]

    c = Carrito()
    pedido = (int(idPedido),)
    result = c.terminarPedido(pedido)

    return render(request, "home.html")

def pedidosAdmin(request):
    p = Pedido()
    pedidos=p.pedidosAdmin()

    contexto = {
        'listadoPedidos': pedidos
    }
    print(listadoProductos)
    return render(request, "listaPedidosAdmin.html", contexto)

def addProductoCarrito(request):
    idUsuario = getIdUsuario(request)
    idPedido = getIdPedido(idUsuario)

    if idPedido == 0:
        #creamos el pedido
        pass
    else:
        #añadimos el producto
        idProducto = request.GET['idProd']
        cantidad = 1
        total = request.GET['precio']

        #comprobar stock
        #añadir producto
        #restar stock

        c = Carrito()
        datos = (idPedido, idProducto, cantidad, total)
        print (datos)
        result = c.addProducto(datos)

        print(result)

        p = Producto()
        listado = p.listadoProductos()

        contexto={
            'mensaje': result,
            'listado': listado
        }

        return render(request, "listadoProductos.html", contexto)


