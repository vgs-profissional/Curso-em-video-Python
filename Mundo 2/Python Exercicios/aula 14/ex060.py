num = int(input('Digite um número pra calcular o fatorial '))
n = num
print('{}! -> '.format(num), end=' ')
while n > 0:
    if n > 1:
        num = num * (n - 1)
        print('{}'.format(n),end=' ')
        print('x', end=' ')
    else:
        print('{}'.format(n),end=' ')
        print('= {}'.format(num),end=' ')
    n = n - 1

