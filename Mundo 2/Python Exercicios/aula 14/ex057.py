"""n = 0
while n < 1:
    sexo = str(input('Qual o seu sexo? [m/f] ')).strip().lower()
    if sexo == 'f' or sexo == 'feminino':
        print('Então você é do sexo feminino')
        n += 1
    elif sexo == 'm' or sexo == 'masculino':
        print('Então você é do sexo masculino')
        n += 1
    else:
        print('Resposta invalida tente novamente')"""

sexo = str(input('Qual o seu sexo? [m/f] ')).strip().lower()[0]
while sexo not in 'fm':
    sexo = str(input('Resposta invalida, por favor informe seu sexo [m/f] ')).strip().lower()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

