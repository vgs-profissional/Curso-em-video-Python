nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))

media = (nota1 + nota2) / 2
print('Sua média foi {}'.format(media))
cores = {'verm': '\033[31m', 'verd':'\033[32m','azul':'\033[34m', 'fecha':'\033[m'}

if media < 5:
    print('Você foi {}reprovado{} este ano'.format(cores['verm'], cores['fecha']))
elif media >= 5 and media <= 6.9:
    print('Você não foi tão mal, pode fazer {}recuperação{}'.format(cores['azul'], cores['fecha']))
else:
    print('Com média boa, você foi {}aprovado{} para o próximo ano!'.format(cores['verd'], cores['fecha']))