prim = int(input('Digite o primeiro número da razão: '))
razao = int(input('Digite a razão: '))
termos = int(input('Quantos termos serão? '))
contador = 0
while contador < termos:
    if contador < 1:
        print(prim, end=' -> ')
        contador += 1
    else:
        print((prim + razao), end=' -> ')
        prim = prim + razao
        contador += 1
    if contador >= termos:
        print('Fim')
        mais = str(input('Quer vizualizar mais números? [s/n] ')).strip()
        termos = int(input('Quantos termos? '))
        if mais in 'sS' and termos > 0:
            prim = prim + razao
            contador = 0
        elif mais in 'nN' or termos == 0:
            print('Fim do programa')