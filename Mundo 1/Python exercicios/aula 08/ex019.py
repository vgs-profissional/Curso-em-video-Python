from random import choice
n1 = str(input('Escolha o primeiro aluno: '))
n2 = str(input('Escolha o segundo aluno: '))
n3 = str(input('Escolha o terceiro: '))
n4 = str(input('Quarto: '))
lista = [n1, n2, n3, n4]
print('O aluno escolhido foi {}'.format(choice(lista)))