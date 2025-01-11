nome = str(input('Qual seu nome completo: ')).strip().split()
print('Prazer em te conheçer\n'
      'seu primeiro nome é {}\n'
      'e seu ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))
