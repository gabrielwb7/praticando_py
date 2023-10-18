nome = input('Digite o seu nome: ')
idade = input('Digite o sua idade: ')

if nome == '' or idade == '':
    print('Desculpe, não foi inserido nenhum valor')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrario é {nome[::-1]}')
    print(f'Seu nome contem espaços? {" " in nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome: {nome[0]}')
    print(f'A última letra do seu nome: {nome[len(nome) - 1]}')