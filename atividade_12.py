def multiplicacao(multiplicador):
    def multiplica(num):
        return num * multiplicador
    return multiplica

dobro = multiplicacao(2)
triplo = multiplicacao(3)
quadruplo = multiplicacao(4)

for num in [2, 3, 4]:
    print(f'\n\tO dobro do {num} é {dobro(num)}')
    print(f'\tO triplo do {num} é {triplo(num)}')
    print(f'\tO quadruplo do {num} é {quadruplo(num)}\n')
    print('-' * 40)