from web.models import Platos


def savePlates(request, FormPlates, data):

    if request.method == 'POST':
        # capturamos datos del formulario
        dataForm = FormPlates(request.POST)
        # validamos
        if dataForm.is_valid():
            dataPlates = dataForm.cleaned_data

            # envio la info de los inputs al modelo
            newPlates = Platos(
                nombre=dataPlates['name'],
                descripcion=dataPlates['description'],
                foto=dataPlates['image'],
                precio=dataPlates['price'],
                tipo=dataPlates['type'],
            )

            # save data platenew post bd
            try:
                newPlates.save()
                print('exito guardando los datos')
                data['flag'] = True
            except Exception as error:
                data['flag'] = False
                print('error', error)
