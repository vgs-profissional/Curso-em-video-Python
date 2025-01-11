num1 = float(input('Diga um número '))
num2 = float(input('Diga o segundo número '))

cores = {'azul':'\033[0;34m', 'verde':'\033[0;32m'}

if num1 > num2:
    print('O primeiro número é {}maior{} que o segundo'.format(cores['verde'], '\033[m'))
elif num1 == num2:
    print('Os dois números são {}iguais'.format(cores['azul']))
else:
    print('O segundo é {}maior{} que o primeiro'.format(cores['verde'],'\033[m'))
