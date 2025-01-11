nome = str(input('Diga seu nome completo: '))
nomeSeparado = nome.split()

print('Analisando cadeia de caracteres...')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(nomeSeparado[0])))