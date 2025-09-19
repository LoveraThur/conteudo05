semana = ['Domingo','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
print('-'*25)
while True:
    try:
        resp = int(input('Dia da semana: '))
    except:
        print('\033[31mDigite em numero[1 a 7]\033[m')
    else:
        if resp == 1:
            print(f'O dia {resp} corresponde a {semana[0]}')
            break
        elif resp == 2:
            print(f'O dia {resp} corresponde a {semana[1]}')
            break
        elif resp == 3:
            print(f'O dia {resp} corresponde a {semana[2]}')
            break
        elif resp == 4:
            print(f'O dia {resp} corresponde a {semana[3]}')
            break
        elif resp == 5:
            print(f'O dia {resp} corresponde a {semana[4]}')
            break
        elif resp == 6:
            print(f'O dia {resp} corresponde a {semana[5]}')
            break
        elif resp == 7:
            print(f'O dia {resp} corresponde a {semana[6]}')
            break
        else:
            print('\033[31mEste número não está disponivel\033[m')