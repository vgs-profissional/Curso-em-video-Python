salario = float(input('Qual o salário do funcionário? R$'))
salario_novo = 1

cores = {'verde_neg_sub':'\033[1;4;32m',
         'verde_neg':'\033[1;32m',
         'verde':'\033[32m',
         'limpo':'\033[m'}

if salario < 1250:
    salario_novo = salario + (salario * 0.15) #salario * 15 / 100 tb funciona
else:
    salario_novo = salario + (salario * (10 / 100))# sem () cobrindo 10 / 100 tb funciona
print('O novo salário desse funcionário será {}R${:.2f}{} \nHouve um aumento de {}R$:{:.2f}'.format(cores['verde'],salario_novo,cores['limpo'],cores['verde_neg_sub'], (salario_novo - salario)))