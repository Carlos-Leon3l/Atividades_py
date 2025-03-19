def contar_palavras(texto):
    texto = texto.lower()
    novo_texto = texto.split()
    dicionario = dict()
    
    for letter in novo_texto: 
        if letter in dicionario:
            dicionario[letter] += 1
            dicionario.update({letter: dicionario[letter] })
        else:
            dicionario.update({letter: 1})

    return dicionario
    
print(contar_palavras("Um novo texto um texto texto novo"))