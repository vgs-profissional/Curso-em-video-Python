nome = str(input('Qual seu nome? ')).lower().strip()
if nome == 'Vasco':
    print('Que nome bonito')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome == 'ana' or nome == 'jessica' or nome == 'paula':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))