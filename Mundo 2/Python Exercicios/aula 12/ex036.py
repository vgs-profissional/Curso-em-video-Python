casa_valor = float(input('Qual o valor casa?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos pretende pagar?'))

prestacao = casa_valor / (anos * 12)

cores = {'vermelho': '\033[0;31m', 'verde': '\033[0;32m'}
print('A parcela seria de R${:.2f} ao mês'.format(prestacao))
if prestacao > (salario + (salario * 0.3)):
    print('{}Emprestimo negado, você não pode financiar esta casa'.format(cores['vermelho']))
else:
    print('{}Emprestimo conscedido'.format(cores['verde']))
