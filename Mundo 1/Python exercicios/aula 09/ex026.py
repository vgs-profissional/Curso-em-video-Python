frase = str(input('Digite uma frase: ')).lower()
frase = frase.strip()
a = frase.count('a')
print('A letra A aparece {} vezes na frase\nAparece pela primeira vez na posição {}\nAparece pela ultima vez na posição {}'.format(a,frase.find('a')+1,frase.rfind('a')+1))