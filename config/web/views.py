# render Py
from django.shortcuts import render
from django.shortcuts import redirect


# forms
from web.formularios.formPlates import FormPlates
from web.formularios.formEmployee import FormEmployee
from web.formularios.formEditPlates import FormEdit

# MODELOS (tablas)
from web.models import Platos
from web.models import Empleados

# Query
from web.helpers.savePlates import savePlates
from web.helpers.saveEmployee import saveEmployee
from web.helpers.getData import getData


def Home(request):
    return render(request, 'index.html')


def PlatesRegister(request):
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


def EmployeRegister(request):
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

    formulario = FormEdit()

    data = {
        'formulario': formulario,
        'flag': False,  # bandera
    }

    getData(data, 'platos', Platos)

    return render(request, 'crudPlates.html', data)


def EditPlates(request, id):

    if request.method == 'POST':
        dataForm = FormEdit(request.POST)
        if dataForm.is_valid():
            dataEdit = dataForm.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(
                    nombre=dataEdit['name'],
                    descripcion=dataEdit['description'],
                    precio=dataEdit['price'])
            except Exception as error:
                print(error)

    return redirect('admin-plates')


def AdminEmpleoyee(request):

    data = {
        'flag': False,  # bandera
    }
    getData(data, 'empleados', Empleados)

    return render(request, 'crudEmploye.html', data)
