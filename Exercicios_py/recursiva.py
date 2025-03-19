

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def recursiva(numeros): 
    if len(numeros) == 1:
        return numeros[0]
    else:
        return numeros[0] + recursiva(numeros[1:])

print(recursiva(numeros))
