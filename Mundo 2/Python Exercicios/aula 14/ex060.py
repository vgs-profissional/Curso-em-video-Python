num = int(input('Digite um número: '))
contador = num
fatorial = num
while contador <= num:
    if num > 1:
        print(contador,(contador - 1), fatorial)
        contador -= 1
        fatorial = fatorial * contador
    elif num == 0 or num == 1:
        print(1)
        contador = num + 1
        