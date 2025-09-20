#verifica se a nota é valida (max 10)
while True:
    nota1 = float(input('Primeira nota: '))
    if nota1 > 10:
        print('-'*30)
        print('\033[31mERRO! Nota max: 10\033[m')
    else:
        break
print('-'*30)
while True:
    nota2 = float(input('Segunda nota: '))
    if nota2 > 10:
        print('-'*30)
        print('\033[31mERRO! Nota max: 10\033[m')
    else:
        break
print('-'*30)

media = (nota1 + nota2) / 2

#verifica o aproveitamento
print(f'Suas notas foram: {nota1} e {nota2}.\nSua média foi {media}')
if media < 6:
    if media < 4:
        print('Seu aproveitamento foi \033[31;1mE\033[m. Melhore!')
    else:
        print('Seu aproveitamento foi \033[31mD\033[m. Melhore!')
    print('\033[31mREPROVADO\033[m')
else:
    if media >= 6 and media < 7.5:
        print('Seu aproveitamento foi \033[33;1mC\033[m. Não foi tão mal!')
    elif media >= 7.5 and media < 9:
        print('Seu aproveitamento foi \033[34;1mB\033[m. Uau, foi bem!')
    else:
        print('Seu aproveitamento foi \033[32;1mA\033[m. Você está de Parabéns!')
    print('\033[32mAPROVADO\033[m')
print('-'*30)