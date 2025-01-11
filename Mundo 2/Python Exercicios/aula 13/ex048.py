a = 0
contagem = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        a += x
        contagem += 1
print('Entre 1 e 500 tem {} números ímpares multiplos de 3 e a soma deles é {}'.format(contagem, a))
