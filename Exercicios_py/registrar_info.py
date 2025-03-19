def registrar_informacoes(*args, **kwargs):
    print("Escreva numeros")
    for arg in args:
        print(arg)
    
    print("Informe sua nome, idade e seu pais")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

registrar_informacoes(2, 4, 6, nome="Carlos", idade=20, pais= "Brasil")