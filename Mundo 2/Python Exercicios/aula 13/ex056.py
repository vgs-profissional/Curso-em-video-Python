mulher = 0
media = 0
conta = 0
for x in range(1, 5):
    print('--- {}ª Pessoa ---'.format(x))
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    conta += idade

    if sexo in 'Mm' and x == 1:
        maiorIdade = idade
        maisVelhoNome = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        maisVelhoNome = nome
    if sexo in 'Ff' and idade <= 20:
        mulher += 1
media = conta / 4
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdade, maisVelhoNome.capitalize()))
print('Ao todo são {} mulheres com idade abaixo de 20 anos'.format(mulher))