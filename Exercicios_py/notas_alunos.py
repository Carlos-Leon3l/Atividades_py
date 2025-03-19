def calcular_soma(notas):
    soma_total = 0
    for nota in notas:  
        soma_total += nota
    return soma_total


def calcular_media(soma, quantidade_alunos):
    return soma / quantidade_alunos