print(f'='*30)
print(f'Banco CEV'.center(30))
print(f'='*30)
sacar = int(input('Quanto você quer sacar? R$'))
total = sacar
cedulaAtual = 50 
cedulas = 0
while True:
    if cedulaAtual <= total:
        total -= cedulaAtual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total de {cedulas} cédulas de R${cedulaAtual}')
        if cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1
        cedulas = 0
        if total == 0:
            break