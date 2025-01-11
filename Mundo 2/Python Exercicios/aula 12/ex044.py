cor = {'g':'\033[32m' ,
       'b':'\033[34m',
       'r':'\033[31m',
       'f':'\033[m'}
print('{:=^40}'.format(' Lojas Guanabara '))
preco = float(input('Qual o valor das compras? R$'))
pagamento = str(input('''Dependendo de como irá pagar, haverá desconto. 
Qual será a forma de pagamento? 
(dinheiro/cheque[1],débito[2] ou crédito[3]) ''')).strip().lower()

if pagamento == 'dinheiro' or pagamento == 'cheque' or pagamento == '1':
    print('Ganha 10% de desconto, ficaria a {}R${:.2f}{}'.format(cor['g'],preco -(preco * 0.10), cor['f']))
elif pagamento == 'debito' or pagamento == '2':
    print('Ganha 5% de desconto, ficaria a {}R${:.2f}{}'.format(cor['g'],preco - (preco * 0.05),cor['f']))
elif pagamento == 'credito' or pagamento == '3':
    parcela = int(input('Se parcelar acima de 2x terá juros de 20%. Quantas parcelas? '))
    if parcela >= 3:
        juros = preco + (preco * 0.20)
        print('Com 20% de juros ficaria a {}R${:.2f}{} \nSerão {} parcelas de R${:.2f}'.format(cor['r'],juros,cor['f'],parcela,(juros / parcela)))
    else:
        print('Serão {} parcela(s) de R${:.2f}'.format(parcela, preco / parcela))
else:
    print('{}Opção de pagamento inválida, tente novamente.{}'.format(cor['r'], cor['f']))
