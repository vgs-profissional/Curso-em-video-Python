peso = float(input('Quanto você pesa(Kg)? '))
altura = float(input('Qual sua altura(Cm)? ')) / 100

imc = peso / (altura * altura) #ou pode ser altura ** 2

print('Seu imc (indíce de massa corpórea) é de {:.1f}'.format(imc))
print('Você está ', end='')
if imc <= 18.5 :
    print('abaixo do peso ideal') #não precisa de < or >, cai no primeiro caso que couber
elif imc <= 25:
    print('no peso ideal')
elif imc <= 30:
    print('em sobrepeso')
elif imc <= 40:
    print('está obeso')
else:
    print('com obesidade morbida')
