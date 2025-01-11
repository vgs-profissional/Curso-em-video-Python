texto = str(input('Digite uma frase: ')).strip().upper()
palavra = texto.split()
junto = ''.join(palavra)
otxet = ''
"""tb da pra usar só otxet = junto[::-1] que faz o mesmo sem usar for"""
for x in range(len(junto) -1, -1, -1):
    otxet += junto[x]
if otxet == junto:
    print('{} É um palindromo'.format(otxet))
else:
    print('{} Não é um palindromo')
