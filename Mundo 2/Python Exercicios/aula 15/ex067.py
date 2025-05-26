contagem = 1
while True: 
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        print('Tabuada encerrada. Volte sempre!')
        break
    print('-' * 30)
    while contagem < 11:
        print('{} x {} = {}'.format(num, contagem, num * contagem))
        contagem += 1
    print('-' * 30)
    contagem = 1