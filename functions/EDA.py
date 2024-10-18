def get_frequency(dfr, elem, control=None):
    '''
    Recibe un DataFrame, el nombre de la columna sobre la cual sacar la frecuencia y el nombre de una columna de control para usar de referencia si se hizo un explode para tratar con elementos repetidos o no.
    Retorna un DataFrame con los elementos únicos, la cantidad de veces que aparece y el porcentaje de estos respecto al total de valores en el DataFrame.
    '''
    # si existe una columna de control se aislan las columnas y se eliminan los duplicados
    if control is not None:
        df = dfr[[control, elem]].drop_duplicates()
    else:
        # si no existe una columna de control, se aisla la columna necesaria
        df = dfr[[elem]]

    # se calcula la frecuencia
    freq = df[elem].value_counts().reset_index()
    freq.columns = [elem, 'frequency']

    # se calcula el porcentaje
    freq['percentage'] = round((freq['frequency'] / freq['frequency'].sum()) * 100, 2)

    return freq