valor = input('Digite qualquer valor')
print('O que você digitou é do tipo {}'.format(type(valor)))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfa-numerico?', valor.isalnum())
print('Está em caixa alta?', valor.isupper())
print('Está em caixa baixa?', valor.islower())
print('Está capitalizada? (min. 1 letra maiúscula)', valor.istitle())

