while True:
    try:
        n = str(input('Digite um número\n>>> '))
        float(n)
    except:
        print('-'*30)
    else:
        try:
            int(n)
        except:
            print(f'O número {n} é decimal')
        else:
            print(f'O número {n} é inteiro')
        print('-'*30)
        break