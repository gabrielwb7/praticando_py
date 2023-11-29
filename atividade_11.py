cpf = input("Digite o seu cpf: ")
cpf_somente_numeros = []

for caractere in cpf: 
    if caractere.isdigit(): 
        cpf_somente_numeros.append(int(caractere))

def calculo_digitos_finais_cpf(numeros_cpf, qtd_indices): 
    contador = qtd_indices
    soma_total = 0
    index = 0
    while contador > 1:
        soma_total += numeros_cpf[index] * contador
        contador-=1
        index+=1
    
    primeiro_digito = (soma_total * 10) % 11

    return primeiro_digito if primeiro_digito <= 9 else 0

primeiro_digito = calculo_digitos_finais_cpf(cpf_somente_numeros,10)
segundo_digito = calculo_digitos_finais_cpf(cpf_somente_numeros,11)

print(f'O primeiro digito: {primeiro_digito}')
print(f'O segundo digito: {segundo_digito}')

