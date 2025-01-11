print('-=-'*15)
print('Analisador de triângulos')
print('-=-'*15)
lado_a = float(input('Qual o tamanho do primeiro lado do triângulo? '))
lado_b = float(input('Do segundo? '))
lado_c = float(input('Do terceiro? '))

cores = {'verde':'\033[1;4;32m',
         'vermelho':'\033[1;4;31m'}

if lado_a + lado_c > lado_b and lado_c + lado_b > lado_a and lado_a + lado_b > lado_c:
    print('{}Este triângulo é capaz de existir'.format(cores['verde']))
else:
    print('{}Este triângulo não é capaz de existir'.format(cores['vermelho']))