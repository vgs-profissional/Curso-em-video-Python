menor = maior = quantidade = media = 0
continuar = 's'

while continuar in 'Ss':
    pergunta = float(input('Digite um número: '))
    quantidade += 1
    media += pergunta
    media /= quantidade
    if quantidade == 1:
        maior = menor = pergunta
    elif pergunta > maior:
        maior = pergunta
    elif pergunta < menor:
        menor = pergunta
    continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()
print("""Você digitou {} números e a média foi {:.1f}
O maior valor foi {:.0f} e o menor foi {:.0f}""".format(quantidade, media, maior, menor))
