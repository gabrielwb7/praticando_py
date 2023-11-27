cpf = input("Digite o seu cpf: ")
cpf_somente_numeros = []

for caractere in cpf: 
    if caractere.isdigit(): 
        cpf_somente_numeros.append(int(caractere))

def calculo_primeiro_digito(numeros): 
    contador = 10
    soma_total = 0
    index = 0
    while contador > 1:
        soma_total += numeros[index] * contador
        contador-=1
        index+=1
    
    primeiro_digito = (soma_total * 10) % 11

    return primeiro_digito if primeiro_digito < 9 else 0

primeiro_digito = calculo_primeiro_digito(cpf_somente_numeros)

print(primeiro_digito)

