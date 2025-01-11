num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

n = 0
while n < 1:
    operaçao = int(input('Escolha uma operação para fazer com os números \n[1] Soma \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa \n'))
    if operaçao == 1:
        print('A soma de {:.0f} mais {:.0f} é {:.0f}'.format(num1, num2, (num1 + num2)))
    elif operaçao == 2:
        print('O produto de {:.0f} e {:.0f} é {:.0f}'.format(num1, num2, (num1 * num2)))
    elif operaçao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior entre {:.0f} e {:.0f} dois é {:.0f}'.format(num1, num2, maior))
    elif operaçao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif operaçao == 5:
        print('Fim do programa')
        n += 1
