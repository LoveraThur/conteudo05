while True:
    try:
        n = int(input('Digite um número inteiro\n>>> '))
    except:
        print('\033[31mIsto é um número inteiro?\033[m')
        print('-'*30)
    else:
        if n % 2 == 0:
            print(f'\033[34mO número {n} é Par!\033[m')
        else:
            print(f'\033[33mO número {n} é Impar\033[m')
        break