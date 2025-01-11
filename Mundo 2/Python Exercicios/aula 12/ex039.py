from datetime import date
ano = int(input('Que ano você nasceu? '))
idade = date.today().year - ano
atual = date.today().year
print('Com {} anos'.format(idade))
if idade >= 16:
    if idade < 18:
        print('Já pode se alistar ou pode esperar {} anos'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano + 18))
    elif idade == 18:
        print('Você já está na idade de se alistar')
    elif idade > 18:
        print('Se você ainda já não fez, deveria ter se alistado {} anos atrás'.format(idade - 18))
        print('Você fez seu alistamento em {}'.format(atual  - (idade - 18)))
else:
    print('Você não tem a idade para o alistamento, espere até pelo menos os 16 anos ')