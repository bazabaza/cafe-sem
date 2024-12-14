import re

from django.shortcuts import render, redirect
from clientes.models import Usuario, Pedidos


def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None


def iniciar_sesion(request):
    return render(request, "clientes/cuenta/iniciar_sesion.html")


def verificar_contrasenia(request):
    email = request.POST['email']
    contrasenia = request.POST['contrasenia']

    usario_model = Usuario()
    cursor = usario_model.get_usuario(email)

    contexto = dict()
    row = cursor.fetchone()

    if not validar_email(email):
        contexto['error'] = 'Email tiene mal formato'
    elif len(contrasenia) < 6:
        contexto['error'] = 'La contraseña es muy corta'
    elif not row:
        contexto['error'] = 'Email no es encontrado'
    elif contrasenia != row[3]:
        contexto['error'] = 'La contraseña es incorrecta'

    if cursor and 'error' not in contexto:
        contexto['email'] = row[2]
        contexto['tipo_usuario'] = row[4]


    response = render(request, "clientes/cuenta/verificar_contrasenia.html", contexto)
    if cursor and 'error' not in contexto:
        response.set_cookie(key='email', value=email)

    return response

def add_direccion_forma(request):
    return render(request, "clientes/cuenta/add_direccion_forma.html")

def add_direccion(request):
    error = False
    calle = request.POST['calle']
    numero = request.POST['numero']
    ciudad = request.POST['ciudad']
    codigo_postal = request.POST['codigo_postal']
    apodo_direccion = request.POST['ciudad']
    email = request.COOKIES.get('email')

    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\.\'\-]+$", calle):
        error = "Nombre de calle es incorrecto"
    elif not re.match(r"^\d{1,10}$", numero):
        error = "Numero de casa es incorrecto"
    elif not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\.\'\-]+$", ciudad):
        error = "Nombre de ciudad es incorrecto"
    elif not re.match(r"^[A-Za-z0-9\s-]{3,10}$", codigo_postal):
        error = "Codigo postal es incorrecto"
    elif not len(apodo_direccion):
        error = "Apodo de dirección es incorrecto"

    usuario_model = Usuario()

    params = {
        'calle': calle,
        'numero': numero,
        'ciudad': ciudad,
        'codigo_postal': codigo_postal,
        'apodo_direccion': apodo_direccion,
        'id_cliente': usuario_model.get_usuario_id(email)
    }

    res = usuario_model.insertar_direccion(params)
    if not res:
        error = 'Algo mal con base de datos. Perdone.'

    contexto = {
        'error': error
    }

    return render(request, "clientes/cuenta/verificar_direccion.html", contexto)

def view_cuenta(request):
    email = request.COOKIES.get('email')

    usario_model = Usuario()
    cursor_direcciones = usario_model.get_direcciones(email)

    contexto = dict()
    contexto['direcciones'] = cursor_direcciones

    pedidos_model = Pedidos()
    cursor_pedidos = pedidos_model.get_pedidos(email)

    pedidos = []
    for id_pedido, fecha, precio in cursor_pedidos:
        fecha = fecha.strftime("%d/%m/%Y")
        pedido = {
            'id_pedido': id_pedido,
            'fecha': fecha,
            'precio': precio
        }
        print(fecha)
        cursor_productos = pedidos_model.get_productos_de_pedido(id_pedido)
        productos_de_pedido = []
        for producto in cursor_productos:
            productos_de_pedido.append(producto[1])

        pedido['productos'] = ', '.join(productos_de_pedido)

        pedidos.append(pedido)

    contexto['pedidos'] = pedidos

    return render(request, "clientes/cuenta/view_cuenta.html", contexto)

def logout(request):
    response = render(request, "clientes/cuenta/logout.html")
    response.delete_cookie('email')

    return response

def eliminar_direccion(request):
    id_direccion = request.GET['id_direccion']

    usuario_model = Usuario()
    usuario_model.eliminar_direccion(id_direccion)

    return render(request, "clientes/cuenta/eliminar_direccion.html")


def formularioRegistro(request):
    return render(request, "clientes/registro/formularioRegistro.html")

def detallePedido(request):
    id = request.GET["idPedido"]
    p = Pedidos()
    pedidoDatos=p.get_pedido_by_id(id)

    contexto = {
        'listadoPedido': pedidoDatos
    }

    return render(request, "clientes/cuenta/detallePedido.html", contexto)