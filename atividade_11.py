import re

def calculo_digitos_finais_cpf(numeros_cpf, qtd_indices): 
    contador = qtd_indices
    soma_total = 0
    index = 0
    while contador > 1:
        soma_total += int(numeros_cpf[index]) * contador
        contador-=1
        index+=1
    
    digito = (soma_total * 10) % 11

    return digito if digito <= 9 else 0

cpf_entrada = input("Digite o seu cpf: ")
cpf_somente_numeros = re.sub(r'[^0-9]', '', cpf_entrada)

primeiro_digito = calculo_digitos_finais_cpf(cpf_somente_numeros,10)
segundo_digito = calculo_digitos_finais_cpf(cpf_somente_numeros,11)

print(f'O primeiro digito: {primeiro_digito}')
print(f'O segundo digito: {segundo_digito}')

