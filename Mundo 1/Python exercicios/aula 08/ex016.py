from math import trunc
import random

print('Gerando número aleatório...')
num = random.random() * 100
'''truncado = trunc(num)'''
print("A parte inteira de {:.3f} é {}, isso é truncar um número".format(num, int(num)))
