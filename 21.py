print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)

while True:
    try:
        valor = float(input('digite o valor que deseja sacar:\n>>> R$'))
    except:
        print('\033[31mDigite um valor válido!\033[m')
        print('-'*30)
    else:
        if valor > 10 and valor <=600:
            break
        else:
            if valor < 10:
                print('\033[33mO valor deve ser maior que R$10\033[m')
            elif valor > 600:
                print('\033[33mO valor deve ser menor que R$600\033[m')
            print('-'*30)
            continue
nt_100 = 0
nt_50 = 0
nt_10 = 0
nt_5 = 0
nt_1 = 0
while True:
    if valor - 100 >= 0:
        valor -= 100
        nt_100 += 1
    elif valor - 50 >= 0:
        valor -= 50
        nt_50 += 1
    elif valor - 10 >= 0:
        valor -= 10
        nt_10 += 1
    elif valor - 5 >= 0:
        valor -= 5
        nt_5 += 1
    elif valor - 1 >= 0:
        valor -= 1
        nt_1 += 1
    else:
        break

print('='*30)
print('\033[32;1mSaque efetuado com sucesso!\033[m')
print(f'Notas de 100: {nt_100}')
print(f'Notas de 50: {nt_50}')
print(f'Notas de 10: {nt_10}')
print(f'Notas de 5: {nt_5}')
print(f'Notas de 1: {nt_1}')