perguntas = [
    {
        'enunciado': 'Quanto é 3 x 3?',
        'alternativas': [12, 9, 10, 3],
        'resposta': 9
    },
    {
        'enunciado': 'Qual é o numero primo?',
        'alternativas': [12, 9, 7, 4],
        'resposta': 7
    },
    {
        'enunciado': 'Qual é a soma 3 + 3?',
        'alternativas': [12, 6, 7, 4],
        'resposta': 6
    },
]

def valida_resposta(resposta_usuario, resposta_correta):
    if resposta_correta == resposta_usuario:
        print('Acertou!\n')
        return True
    else: 
        print(f'Errou! Resposta correta: {resposta_correta}\n')
        return False


def montar_questionario():
    acertos = 0 
    lista_de_alternativas = ['a', 'b', 'c' ,'d']
    
    for indice_pergunta, pergunta in enumerate(perguntas):
        
        indice_pergunta+=1
        
        print(f'{indice_pergunta}.{pergunta['enunciado']}')
        print('Alternativas:\n')
        
        for indice, alternativa in enumerate(lista_de_alternativas):
            print(f'{alternativa} - {pergunta['alternativas'][indice]}')
        resposta = input('\nEscolha a alternativa correta: ')
        
        try:
            indice_da_resposta = lista_de_alternativas.index(resposta)
            resultado = valida_resposta(pergunta['alternativas'][indice_da_resposta], pergunta['resposta'])
            
            if resultado:
                acertos += 1
            
        except ValueError:
            print('Alternativa invalida! Questão não contabilizada')
            
    print(f'Acertos: {acertos}')
    
montar_questionario()
        

