def registrar_informacoes(*args, **kwargs):
    print("Argumentos (args):")
    for arg in args:
        print(arg)
    
    print("Informacoes extras (kwargs):")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

registrar_informacoes(2, 4, 6, nome="Carlos", idade=20, pais="Brasil")
