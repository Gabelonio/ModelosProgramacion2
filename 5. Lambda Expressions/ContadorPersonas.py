from functools import reduce


class persona:
    def __init__(self, nombre, edad, estado, hijos):
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        self.hijos = hijos


def main():
    personas = [persona("Carlos", 45, "separado", 3),
                persona("Manuel", 67, "viudo", 1),
                persona("Daniela", 50, "casada", 2),
                persona("Angelica", 21, "soltera", 0),
                persona("Monica", 52, "separada", 1),
                persona("Daniel", 58, "casado", 3)]

    print(len(list(filter(lambda x: 40 < x.edad < 60 and x.hijos <= 2,# Filtra edad (40,60) y cantidad de hijos (max 2)
                      personas))))


main()