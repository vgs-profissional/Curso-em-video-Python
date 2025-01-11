salario = float(input('Vou aumentar seu salário em 15%, quanto ele é atualmente? R$:'))
salario_aumento = salario + (salario * (15/100))
print('Seu salário era R${:.2f}, aumentou em 15% e passou a ser R${:.2f}'.format(salario, salario_aumento))