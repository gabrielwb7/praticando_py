def calculo_de_imc(peso, altura):
    return peso / altura ** 2

class pessoa: 
    nome = 'Gabriel'
    peso = 115
    altura = 1.83
    imc = calculo_de_imc(peso, altura)

print(f'{pessoa.nome} tem {pessoa.altura:.2f} de altura,')
print(f'pesa {pessoa.peso} e seu IMC é {pessoa.imc:.2f}')