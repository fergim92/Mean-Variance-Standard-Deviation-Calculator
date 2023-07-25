import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list_numpy = np.reshape(list, (3,3))

    # Cálculo de la media en cada eje y para la matriz aplanada
    mean_axis_1 = list_numpy.mean(axis=0).tolist()        # Media en el eje 0 (columnas)
    mean_axis_2 = list_numpy.mean(axis=1).tolist()        # Media en el eje 1 (filas)
    mean_axis_flattened = list_numpy.mean().tolist()      # Media en la matriz aplanada

    # Cálculo de la varianza en cada eje y para la matriz aplanada
    variance_axis_1 = list_numpy.var(axis=0).tolist()     # Varianza en el eje 0 (columnas)
    variance_axis_2 = list_numpy.var(axis=1).tolist()     # Varianza en el eje 1 (filas)
    variance_flattened = list_numpy.var().tolist()        # Varianza en la matriz aplanada

    # Cálculo de la desviación estándar en cada eje y para la matriz aplanada
    standard_deviation_axis_1 = list_numpy.std(axis=0).tolist()   # Desviación estándar en el eje 0 (columnas)
    standard_deviation_axis_2 = list_numpy.std(axis=1).tolist()   # Desviación estándar en el eje 1 (filas)
    standard_deviation_flattened = list_numpy.std().tolist()      # Desviación estándar en la matriz aplanada

    # Cálculo del máximo en cada eje y para la matriz aplanada
    max_axis_1 = list_numpy.max(axis=0).tolist()         # Máximo en el eje 0 (columnas)
    max_axis_2 = list_numpy.max(axis=1).tolist()         # Máximo en el eje 1 (filas)
    max_flattened = list_numpy.max().tolist()            # Máximo en la matriz aplanada

    # Cálculo del mínimo en cada eje y para la matriz aplanada
    min_axis_1 = list_numpy.min(axis=0).tolist()         # Mínimo en el eje 0 (columnas)
    min_axis_2 = list_numpy.min(axis=1).tolist()         # Mínimo en el eje 1 (filas)
    min_flattened = list_numpy.min().tolist()            # Mínimo en la matriz aplanada

    # Cálculo de la suma en cada eje y para la matriz aplanada
    sum_axis_1 = list_numpy.sum(axis=0).tolist()         # Suma en el eje 0 (columnas)
    sum_axis_2 = list_numpy.sum(axis=1).tolist()         # Suma en el eje 1 (filas)
    sum_flattened = list_numpy.sum().tolist()            # Suma en la matriz aplanada

    # Definición del diccionario calculations con los resultados
    calculations = {
        "mean": [mean_axis_1, mean_axis_2, mean_axis_flattened],
        "variance": [variance_axis_1, variance_axis_2, variance_flattened],
        "standard deviation": [standard_deviation_axis_1, standard_deviation_axis_2, standard_deviation_flattened],
        "max": [max_axis_1, max_axis_2, max_flattened],
        "min": [min_axis_1, min_axis_2, min_flattened],
        "sum": [sum_axis_1, sum_axis_2, sum_flattened]
    }

    return calculations
