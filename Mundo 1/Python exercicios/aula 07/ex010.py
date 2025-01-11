real = float(input('Quanto você tem na carteira? R$:'))
dolar = real / 4.96
euro = real / 5.38
iene = real /0.034
print('Você teria US${:.2f} dolares'.format(dolar))
print('€{:.2f} em euros'.format(euro))
print('¥{:.2f} em ienes'.format(iene))