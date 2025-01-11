distancia = float(input('Qual será a distância da viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(distancia))

#valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45 - if simplificado, igual operador ternario
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço da passagem será de R${:.2f}'.format(valor))