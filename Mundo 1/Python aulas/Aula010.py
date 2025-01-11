"""nome = str(input('Qual seu nome? ')).lower().strip().capitalize()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia {}'.format(nome)) """

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi de {:.1f}'.format(m))
print('Parabens' if m >= 6 else 'Estude mais')