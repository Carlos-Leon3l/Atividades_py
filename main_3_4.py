from Exercicios_py.registrar_info import registrar_informacoes

args_input = input("Digite os argumentos posicionais separados por espaço: ")
args = []  
for arg in args_input.split(): 
    args.append(int(arg)) 
    
kwargs = {}
while True:
    chave = input("Digite uma chave (ou 's' para terminar): ")
    if chave.lower() == 's':
        break
    valor = input(f"Digite o valor para '{chave}': ")
    kwargs[chave] = valor
    
registrar_informacoes(*args, **kwargs)