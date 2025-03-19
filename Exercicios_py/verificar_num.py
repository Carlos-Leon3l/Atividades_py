def verificar_numero(numero):
    if numero < 2:
        return False
    for num in range(2, int(numero ** 0.5) + 1):
        if numero % num == 0:
            return False
    return True


print(verificar_numero(8))
