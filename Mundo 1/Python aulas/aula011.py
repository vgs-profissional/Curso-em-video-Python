#print('\033[3;;40mOlá mundo!\033[m')

#a = 4
#b = 3
#print('Os valores são \033[4;32m{}\033[m e \033[4;31m{}\033[m'.format(a,b))

###nome = 'vinicius'
#dicionario:
#cores = {'limpa': '\033[m',
#         'amarelo_sub':'\033[4;33m',
#         'azul_neg':'\033[1;34m'}
#
#print('Olá e bem vindo {}{}'.format(cores['azul_neg'],nome))
###
#código das cores
###
# estilo: 0 padrão, 1 negrito, 4 sublinhado, 7 inverte cor
# texto: 30 a 37: bra, ver, verd, ama, azu, rox, azuc, cin
# fundo: 40 a 47: mesma coisa de cima
###

import random
cores = {'verde':'\033[1;4;32m',
         'vermelho':'\033[1;4;31m'}
num = random.randint(1,10)
print(num)
adiv = int(input('Adivinhe o número aleatório de 1 a 10 '))
if adiv == num:
    print('{}ganhou!'.format(cores['verde']))
else:
    print('{}perdeu!'.format(cores['vermelho']))
