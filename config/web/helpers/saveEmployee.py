from web.models import Empleados


def saveEmployee(request, formEmployee, data):

    if request.method == 'POST':

        dataForm = formEmployee(request.POST)
        print(dataForm)
        if dataForm.is_valid():
            dataEmploye = dataForm.cleaned_data
            print(dataEmploye)
            newEmploye = Empleados(
                nombre=dataEmploye['nombre'],
                apellido=dataEmploye['apellido'],
                foto=dataEmploye['foto'],
                salario=dataEmploye['salario'],
                contacto=dataEmploye['contacto'],
                cargo=dataEmploye['cargo']
            )

            try:
                newEmploye.save()
                data['flag'] = True
            except Exception as error:
                print('error', error)
                data['flag'] = True
