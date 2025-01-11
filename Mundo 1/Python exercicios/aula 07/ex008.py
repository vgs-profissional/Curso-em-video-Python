metro = float(input('Diga um valor em metros:'))
decimetro = metro * 10
centimetros = metro * 100
milimetro = metro * 1000
dam = metro / 10
hm = metro / 100
km = metro / 1000
print('Essa medida equivale a {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(decimetro, centimetros, milimetro))
print('Essa medida equivale a {}dam, {}hm e km{}'.format(dam, hm, km))