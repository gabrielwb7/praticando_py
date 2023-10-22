palavra_secreta = 'Poder'
letras_acertadas = ''
qtd_tentativa = 0 

while True: 
    letra_digitada = input('Digite uma letra: ')

    if (len(letra_digitada) > 1): 
        print('Digite apenas uma letra! Por favor.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formatada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formatada += letra
        else:
            palavra_formatada += '*'
    
    qtd_tentativa+=1

    if(palavra_secreta == palavra_formatada):
        print(
            f'Você acertou!! ' 
            f' \n A palavra era: {palavra_secreta} ' 
            f' \n Tentativas: {qtd_tentativa}' 
        )
        break
    
    print(palavra_formatada)

