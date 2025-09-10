while True:
    try:
        sexo = str(input('Digite seu sexo[M/F]: ')).upper()
    except (KeyboardInterrupt):
        print('\n\033[31mO usuário decidiu nao informar o sexo, e encerrar o programa\033[m')
        break
    
    else:
        if sexo == 'M':
            print('\033[34mVocê é homem\033[m')
            break
        elif sexo == 'F':
            print('\033[35mVocê é mulher\033[m')
            break
        else:
            continue