vel_carro = float(input('Qual a velocidade atual do seu carro? '))
multa = ((vel_carro - 80) * 7)
if vel_carro > 80:
    print('Ultrapassou o limite permitido de 80km/h! Será multado em R$:{:.2f}'.format(multa))
print('Abaixo do limite, pode prosseguir!')