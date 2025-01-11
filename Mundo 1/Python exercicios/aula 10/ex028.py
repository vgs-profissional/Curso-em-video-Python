from random import randint
from time import sleep
num_ale = randint(0, 5)
print('-=-' * 20)
print('{:>4} Adivinhe o número que estou pensando de 1 a 5'.format(' '))
print('-=-' * 20)
num_ad = int(input('Em quem número pensei? '))
print('Processando...')
sleep(2)
if num_ale == num_ad:
    print('PARABÉNS! Você acertou o número que pensei!')
else:
    print('Errouuuuu! eu pensei no número {}'.format(num_ale))