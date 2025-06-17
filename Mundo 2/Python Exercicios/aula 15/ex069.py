cores = {'verde_neg_sub':'\033[1;4;32m',
         'verde_neg':'\033[1;32m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'verme':'\033[31m',
         'fecha':'\033[m'}
adulto = homens = mulheresMenos20 = 0

while True:
    print('-' * 30)
    print('Cadastre uma pessoa'.title().center(30,' '))
    print('-' * 30)
    idade = int(input('Qual a idade da pessoa? ').strip())
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F] ').strip().upper()[0])
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    if idade >= 18:
        adulto +=1
    if sexo in 'mM':
        homens +=1
    if sexo in 'Ff' and idade < 20:
        mulheresMenos20 += 1
    if continuar in 'nN':
        print('Total de pessoas com mais de 18 anos: {}{}{}.'.format(cores['azul'],adulto, cores['fecha']))
        print('Ao todo houveram {}{}{} homens cadastrados.'.format(cores['verde'],homens,cores['fecha']))
        print('E temos {}{}{} mulheres com menos de 20 anos.'.format(cores['azul'],mulheresMenos20,cores['fecha']))
        break
    
    