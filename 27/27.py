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
morangos = strawberry(morango)
macas = apple(maca)
if morango > 8 or morangos > 25:
    morangos = morangos - ((10/100)*morangos)
    print(f'=> Você irá pagar R${morangos} nos morangos')
else:
    print(f'=> Você irá pagar R${morangos} nos morangos')
if maca > 8 or macas > 25:
    vmacas = macas - ((10/100)*macas)
    print(f'=> Você irá pagar R${macas} nas maçãs')
else:
    print(f'=> Você irá pagar R${macas} nas maçãs')
