This is the boilerplate for the Mean-Variance-Standard Deviation Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator


# Mean-Variance-Standard Deviation Calculator

Este proyecto consiste en crear una función llamada `calculate()` en el archivo `mean_var_std.py` que utilice NumPy para calcular la media, varianza, desviación estándar, máximo, mínimo y suma de las filas, columnas y elementos de una matriz 3x3.

## Instrucciones

1. Comienza importando este proyecto en Replit.
2. Luego, selecciona "Use run command" en la ventana .replit y haz clic en "Done".
3. Se proporcionan algunos recursos de video para aprender sobre Python y Pandas en la descripción del proyecto.

## Función calculate()

La función `calculate()` debe recibir una lista con 9 dígitos como entrada. Luego, convierte esta lista en una matriz NumPy de 3x3 y realiza los cálculos necesarios para obtener la media, varianza, desviación estándar, máximo, mínimo y suma en diferentes ejes y para la matriz aplanada.

El diccionario devuelto por la función debe seguir el siguiente formato:

```python
{
  'mean': [media_eje1, media_eje2, media_aplanada],
  'variance': [varianza_eje1, varianza_eje2, varianza_aplanada],
  'standard deviation': [desviacion_estandar_eje1, desviacion_estandar_eje2, desviacion_estandar_aplanada],
  'max': [maximo_eje1, maximo_eje2, maximo_aplanada],
  'min': [minimo_eje1, minimo_eje2, minimo_aplanada],
  'sum': [suma_eje1, suma_eje2, suma_aplanada]
}
```

## Ejemplo

Si llamamos a `calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])`, debería devolver:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Unit Tests

Se proporciona un archivo `test_module.py` con pruebas unitarias para verificar que la función `calculate()` funcione correctamente.