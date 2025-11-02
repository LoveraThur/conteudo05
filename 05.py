
while True:
    try:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
    except:
        print('\033[31;1mIsso é uma nota?\033[m')
    else: 
        break

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print('\033[32;1mAPROVADO! \033[m')
elif media == 10:
    print('\033[33;1mAPROVADO COM DISTINÇÃO! \033[m')
elif media < 7:
    print('\033[31;1m REPROVADO! \033[m')
else:
    print('\033[34mSua média foi maior que 10.\nEste programa calcula media até 10 apenas.\033[m')