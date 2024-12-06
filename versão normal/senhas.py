import random
import string

def gerador_de_senha(tamanho_padrão=8):
    gerador1 = string.ascii_letters 
    gerador2 = string.digits
    gerador3 = string.punctuation
    opcao = gerador1 + gerador2 + gerador3

    senha_usada = ""
    for i in range(tamanho_padrão):
        digito = random.choice(opcao)
        senha_usada += digito
    
    return senha_usada

while True:
    tamanho_senha = input("Quantos dígitos terá a senha: ")

    if tamanho_senha.isdigit():
        tamanho_senha = int(tamanho_senha)
        senha = gerador_de_senha(tamanho_padrão=tamanho_senha)
        print(f"A senha gerada é: {senha}")
    else:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    continuar = input("Deseja gerar outra senha? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break

