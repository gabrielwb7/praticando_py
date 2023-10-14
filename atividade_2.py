class pessoa: 
    nome = 'Gabriel'
    sobrenome = 'Rocha'
    idade = 27
    ano_nascimento = 1996 
    altura = 1.83

print()
print('Nome', pessoa.nome, sep=': ')
print('Sobrenome', pessoa.sobrenome, sep=': ')
print('Idade', pessoa.idade, sep=': ')
print('Ano de nascimento', pessoa.ano_nascimento, sep=': ')
print('Altura', pessoa.altura, sep=': ')
print('É maior de idade?', pessoa.idade >= 18)