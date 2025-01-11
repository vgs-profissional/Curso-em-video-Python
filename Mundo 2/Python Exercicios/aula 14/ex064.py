num = float(input('Digite um número (999 faz o programa parar) '))
soma = num
quant = 1
while num != 999:
    num = float(input('Digite um número: '))
    if num != 999:
        soma += num
        quant += 1
    else:
        print('Você digitou {} números e a soma deles é: {:.0f}'.format(quant, soma))
print('Fim')