while True:
    try:

        idade = int(input('Idade: '))
        sexo = input('Sexo [M/F]: ').upper()
        peso = float(input('Peso (kg): '))
        altura = float(input('Altura (m): '))

   
        if idade < 0:
            print("Idade inválida. Por favor, insira novamente.")
            continue
        if peso <= 0:
            print("Peso inválido. Por favor, insira novamente.")
            continue
        if altura <= 0:
            print("Altura inválida. Por favor, insira novamente.")
            continue
        if sexo not in ['M', 'F']:
            print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
            continue

     
        imc = peso / (altura ** 2)


        faixa_etaria = "criança" if idade <= 18 else "adulto"
        print(f"Você é um(a) {faixa_etaria} com {idade} anos.")

        
        if sexo == 'M':
            print(f"Seu sexo é Masculino e seu IMC é {imc:.2f}")
            if idade <= 18:
                print("""Tabela de comparação para crianças do sexo masculino:
                Abaixo de 16,5: Abaixo do peso
                16,5 - 22,9: Peso normal
                23 - 26,9: Sobrepeso
                27 ou mais: Obesidade""")
            else:
                print("""Tabela de comparação para adultos do sexo masculino:
                Abaixo de 18,5: Abaixo do peso
                18,5 - 24,9: Peso normal
                25 - 29,9: Sobrepeso
                30 ou mais: Obesidade""")
        elif sexo == 'F':
            print(f"Seu sexo é Feminino e seu IMC é {imc:.2f}")
            if idade <= 18:
                print("""Tabela de comparação para crianças do sexo feminino:
                Abaixo de 15,5: Abaixo do peso
                15,5 - 21,9: Peso normal
                22 - 25,9: Sobrepeso
                26 ou mais: Obesidade""")
            else:
                print("""Tabela de comparação para adultos do sexo feminino:
                Abaixo de 17,5: Abaixo do peso
                17,5 - 23,9: Peso normal
                24 - 28,9: Sobrepeso
                29 ou mais: Obesidade""")
        break  
    except ValueError:
        print("Entrada inválida! Certifique-se de inserir números válidos para idade, peso e altura.")
