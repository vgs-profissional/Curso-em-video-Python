from datetime import date
maiores = 0
menores = 0
for x in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(x + 1)))
    idade = date.today().year - ano
    #Fiz a conta de quantos maiores e menores sem armazenar dados e sem separar cada um
    if idade >= 18:
        maiores += 1
    elif idade < 18:
        menores += 1

print('Ao todo houveram {} maiores de idade e {} menores de idade'.format(maiores, menores))
