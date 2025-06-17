precoTot = produtosMil = menorPreco = primeiro = 0
maisBarato = ' '
while True: 
    print(f'{'-'*30}\n{'Loja Super Baratão'.center(30)}\n{'-' *30}')
    produto = str(input('Nome do produto: ').strip())
    preco = float(input('Preço: R$ '))
    precoTot += preco
    continua = ' '
    while continua not in 'SsnN':
        print('-' * 30)
        continua = str(input('Quer continuar? [S/N] ').strip()[0])
    if preco >= 1000:
        produtosMil += 1
    if primeiro == 0 or preco < menorPreco:
        menorPreco = preco
        maisBarato = produto
        primeiro += 1        
    if continua in 'Nn':
        #print('O total da compra foi R${:.2f}'.format(precoTot))
        print(f'O total da compra foi {precoTot:.2f}')
        #print('Temos {} itens de R$1000 ou mais'.format(produtosMil))
        print(f'Temos {produtosMil} itens de R$1000 ou mais')
        #print('O produto mais barato foi {} que custa R${:.2f}'.format(maisBarato, menorPreco))
        print(f'O produto mais barato foi {maisBarato.capitalize()} que custa R${menorPreco:.2f}')
        break
    
    