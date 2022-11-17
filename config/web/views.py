# render
from django.shortcuts import render
from web.formularios.formPlates import FormPlates
from web.formularios.formEmploye import FormEmployee

#MODELOS (tablas)
from web.models import Platos
from web.models import Empleados

# consultas
from web.helpers.postPlates import saveData
from web.helpers.getPlates import getPlates


def Home(request):
    return render(request, 'index.html')


def PlatesView(request):
    # instanciamos un objecto de la clase formulario
    formulario = FormPlates()
    # diccionario para enviar al HTML (templates)
    data = {
        'formulario': formulario,
        'flag': False,  # bandera
    }
    saveData(request, FormPlates, data)
    getPlates(data, Platos, 'platos')

    return render(request, 'mainPlates.html', data)


def Employe(request):
    formulario = FormEmployee()

    data = {
        'formulario': formulario,
        'flag': False,  # bandera
    }

    getPlates(data, Empleados, 'empleados')

    # preguntamos si existe alguna peticion tipo POST asociada a la vista
    return render(request, 'mainEmploye.html', data)
