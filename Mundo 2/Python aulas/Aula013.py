# LAÇOS  DE REPETIÇÃO #
# RECEBE VÁRIOS PARÂMETROS PRA ITERAR #
'''for c in range(-1, 10, 2): #de, até e de quanto em quanto

    print(c)'''

'''n = int(input('Digite um número'))
for n in range (0, n+1):
    print(n)
print('fim')'''

'''inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passos: '))

for a in range(inicio, fim+1, passo):
    print(a)
print('fim')'''

'''for n in range(0,3):
    c = int(input('Diga um numero'))
print(c)'''

s = 0
for c in range(0,5):
    n = int(input('Diga um número: '))
    s += n
print('A soma dos números é {}'.format(s))