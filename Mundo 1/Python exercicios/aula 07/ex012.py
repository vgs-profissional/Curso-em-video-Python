preco = float(input('Qual o preço do produto que você quer levar?'))
desconto = preco - (preco * 5/100)
print('O produto que custava R${:.2f} antes agora vai custar R${:.2f} na promoção'.format(preco, desconto))
