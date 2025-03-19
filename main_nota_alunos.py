from Exercicios_py.notas_alunos import calcular_soma, calcular_media

notas = [10, 5, 6, 9, 8]
alunos = ['Carlos', 'Dimitri', 'Elias', 'Fabricio', 'Ronaldo']

soma_total = calcular_soma(notas)
media = calcular_media(soma_total, len(alunos))
print(f"A média das notas é: {media}")

