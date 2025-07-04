tupla = ('zero', 'um', 'dois', 'três', 'quatro','cinco','seis','sete','oito'
         ,'nove','dez','onze','doze','treze','cartorze','quinze','dezesseis'
         ,'dezessete','dezoito','dezenove','vinte')

while True:
    posicao = int(input('Digite um número entre 0 e 20 '))
    if posicao <= 20:
        break
print(f'Esse número escrito por extenso é {tupla[posicao]}')