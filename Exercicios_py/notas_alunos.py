notas = [10, 5, 6, 9, 8]
alunos = ['Carlos', "Dimitri", "Elias", "Fabricio", "Ronaldo"]

soma_total  = 0
for nota in notas:
    soma_total += nota


def calculo_media(soma, quantidade_alunos):
    media = soma / quantidade_alunos
    return media    


print(calculo_media(soma_total, len(alunos)))
