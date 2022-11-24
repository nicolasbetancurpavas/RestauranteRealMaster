def getData(data, dataName, model):
    # consulta a todos los datos
    query = model.objects.all()
    data[dataName] = query
    print(query)
