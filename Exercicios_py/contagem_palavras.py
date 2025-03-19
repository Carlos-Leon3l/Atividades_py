def contar_palavras(texto):
    texto = texto.lower()
    novo_texto = texto.split()
    dicionario = dict()
    
    for palavra in novo_texto: 
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

    return dicionario
