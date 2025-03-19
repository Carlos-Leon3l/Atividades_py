from Exercicios_py.cont_palavras_2 import contar_palavras

texto_usuario = input("Digite um texto para contar as palavras: ")
numero_palavras = contar_palavras(texto_usuario)
print(f"O número de palavras no texto é: {numero_palavras}")