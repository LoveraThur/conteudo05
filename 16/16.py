from funcoes import *    
menu('CALCULADOR DE BHASKARA')
while True:
    try:
        a = int(input('Digite um valor inteiro: '))
    except:
        print('\033[31mIsso é um número inteiro?\033[m')
        print('.'*30)
    else:
        break
print('-'*30)
while True:
    try: 
        b = int(input('Digite o segundo valor inteiro: '))
    except:
        print('\033[31mIsso é um valor inteiro?\033[m')
        print('.'*30)
    else:
        break
print('-'*30)
while True:
    try:
        c = int(input('Digite o terceiro valor inteiro: '))
    except:
        print('\033[31mIsso é um valor inteiro?\033[m')
        print('.'*30)
    else:
        break
print('-'*30)
print(bhaskara(a, b, c))
print('-'*30)