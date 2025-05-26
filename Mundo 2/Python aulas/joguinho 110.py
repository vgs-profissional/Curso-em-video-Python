""" Jogo 110

jogo vai funcionar em um loop
no menu inicial vai perguntar se quer

[1] jogador vs máquina
[2] jogador vs jogador
[3] instruções
[4] sair do jogo

1 e 2- Aleatorizar quem joga primeiro -> mostrar os números disponiveis de cada jogador
-> perguntar qual número o jogador escolhe -> somar e mostrar o valor atual até alcançar 110
-> quem chegar a 110 ganha

3 - Dizer as regras do jogo:
'cada jogador tem 10 números (1-10) e deve escolher um para ser somado ao total, o total inicia como 0,
ao escolher o número ele será riscado e o jogador não poderá mais usar ele, vence quem chegar a 110'
"""
menu = escolha = sair = 0
menu_titulo = '110!'
menu_opcoes = '''[1] Jogador VS Máquina
[2] Jogador VS Jogador
[3] instruções
[4] sair do jogo'''
instrucoes = '''A pilha começa com 0 e cada jogador tem 10 números de 1 a 10
para escolher, quando um jogador escolhe um número, ele é riscado
(não pode mais ser usado) e somado a pilha, quem chegar a 110 ganha.'''
while True:
    if menu == 0:
        print('-='*16)
        print('{:^30}'.format(menu_titulo))
        print('{:^20}'.format(menu_opcoes))
        print('-='*16)
        escolha = int(input('> '))
        # escolhas
        if escolha == 1:
            print('Você escolheu jogar contra a máquina')
            break
        if escolha == 2:
            print('Você escolheu jogar contra o jogador')
            break
        if escolha == 3:
            print('-=' * 16)
            print(instrucoes)
            sair = int(input('''[digite 1 para voltar ao menu] 
> '''))
            if sair == 1:
                print('')
        if escolha == 4:
            print('Fim de jogo')
            break
