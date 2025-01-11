''' operadores artimeticos
     + - adição
     - - subtração
     * - multiplicação
     / - divisão
     ** - potência
     // - divisão inteira
     % - resto de devisão
     == igual em valor OU tipo
     === igual em valor E tipo

 ordem de precedência
    (), **, [*,/,//,%], [+,-]

 comandos uteis
    raiz - 25**(1/2) = 5.0
    potência - pow(2,2) = 4.0
    multiplicar strings - 'oi'*20 = oioioioioioioioioioioioioioioioioioioioi
    alinhamento dir - {:>20}!'.format(nome) =  [  espaço vazio  ] vasco!
    alinhamento esq - {:>20}!'.format(nome) =  vasco! [  espaço vazio  ]
    alinhamento centro - {:^20}!'.format(nome) = [espaço vazio] vasco! [  espaço vazio  ]
    alinhamento centro - {:=^20}!'.format(nome) = ==========vasco!==========
    quant. de casas decimais - '{:.3f}'.format(14.1234) = 14.123
    não quebrar linha - , end=''
    quebrar linha - \n
'''
n1 = float(input('Diga um número'))
n2 = float(input('Diga outro número'))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
di = n1 / n2
di_s = n1 // n2
e = n1 ** n2
print('Soma = {}, Subtração = {}, \n Multiplicação = {}, Divisão = {}'.format(soma,sub,multi,di), end='')
print('Sobra da divisão = {} e Potência = {}'.format(di_s, e))

