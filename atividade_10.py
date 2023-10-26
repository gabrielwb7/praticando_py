lista_de_compras = []
OPCOES_VALIDAS = 'I', 'A', 'L'

def valida_opcao(opcao):

    if not OPCOES_VALIDAS.__contains__(opcao):
        print('Você não digitou uma opcao valida!')
        opcao = input('Digite novamente: ').upper()
        valida_opcao(opcao)

    return opcao

def validaNumero(num):
    if not num.isdigit():
        print('Você não digitou um numero valido!')
        num = validaNumero(input('Digite um numero novamente: '))

    return int(num)

while True:
    print('Selecione uma opção abaixo:')

    opcao_selecionada = input('[i]nserir [a]pagar [l]istar -> ').upper()
    opcao_selecionada = valida_opcao(opcao_selecionada)
    
    if opcao_selecionada == OPCOES_VALIDAS[0]:
        item_add = input('Digite o item que deseja adicionar: ')
        lista_de_compras.append(item_add)
    elif opcao_selecionada == OPCOES_VALIDAS[1]:
        indice_item_excluido = validaNumero(input('Digite o indice que se encontra o item que será excluido: '))
        try:
            lista_de_compras.pop(indice_item_excluido)
        except IndexError:
            print('Nao foi possivel deletar esse item')
    else:
        for indice, item in enumerate(lista_de_compras):
            print(f'{indice} -> {item}')
