nome = input('Digite o seu nome: ')

while nome.isdigit(): 
    print('Você digitou um numero!!')
    nome = input('Digite o seu nome: ')

contador = 0

while contador < len(nome):
    eh_espaco_branco = not nome[contador].isspace()
    if eh_espaco_branco:
        print(f'*{nome[contador].upper()}*')
    contador+=1
