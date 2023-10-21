OPERACOES = ['+', '-', '*', '/']

def validaNumero(num):
    if not num.isdigit():
        print('Você não digitou um numero valido!')
        num = validaNumero(input('Digite um numero novamente: '))

    return int(num)

def validaOperacao(operacao):

    if not OPERACOES.__contains__(operacao):
        print('Você não digitou uma operacao valida!')
        operacao = validaOperacao(input('Digite novamente: '))

    return operacao
    

while True:
    print('Bem vindo a sua calculadora de numeros inteiros!!')
    primeiro_numero = validaNumero(input('Digite o primeiro numero: '))
    segundo_numero = validaNumero(input('Digite o segundo numero: '))
    operacao = validaOperacao(input('Digite a operacao: [+, -, *, /] '))
    resultado = None

    if operacao == OPERACOES[0]:
        resultado = primeiro_numero + segundo_numero
    elif operacao == OPERACOES[1]:
        resultado = primeiro_numero - segundo_numero
    elif operacao == OPERACOES[3]:
        resultado = primeiro_numero * segundo_numero
    else:
        resultado = primeiro_numero / segundo_numero
    
    print(f'O resultado da {primeiro_numero}{operacao}{segundo_numero} é: {resultado}')

    sair = input('Deseja sair? [s] sim ').lower().startswith('s')
    if sair:
        break





