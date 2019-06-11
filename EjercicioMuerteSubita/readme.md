#### Gabriel Esteban Castillo Ramirez
# Tercer Ejercicio Muerte Subita
##Extraer los valores máximos de cada lista de una lista de listas
Para la determinación de un mayor en cada lista declaramos la siguiente funcion:
```python
def determinarMayor(arreglo):
    if all(x < arreglo[0] for x in arreglo[1:]):
        return arreglo[0]
    return determinarMayor(arreglo[1:])
```
Vemos que al ser una función podemos utilizarla con la finalidad de  recorrer una lista compuesta de listas


tal que, al hacer uso de la función map, podemos resumir ese recorrido en una linea:
```python
list(map(lambda x: determinarMayor(x), listadeListas)))
```
Con map garantizamos que en la lista se recorra cada lista realizando la operación y retornando en cada una el mayor de cada una de ellas.


