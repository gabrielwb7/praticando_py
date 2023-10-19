"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero: ')

if numero.isdecimal():
    if int(numero) % 2 == 0:
        print('par')
    else:
        print('impar') 
else:
    print('Você não digitou um numero!!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_str = input('Digite a hora: ')
texto_saudacao = None

if hora_str.isdecimal():
    hora_int = int(hora_str)
    if (hora_int >= 0 and hora_int <= 11):
        texto_saudacao = 'Bom dia!'
    elif (hora_int <= 17):
        texto_saudacao = 'Boa tarde'
    elif (hora_int <= 23):
        texto_saudacao = 'Boa noite'
    else:
        print('Hora invalida')
else:
    print('Você não digitou um numero!!')

print(texto_saudacao)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é pequeno')
elif (tamanho_nome <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é grande')