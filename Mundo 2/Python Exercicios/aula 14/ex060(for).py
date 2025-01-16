num = int(input('Diga um número para ver seu fatorial '))
n = num
fatorial = 1
print('{}! -> '.format(num), end='')
for n in range(n, 0, -1):
    print(n, end=' ')
    print('x ' if n > 1 else '= ', end='')
    fatorial *= n
print(fatorial)
