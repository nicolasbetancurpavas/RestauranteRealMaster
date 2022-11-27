def EditPlates(request, formEdit, data):
    if request.method == 'POST':
        dataForm = formEdit(request.POST)
        if dataForm.is_valid():
            datosEdit = dataForm.cleaned_data
            (datosEdit)
