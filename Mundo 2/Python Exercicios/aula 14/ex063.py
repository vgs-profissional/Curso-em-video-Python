print('-='*20 + '\n        Sequência de Fibonacci \n' + '-='*20)
limite = int(input('Quantos números você quer ver? '))
num_ini = 1
prime_ant = 0
segun_ant = 0
conta = 0
contagem = 0

while contagem < limite:
    if contagem < 1:
        conta = num_ini + prime_ant
        prime_ant = segun_ant
        segun_ant = conta
        contagem += 1
        print(num_ini, end=' -> ')
        print(conta, end=' -> ')
    else:
        prime_ant = segun_ant
        segun_ant = conta
        conta = prime_ant + segun_ant
        contagem += 1
        print(conta, end=' -> ')
print('FIM')
