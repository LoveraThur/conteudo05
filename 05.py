
while True:
    try:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
    except:
        print('\033[31;1mIsso é uma nota?\033[m')
    else: 
        break

media = (nota1 + nota2) / 2

if media >= 0 and media < 7:
    print('\033[31;1mREPROVADO! \033[m')
elif media >= 7 and media <10:
    print('\033[31;1mAPROVADO! \033[m')
else:
    print('\033[33;1m TIROU 10! \033[m')
