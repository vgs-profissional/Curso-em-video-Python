nome = str(input('Qual seu nome completo? '))
nome = nome.lower()
nome = nome.strip()
silva = 'silva' in nome
print('Seu nome tem silva nele? {}'.format(silva))