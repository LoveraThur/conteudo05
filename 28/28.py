from funcoes import *
menu('Promoção Tabajara')

steak = 0
while True:
    try:
        steak = int(input('Carne desejada: \n>>> '))
        if steak >3 or steak <= 0:
            print('\033[31mDigite uma opção válida!\033[m')
            print('-'*25)
        else:
            break
    except:
        print('\033[31mOpção inválida\033[m')
        print('-'*25)

print('-'*25)
while True:
    try:
        amount = float(input('Quantidade desejada[Kg]: \n>>> '))
    except:
        print('\033[31mDigite uma opção válida!\033[m')
    else:
        break

print('-'*25)
card = ''
while True:
    card = str(input('Deseja utilizar o cartão Tabajara? [S/N] ')).upper()
    if card not in 'SN':
        print('\033[31mDigite uma opção válida\033[m')
        continue
    else:
        break
print('-'*25)
if steak == 1:
    carne_valor = fileDuo(amount, card)
    print(f'Você comprou {amount}KG de \033[33mFilé Duplo\033[m')
elif steak == 2:
    carne_valor = alcatra(amount, card)
    print(f'Você comprou {amount}KG de \033[33mAlcatra\033[m')
else:
    carne_valor = picanha(amount, card)
    print(f'Você comprou {amount}KG de \033[33mPicanha\033[m')
if card == 'S':
    print('Você decidiu pagar no cartão Tabajara e teve \033[34m5% de desconto\033[m')
else:
    print('Infelizmente você não pagou no cartão tajabara e não teve \033[34m5% de desconto\033[m')

print(f'Sua compra deu um total de \033[32mR${carne_valor:.2f}\033[m')

print('-'*25)