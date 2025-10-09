while True:
    num = int(input('Digite um número menor de 1000\n>>> '))
    a = str(num)
    if num > 1000 or num < 0:
        print('\033[31mMENOR que 1000!\033[m')
    else:
        if len(a) == 4:
            print(f'{num} = ', end='')
            print(f'{a[0]} Milhare(s), ', end='')
            print(f'{a[1]} Centena(s), ', end='')
            print(f'{a[2]} Dezena(s) e ', end='')
            print(f'{a[3]} Unidade(s)')
            break

        elif len(a) == 3:
            print(f'{num} = ', end='')
            print(f'{a[0]} Centena(s), ',end='')
            print(f'{a[1]} Dezena(s) e ',end='')
            print(f'{a[2]} Unidade(s)')
            break
        
        elif len(a) == 2:
            print(f'{num} = ', end='')
            print(f'{a[0]} Dezena(s) e ', end='')
            print(f'{a[1]} Unidade(s)')
            break
        
        else:
            print(f'{num} = ', end='')
            print(f'{a[0]} Unidade(s)')
            break