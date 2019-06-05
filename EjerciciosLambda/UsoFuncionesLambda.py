from functools import reduce

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)


def main():

    #Map realiza la aplicacion de una funcion a una lista de entradas
    #esta lista de entradas pueden ir en dos e inclusive pueden ir listas de funciones
    funcs = [multiply, add]
    print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [9, 8, 7, 6])))
    print(list(map(lambda x: x(5), funcs)))
    #Filter retorna elementos en donde la funcion retorna una sentencia verdadera
    #para la lista de elementos de entrada
    print(list(filter(lambda x: x % 3 == 0, [3, 6, 9, 12, 11, 13, 14])))
    #Reduce retorna una expresion simplificada en donde los elementos se operan de a pares
    #de manera  secuencial
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

main()
