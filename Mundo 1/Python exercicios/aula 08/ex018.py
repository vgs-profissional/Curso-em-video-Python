import math
an = float(input('Qual o valor do ângulo? '))
rad = an * (math.pi/180)
print('O seno desse valor é: {:.2f}\no Cosseno é: {:.2f}\ne a Tangente é: {:.2f} '.format((math.sin(rad)), math.cos(rad), math.tan(rad)))