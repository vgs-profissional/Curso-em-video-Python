celsius = float(input('Informe a temperatura em ºC:'))
farenheit = (celsius * 9) / 5 + 32
print('Essa mesma temperatura m Farenheit é {}ºF'.format(farenheit))
kelvin = ((farenheit - 32) * 5) / 9 + 273.15
print('Essa temperatura em Kelvin é {}K'.format(kelvin))

