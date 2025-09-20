from funcoes import *
    
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))

print('-'*30)
triangulo = valida_triangulo(n1, n2, n3)

if triangulo == True:
    classificacao(n1, n2, n3)
else:
    pass