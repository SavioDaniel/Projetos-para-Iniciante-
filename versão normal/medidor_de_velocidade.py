while True:
    velocidade = float(input('Qual a velocidade do veiculo? '))
    if velocidade < 0:
        print(f'Sua velocidade é {velocidade}, logo não existe velocidade negativa')
        print('Por favor faça novamente!')
        continue
    elif velocidade <= 80:
        print(f'Vôce não recebeu multa pós sua velocidade era de {velocidade}, e esta dentro da velocidade permitida que é de 80km')
        break
    elif 81 <= velocidade <= 90:
        print(f'Você esta acima da velocidade permitida, sua velocidade era de {velocidade}')
        print('Vôce recebera uma multa leve')
        break
    elif 91 <= velocidade <= 100:
        print(f'Você esta acima da velocidade permitida, sua velocidade era de {velocidade}')
        print('Vôce recebera uma multa grave')
        break
    elif 101 <= velocidade:
        print(f'Você esta acima da velocidade permitida, sua velocidade era de {velocidade}')
        print('Vôce recebera uma multa gravíssima')
        break