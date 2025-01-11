altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))
metro_quadrado = largura * altura
baldes = metro_quadrado / 2
print('Sua parede tem a dimensões de {}x{} e área {:.2f}m²'.format(altura, largura, metro_quadrado))
print('você vai precisar de {:.1f} litros de tinta'.format(baldes))