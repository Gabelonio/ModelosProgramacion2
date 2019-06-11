
def determinarMayor(arreglo):
    if all(x < arreglo[0] for x in arreglo[1:]):
        return arreglo[0]
    return determinarMayor(arreglo[1:])


def main():

    print(list(map(lambda x: determinarMayor(x), [[1, 2, 3, 4],
                                                  [1, 3, 5, 7],
                                                  [8, 9, 12, 7],
                                                  [7, 20, 2, 9]])))
    

main()