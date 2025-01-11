from math import hypot
cat_adj = float(input('Qual o tamanho do cateto adjacente? '))
cat_opo = float(input('Qual o tamanho do cateto oposto? '))
hip = hypot(cat_adj, cat_opo)
print('O comprimento da hipotenusa é: {:.2f}'.format(hip))
