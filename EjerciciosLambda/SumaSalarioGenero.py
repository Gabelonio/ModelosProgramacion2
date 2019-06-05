from functools import reduce


class persona:
    def __init__(self, nombre, genero, cargo, salario):
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.salario = salario


def main():
    personas = [persona("Carlos", "masculino", "jefe", 3000000),
                persona("Manuel", "masculino", "ingeniero", 1800000),
                persona("Daniela", "femenino", "empleado", 800000),
                persona("Angelica", "femenino", "diseñador", 1300000),
                persona("Monica", "femenino", "director ejecutivo", 2300000),
                persona("Daniel", "masculino", "empleado", 800000)]

    print("Salario hombres")
    print(reduce(lambda x, y: x + y,  # Realiza la suma de los numeros
                 list(map(lambda x: x.salario,  # Selecciona los salarios de los empleados
                          list(filter(lambda x: x.genero == "masculino",  # Filtra el genero "hombres"
                                      personas))))))
    print("Salario mujeres")
    print(reduce(lambda x, y: x + y,  # Realiza la suma de los numeros
                 list(map(lambda x: x.salario,  # Selecciona los salarios de los empleados
                          list(filter(lambda x: x.genero == "femenino",  # Filtra el genero "mujeres"
                                      personas))))))


main()