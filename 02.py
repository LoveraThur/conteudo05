while True:
    try:    
        num = int(input('Digite um numero inteiro: '))
    except:
        print('\033[31mDigite um numero inteiro válido\033[m')
    else:
        if num > 0:
            print(f'O número {num} é positivo')
        else:
            print(f'O número {num} é negativo')
        break