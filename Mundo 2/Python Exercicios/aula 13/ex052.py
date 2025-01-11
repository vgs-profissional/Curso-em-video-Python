#Jeito que eu fiz:

num = int(input('Diga um número inteiro: '))
cores = {'fecha':'\033[m',
         'verm':'\033[31m',
         'verd':'\033[32m'}
cont = 0
for x in range(1, num + 1):
    print(cores['verm'], end='')
    if num % x == 0:
        print(cores['verd'], end='')
        cont += 1
    print(x, end=' ')
    print(cores['fecha'], end='')
if cont == 2:
    print('\n{} É um número primo'.format(x), end='')
else:
    print('\n{} Nâo é primo pois é divisível por {}{}{} números'.format(x,cores['verd'], cont, cores['fecha']), end='')


#Jeito que o Guanabara fez:

"""num = int(input('Digite um número inteiro: '))
tot = 0
for x in range(1, num + 1):
    if num % x == 0:
        print('\033[34m',end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(x), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(x, tot))
if tot == 2:
    print('primo')
else:
    print('n primo')"""
