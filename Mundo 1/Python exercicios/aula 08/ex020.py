from random import shuffle
nome1 = str(input('Diga o primeiro nome: '))
nome2 = str(input('Diga o segundo nome: '))
nome3 = str(input('O terceiro: '))
nome4 = str(input('Quarto: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(lista)