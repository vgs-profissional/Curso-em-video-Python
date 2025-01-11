import random
import time
print('Vamos jogar pedra, papel e tesoura\n[ 0 ] pedra \n[ 1 ] papel \n[ 2 ] tesoura')
mao = int(input('O que você escolhe? '))
if(mao == (0,1,2)):
    lista = ['pedra', 'papel', 'tesoura']
    mao_robo = random.randint(0,2)

    print('Jô')
    time.sleep(0.5)
    print('Ken')
    time.sleep(0.5)
    print('Pô!')

    print('-='*20)
    print('Você escolheu {} e eu escolhi {}'.format(lista[mao],lista[mao_robo]))
    print('-='*20)
    if mao == mao_robo:
        print('Empate!')
    elif (mao == 0 and mao_robo == 2) or (mao == 1 and mao_robo == 0) or (mao == 2 and mao_robo == 1): #0 pedra, 1 papel, 2 tesoura
        print('Você venceu!')
    else:
        print('Você perdeu!')
else:
    print('Resposta inválida, tente novamente')
