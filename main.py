#SISTEMA DE PERGUNTAS E RESPOSTAS. GANHADORES DE COPAS DO MUNDO

print('Vamos testar seus conhecimentos de futebol! Vamos ver se você conhece todos os países ganhadores de COPAS DO MUNDO desde 1930')
print('Está pronto? Responda as perguntas abaixo COM A LETRA correspondente ao país vencedor')
print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1930? ',
        'respostas': {'a': 'Uruguai', 'b': 'Brasil', 'c': 'Estados Unidos', 'd': 'Iugoslávia'},
        'resp_certa': 'a'
    },
    'Pergunta 2': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1934? ',
        'respostas': {'a': 'Brasil', 'b': 'Uruguai', 'c': 'Áustria', 'd': 'Itália'},
        'resp_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1938? ',
        'respostas': {'a': 'Uruguai', 'b': 'Alemanha', 'c': 'Itália', 'd': 'Suécia'},
        'resp_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Quem venceu a copa do Mundo de 1950? ',
        'respostas': {'a': 'Brasil', 'b': 'Uruguai', 'c': 'Inglaterra', 'd': 'Holanda'},
        'resp_certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1954? ',
        'respostas': {'a': 'Venezuela', 'b': 'Hungria', 'c': 'Alemanha', 'd': 'Uruguai'},
        'resp_certa': 'c'
    },
    'Pergunta 6': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1958? ',
        'respostas': {'a': 'Brasil', 'b': 'Argentina', 'c': 'Uruguai', 'd': 'Flamengo'},
        'resp_certa': 'a'
    },
    'Pergunta 7': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1962? ',
        'respostas': {'a': 'Argentina', 'b': 'Brasil', 'c': 'Uruguai', 'd': 'Itália'},
        'resp_certa': 'b'
    },
    'Pergunta 8': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1966? ',
        'respostas': {'a': 'Brasil', 'b': 'Inglaterra', 'c': 'França', 'd': 'Holanda'},
        'resp_certa': 'b'
    },
    'Pergunta 9': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1970? ',
        'respostas': {'a': 'Alemanha', 'b': 'Inglaterra', 'c': 'França', 'd': 'Brasil'},
        'resp_certa': 'd'
    },
    'Pergunta 10': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1974? ',
        'respostas': {'a': 'Espanha', 'b': 'Croácia', 'c': 'Alemanha', 'd': 'Holanda'},
        'resp_certa': 'c'
    },
    'Pergunta 11': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1978? ',
        'respostas': {'a': 'Turquia', 'b': 'Argentina', 'c': 'França', 'd': 'Bélgica'},
        'resp_certa': 'b'
    },
    'Pergunta 12': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1982? ',
        'respostas': {'a': 'Brasil', 'b': 'Inglaterra', 'c': 'Itália', 'd': 'Espanha'},
        'resp_certa': 'c'
    },
    'Pergunta 13': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1986? ',
        'respostas': {'a': 'Alemanha', 'b': 'Espanha', 'c': 'Argentina', 'd': 'Holanda'},
        'resp_certa': 'c'
    },
    'Pergunta 14': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1990? ',
        'respostas': {'a': 'Brasil', 'b': 'Inglaterra', 'c': 'França', 'd': 'Alemanha'},
        'resp_certa': 'd'
    },
    'Pergunta 15': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1994? ',
        'respostas': {'a': 'Brasil', 'b': 'México', 'c': 'Suécia', 'd': 'Holanda'},
        'resp_certa': 'a'
    },
    'Pergunta 16': {
        'pergunta': 'Quem venceu a Copa do Mundo de 1998? ',
        'respostas': {'a': 'Brasil', 'b': 'Inglaterra', 'c': 'França', 'd': 'Holanda'},
        'resp_certa': 'c'
    },
    'Pergunta 17': {
        'pergunta': 'Quem venceu a Copa do Mundo de 2002? ',
        'respostas': {'a': 'Uruguai', 'b': 'Argentina', 'c': 'Brasil', 'd': 'Inglaterra'},
        'resp_certa': 'c'
    },
    'Pergunta 20': {
        'pergunta': 'Quem venceu a Copa do Mundo de 2006? ',
        'respostas': {'a': 'Portugal', 'b': 'Alemanha', 'c': 'França', 'd': 'Itália'},
        'resp_certa': 'd'
    },
    'Pergunta 21': {
        'pergunta': 'Quem venceu a Copa do Mundo de 2010? ',
        'respostas': {'a': 'Espanha', 'b': 'Holanda', 'c': 'Alemanha', 'd': 'Uruguai'},
        'resp_certa': 'a'
    },
    'Pergunta 22': {
        'pergunta': 'Quem venceu a Copa do Mundo de 2014? ',
        'respostas': {'a': 'Brasil', 'b': 'Holanda', 'c': 'Argentina', 'd': 'Alemanha'},
        'resp_certa': 'd'
    },
    'Pergunta 23': {
        'pergunta': 'Quem venceu a Copa do Mundo de 2018? ',
        'respostas': {'a': 'Inglaterra', 'b': 'França', 'c': 'Croácia', 'd': 'Argentina'},
        'resp_certa': 'b'
    },

}

respostas_certas = 0 #contador de respostas certas

for k, v in perguntas.items():
    print(f'{k}: {v["pergunta"]}')

    for r, a in v['respostas'].items():
        print(f'{r}: {a}')

    print()
    resposta_usuario = input('Digite a letra do país vencedor: ')

    if resposta_usuario == v['resp_certa']:
        print('Parabéns! Resposta certa.')
        respostas_certas += 1

    else:
        print(f'Resposta errada. A resposta correta seria a letra [{v["resp_certa"]}]')
    print()

qtd_perguntas = len(perguntas)
perc_acerto = round(respostas_certas / qtd_perguntas * 100, 2)


# FEEDBACK

print(f'Até hoje já foram realizadas {qtd_perguntas} Copas do Mundo. Você acertou {respostas_certas} repostas. O que corresponde a um percentual de acerto de {perc_acerto}%.')

if perc_acerto == 100:
    print('Você foi brilhante! Acertou a todas as perguntas. Seu conhecimento sobre Copas do Mundo está no nível MASTER!')
elif 80 <= perc_acerto <= 99:
    print('Parabéns, você tem um conhecimento excelente sobre as Copas do Mundo')
elif 50 <= perc_acerto < 80:
    print('Parabéns, seu conhecimento sobre as Copas do Mundo é muito bom.')
elif perc_acerto == 0:
    print('Você desconhece completamente o assunto "Copas do Mundo"')
else:
    print('Você tem um conhecimento básico sobre o assunto.')
