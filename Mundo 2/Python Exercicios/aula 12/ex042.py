a = float(input('Qual o tamanho do lado do triângulo? '))
b = float(input('Qual o tamanho do segundo lado? '))
c = float(input('Qual o tamanho do terceiro lado? '))

cor = {'b': '\033[34m',
       'g': '\033[32m',
       'r': '\033[31m',
       'f': '\033[m'}

if a + b > c and a + c > b and b + c > a:
    print('Este triângulo pode {}existir{}, seria um triângulo '.format(cor['g'], cor['f']), end='')
    if a == c == b:
        print('{}Equilátero{}'.format(cor['b'], cor['f']))
    elif a != b != c != a:
        print('{}Escaleno{}'.format(cor['b'], cor['f']))
    else:
        print('{}Isósceles{}'.format(cor['b'], cor['f']))
else:
    print('Este triângulo não pode existir')

