def getPlates(data, model, newdata):
    # consulta a todos los datos
    query = model.objects.all()
    data[newdata] = query
    print(query)
