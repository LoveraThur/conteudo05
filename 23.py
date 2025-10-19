while True:
    try:
        n = str(input('Digite um número\n>>> '))
        float(n)
    except:
        print('-'*30)
    else:
        try:
            n = float(n)
            if n % 1 == 0:
                print('O número é Inteiro')
            else:
                print('O número é Decimal')
        except:
            print('O número é Decimal')
        break