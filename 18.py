def menu (txt):
    tam = len(txt) + 4
    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)

menu('Validador de Data')
while True:
    try:
        data = str(input('Insira a data [dia/mês/ano]\n>>>'))

        if int(data[0:2]) <= 31:
            if int(data[3:5]) <= 12:
                if len(data) == 10 or len(data) == 8:
                    if data[2] == '/' and data[5] == '/':
                        print('\033[32mEssa é uma data válida!/033[m]')
                        break
                    else:
                        print('\033[31mUtilize / para separar dia, mês e ano\033[m')
                        print('-'*30)
                else:
                    print('\033[31mA data deve conter 8 ou 10 caracteres\033[m')
                    print('-'*30)
            else:
                print('\033[31mVocê já viu esse mês?\033[m')
                print('-'*30)            
        else:
            print('\033[31mEste dia existe?\033[m')
            print('-'*30)
    except:
        print('\033[31;1mERRO! Digite corretamente\033[m')