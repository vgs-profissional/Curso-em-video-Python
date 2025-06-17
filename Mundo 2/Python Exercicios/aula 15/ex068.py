from random import randint 
soma = valor = maquina = jogar = vitorias = 0
print('-=-' * 10)
print('Vamos jogar Para ou Ímpar!')
print('-=-' * 10)
while True:
    maquina = randint(0,10)
    valor = int(input('Digite um valor [0 a 10]: ')) 
    soma = valor + maquina
    parimpar = ' '
    while parimpar not in 'pi':
        parimpar = str(input('Par ou Impar? [P/I] ').strip().lower()[0])
    print('Você jogou {} e eu joguei {}. A soma é {}.'.format(valor, maquina, soma), end='')
    print('Deu Par' if soma % 2 == 0 else 'Deu Ímpar')
    print('-' * 45)
    if parimpar == 'p':
        if soma % 2 == 0:
            vitorias += 1
            print('Você ganhou!\nVamos jogar novamente...')
        else:
            print('Você perdeu! \nVocê venceu {} vezes'.format(vitorias))
            break
    elif parimpar == 'i':
        if soma % 2 == 1:
            vitorias += 1
            print('Você ganhou!\nVamos jogar novamente...')
        else:
            print('Você perdeu! \nVocê venceu {} vezes'.format(vitorias))
            break

                

