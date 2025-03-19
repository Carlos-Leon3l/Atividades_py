def recursiva(numeros): 
    if len(numeros) == 1:
        return numeros[0]
    else:
        return numeros[0] + recursiva(numeros[1:])

