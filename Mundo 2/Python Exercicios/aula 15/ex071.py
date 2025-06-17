print('='*30)
print('Banco CEV'.center(30,' '))
print('='*30)
divide_cinq = 0 
while True:
    sacar = int(input('Quanto você quer sacar? R$'))
    divide_cinq = round(sacar / 50)
    resto_divide = sacar - (divide_cinq * 50)
    divide_dez = round(resto_divide / 10)
    resto_divide = sacar - (divide_dez * 10)
    divide_um = round(resto_divide / 1)
    if divide_cinq > 1:
        print(f'Total de {divide_cinq} cédulas de R$50')
    if divide_dez % 2 == 0:
        print(f'Total de {divide_dez} cédulas de R$20')
    if divide_um > 1:
        print(f'Total de {divide_um} cédulas de R$1')
    print(f'sacar - (divide * 50 = {resto_divide})')
    break