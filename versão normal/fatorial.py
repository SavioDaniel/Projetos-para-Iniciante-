
while True:
    print('Digite um número diferente de -10, caso queira continuar.')
    num = int(input('Digite um número: '))

    if num == -10:
        print('Você saiu.')
        break
    elif num < 0:
        print('Número inválido, não é possível calcular o fatorial de números negativos.')
        continue
    elif num == 0:
        print(f'O fatorial de {num} é 1.')
    else:
        fatorial = 1
        for i in range(1, num + 1):
            fatorial *= i
        print(f'O fatorial de {num} é {fatorial}.')
