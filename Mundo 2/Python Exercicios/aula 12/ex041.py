from datetime import date
ano = int(input('Que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano
print('A sua idade é {}'.format(idade))
if idade <= 9:
    print('Você é um nadador da categoria mirim')
elif idade <= 14:
    print('Você é um nadador da categoria infantil')
elif idade <= 19:
    print('Você é um nadador da categoria junior')
elif idade <= 24:
    print('Você é um nadador da categoria sênior')
else:
    print('Você é uma nadador da categoria mestre')