class pessoa: 
    nome = 'Gabriel'
    peso = 115
    altura = 1.83

imc = pessoa.peso / pessoa.altura ** 2

print(pessoa.nome, 'tem', pessoa.altura, 'de altura,')
print('pesa', pessoa.peso, 'e seu IMC é:', imc)
