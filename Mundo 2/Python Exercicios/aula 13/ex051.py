prim = int(input('Qual será o primeiro termo: '))
razao = int(input('Qual será a razão: '))
decimo = prim + (10 - 1) * razao
for x in range(prim, decimo + razao, razao):
    print('{}'.format(x),end=' -> ')
print('Acabou!', end='')
