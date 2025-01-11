n = 0
menor = 0
maior = 0
primeiro = 1
media = 0
quantidade = 0
conta = 0
while n < 1:
    pergunta = float(input('Digite um número: '))
    quantidade += 1
    media += pergunta
    media = media / quantidade
    if primeiro == 1:
        maior = menor = pergunta
        primeiro -= 1
    elif pergunta > maior:
        maior = pergunta
    elif pergunta < menor:
        menor = pergunta
    continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()
    if continuar in 'Nn':
        n += 1
    elif continuar in 'Ss':
        n = 0
    print('Pergunta {}, Maior {}, Menor {}, Media {}, Quantidade {}'.format(pergunta, maior, menor, media, quantidade))