while True:
    try:
        sallary = float(input('Digite seu Salário: R$'))
    except:
        print('\033[31mPor acaso isso é um salário?\033[m')
    else:
        if sallary <= 280:
            print('-'*30)
            porcent = sallary * (20 /100)
            aumento = sallary + porcent
            print(f'Você teve um aumento de 20%\nSeu novo salário é {aumento}')

        elif sallary > 280 and sallary <= 700:
            print('-'*30)
            porcent = sallary * (15 / 100)
            aumento = porcent + sallary
            print(f'Você teve um aumento de 15%\nSeu novo salário é {aumento}')

        elif sallary > 700 and sallary <= 1500:
            print('-'*30)
            porcent = sallary * (10 / 100)
            aumento = sallary + porcent
            print(f'Você teve um aumento de 10%\nSeu novo salário é {aumento}')
        else:
            print('-'*30)
            porcent = sallary * (5 / 100)
            aumento = sallary + porcent
            print(f'Você teve um aumento de 5%\nSeu novo salário é {aumento}')
    break