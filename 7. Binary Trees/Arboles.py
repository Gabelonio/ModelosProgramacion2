class nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor < valor:
        return buscar(arbol.derecha, valor)
    return buscar(arbol.izquierda, valor)


def sumar(arbol):
    if arbol == None:
        return 0
    return sumar(arbol.izquierda)+arbol.valor+sumar(arbol.derecha)

def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izquierda)+[arbol.valor]+a_lista(arbol.derecha)

#Agregar un nodo a un arbol existente
def agregarNodo(arbol,valor):

    if arbol.valor == valor:
        return arbol
    #Si el valor que entra es menor, debe ingresar por izquierda
    if arbol.valor > valor:
        # Si no hay mas donde buscar el valor, se coloca en la posicion
        if(arbol.izquierda == None):
            return nodo(arbol.valor, nodo(valor), arbol.derecha)
        # Se sigue buscando el lugar del valor
        else:
            return nodo(arbol.valor, agregarNodo(arbol.izquierda, valor), arbol.derecha)
    #Si el valor que entra es mayor, debe ingresar por derecha
    if arbol.valor < valor:
        if(arbol.derecha == None):
            return nodo(arbol.valor, arbol.izquierda, nodo(valor))
        else:
            return nodo(arbol.valor, arbol.izquierda, agregarNodo(arbol.derecha, valor))


#Agregar lista de nodos a un arbol existente
def agregarNodos(arbol, listaValores):
    if listaValores == []:
        return arbol
    return agregarNodos(agregarNodo (arbol,listaValores[0]) , listaValores[1:])


#Agrega los nodos en la creación del árbol
def agregarElemento(arbol, valor):
    if arbol == None:
        return nodo(valor)
    return agregarNodo(arbol, valor)


#Pasa los valores a la agregación de nodos
def a_arbol(lista):
    if lista == []:
        return None
    return agregarElemento(a_arbol(lista[:-1]),lista[-1])


def main():
    l = nodo(25, nodo(10, nodo(5), nodo(18)), nodo(40, None, nodo(50)))
    print(buscar(l,10))
    print(sumar(l))
    print(a_lista(l))
    print(a_lista(agregarNodo(l, 7)))
    print(a_lista(agregarNodos(l, [1,2,3,15,20,90,900])))
    print(a_lista(a_arbol([25, 10, 40, 5, 18, 30, 50])))


main()
