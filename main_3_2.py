from Exercicios_py.recursiva import recursiva

entrada = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, entrada.split()))
resultado = recursiva(lista_numeros)
print(f"Soma da lista: {resultado}")