from random import randint 
soma = valor = maquina = jogar = vitorias = 0
parimpar = textoparimpar = ''
print('-=-' * 10)
print('Vamos jogar Para ou Ímpar!')
print('-=-' * 10)
while jogar == 0:
    maquina = randint(0,10)
    valor = int(input('Digite um valor [0 a 10]: '))
    parimpar = str(input('Par ou Impar? [P/I] ').lower()) 
    soma = valor + maquina
    print('-' * 45)   
    if soma % 2 == 0:
        print('Você jogou {} e eu joguei {}. A soma é {} que é Par'.format(valor, maquina, soma))
        print('-' * 45)
        if parimpar == 'par' or parimpar == 'p':
            vitorias += 1
            print('Você ganhou!')
            print('Vamos jogar novamente...')
        elif parimpar == 'impar' or parimpar == 'i':
            print('Você perdeu!')
            print('Você venceu {} vezes'.format(vitorias))
            jogar+=1
    else:
        print('Você jogou {} e eu joguei {}. A soma é {} que é Ímpar'.format(valor, maquina, soma))
        print('-' * 45)
        if parimpar == 'impar' or parimpar == 'i':
            vitorias += 1
            print('Você ganhou!')
            print('Vamos jogar novamente...')
        elif parimpar == 'par' or parimpar == 'p':
            print('Você perdeu!')
            print('Você venceu {} vezes'.format(vitorias))
            jogar+=1   

                

