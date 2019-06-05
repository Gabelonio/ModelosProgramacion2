from functools import reduce


class carta:
    def __init__(self, valor, pinta, color):
        self.valor = valor
        self.pinta = pinta
        self.color = color


def main():

    cartas = [carta("3", "picas", "rojo"),
              carta("A", "trebol", "negro"),
              carta("10", "diamante", "rojo"),
              carta("Q", "corazon", "rojo"),
              carta("7", "trebol", "negro"),
              carta("8", "corazon", "rojo")]

    print(reduce(lambda x, y: x + y,                                                    #Realiza la suma de los numeros
            list(map(lambda x: (int)(x.valor),                                          #Selecciona los num. de las cartas
                     list(filter(lambda x: x.color == "rojo" and not x.valor.isalpha(), #Filtra rojos sin letra
                                 cartas))))))


main()