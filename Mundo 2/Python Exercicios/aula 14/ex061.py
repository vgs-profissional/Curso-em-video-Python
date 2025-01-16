primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão dos termos: '))
contagem = 1

while contagem <= 10:
    print('{} ->'.format(primeiro), end=' ')
    primeiro += razao
    contagem += 1
print('Fim')
