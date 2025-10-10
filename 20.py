while True:
    try:
        nota1 = float(input('Digite a Primeira nota: '))
    except:
        print('\033[31mDigite uma nota válida!\033[m')
    else:
        if nota1 > 10 or nota1 < 0:
            print('\033[31mA nota deve ser entre 0 e 10\033[m')
            print('-'*30)
            continue
        else:
            break
print('='*30)
while True:
    try:
        nota2 = float(input('Digite a Segunda nota: '))
    except:
        print('\033[31mDigite uma nota válida!\033[m')
    else:
        if nota2 > 10 or nota2 < 0:
            print('\033[31mA nota deve ser entre 0 e 10\033[m')
            print('-'*30)
            continue
        else:
            break
print('='*30)
while True:
    try:
        nota3 = float(input('Digite a Terceira nota: '))
    except:
        print('\033[31mDigite uma nota válida!\033[m')
    else:
        if nota3 > 10 or nota3 < 0:
            print('\033[31mA nota deve ser entre 0 e 10\033[m')
            print('-'*30)
            continue
        else:
            break
print('='*30)

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print(f'Sua média foi: {media:.2f} \nVocê foi \033[31mREPROVADO!\033[m')
if media >=7 and media < 10:
    print(f'Sua média foi: {media:.2f} \nVocê foi \033[32mAPROVADO!\033[m')
if media == 10:
    print(f'Sua média foi: {media:.2f} \nVocê foi \033[34mAPROVADO COM DISTINÇÃO!\033[m')