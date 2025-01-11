prim = int(input('Qual o primeiro número? '))
sec = int(input('Qual o segundo número? '))
ter = int(input('Qual o terceiro número? '))
maior = prim
#verifica o maior
if ter > sec and ter > prim: # 3 > 1,2
    maior = ter
if sec > prim and sec> ter: #2 > 1,3
    maior = sec
#verifica o menor
menor = sec
if ter < prim and ter < sec: #3 < 1,2
    menor = ter
if prim < sec and prim < ter: #1 < 2,3
    menor = prim
print('O maior é o {}'.format(maior))
print('O menor é o {}'.format(menor))
