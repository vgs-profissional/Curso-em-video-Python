maior_peso = 0
menor_peso = 0
for x in range (1, 6):
    per_peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maior_peso = per_peso
        menor_peso = per_peso
    else:
        if per_peso >  maior_peso:
            maior_peso = per_peso
        if per_peso < menor_peso:
            menor_peso = per_peso

print('O maior peso foi {}Kg e o menor foi {}Kg'.format(maior_peso, menor_peso))