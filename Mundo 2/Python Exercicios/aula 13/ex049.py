num = int(input('Diga um número que você quer saber a tabuada: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num * i)))
