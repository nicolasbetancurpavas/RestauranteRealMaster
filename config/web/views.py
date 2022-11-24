# render Py
from django.shortcuts import render
from web.formularios.formPlates import FormPlates
from web.formularios.formEmployee import FormEmployee

#MODELOS (tablas)
from web.models import Platos
from web.models import Empleados

# Query
from web.helpers.savePlates import savePlates
from web.helpers.saveEmployee import saveEmployee
from web.helpers.getData import getData


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

    savePlates(request, FormPlates, data)
    getData(data, 'platos', Platos)

    return render(request, 'registerPlates.html', data)


def EmployeView(request):
    formulario = FormEmployee()

    data = {
        'formulario': formulario,
        'flag': False,  # bandera
    }

    saveEmployee(request, FormEmployee, data)

    return render(request, 'registerEmploye.html', data)


def MainView(request):
    data = {
        'flag': False,  # bandera
    }
    getData(data, 'platos', Platos)
    return render(request, 'getmain.html', data)


def AdminPlates(request):

    data = {
        'flag': False,  # bandera
    }

    getData(data, 'platos', Platos)

    return render(request, 'crudPlates.html', data)


def AdminEmpleoyee(request):

    data = {
        'flag': False,  # bandera
    }
    getData(data, 'empleados', Empleados)

    return render(request, 'crudEmploye.html', data)
