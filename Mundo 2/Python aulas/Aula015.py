"""n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')"""

nome = 'José'
idade = 33
salario = 9000
print(f'O {nome:^20} tem {idade:-<} anos e ganha {salario:.2f}')
"""print(f'O {nome} tem {idade} anos') #python 3.6+
print('O {} tem {}'.format(nome, idade)) #python 3
print('O %s tem %d' % (nome, idade)) #python 2"""