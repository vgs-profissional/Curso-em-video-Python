num = int(input('Escolha um número inteiro '))
escolhas = int(input('Escolha a base de conversão \n [1]-binário \n [2]-octal \n [3]-hexadecimal \n'))

print('{} {}'.format(num, escolhas))
if escolhas == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif escolhas == 2:
    print('{} convertido para octadeximal é {}'.format(num, oct(num)[2:]))
elif escolhas == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha invalida')
