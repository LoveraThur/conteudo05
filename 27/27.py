from funcoes import *
while True:
    try:
        morango = float(input('Quantidade de morangos a serem comprados [Kg]\n>>> '))
    except:
        print('\033[31mDigite um valor válido!\033[m')
        print('-'*30)
    else:
        break

print('-'*30)
while True:
    try:
        maca = float(input('Quantidade de maçãs a serem compradas [Kg]\n>>> '))
    except:
        print('\033[31mDigite um valor válido!\033[m')
        print('-'*30)
    else:
        break