dias = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos Quilômetros você andou com ele?'))
preco = (dias * 60) + (km * 0.15)
print('Por ter andado {}km por {} dias, você pagará R${:.2f}'.format(km, dias, preco))