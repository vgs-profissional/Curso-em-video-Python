num = int(input('Digite um número pra calcular o fatorial '))
n = num
if num != 0:
    print('{}! -> '.format(num), end=' ')
    while n > 0:
        #print('{} x '.format(n), end=' ')
        #print(' = ' if n > 1 else ' = ', end=' ') <--- if e else no print e na mesma linha é possível
        if n > 1:
            num = num * (n - 1)
            print('{}'.format(n),end=' ')
            print('x', end=' ')
        else:
            print('{}'.format(n),end=' ')
            print('= {}'.format(num),end=' ')
        n = n - 1
else:
    print('0! = 1')

"""from math import factorial
pergunta = int(input('Diga um número para ver seu fatorial '))
fatorial = factorial(pergunta)
print('O fatorial de {} é {}.'.format(pergunta, fatorial))"""