import random as random
n = 0
palpites = 0
numAleatorio = random.randint(1, 10)
print('Tente adivinhar que número inteiro de 1 a 10 eu estou pensando')
while n < 1:
    escolha = int(input('Número: '))
    palpites += 1
    if escolha == numAleatorio:
        print('Correto, eu pensava no número {}, você precisou de {} tentativas pra acertar'.format(numAleatorio, palpites))
        n += 1
    if escolha != numAleatorio:
        if escolha > numAleatorio:
            print('Menor que isso, tente novamente')
        else:
            print('Maior que isso, tente novamente')
