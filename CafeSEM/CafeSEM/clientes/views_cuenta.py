import re

from django.shortcuts import render, redirect
from clientes.models import Usario


def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None


def iniciar_sesion(request):
    return render(request, "clientes/cuenta/iniciar_sesion.html")


def verificar_contrasenia(request):
    email = request.POST['email']
    contrasenia = request.POST['contrasenia']

    usario_model = Usario()
    cursor = usario_model.get_usario(email)

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

    response = render(request, "clientes/cuenta/verificar_contrasenia.html", contexto)
    if cursor and 'error' not in contexto:
        response.set_cookie(key='email', value=email)

    return response