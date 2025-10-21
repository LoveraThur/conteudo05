def alcool(litros):
    preco = 1.9
    if litros <= 20:
        reduzido = litros -((3/100) * litros)
    else:
        reduzido = litros -((5/100) * litros)
    valor = preco * reduzido
    return valor

def gasolina(litros):
    preco = 2.5
    if litros <= 20:
        reduzido = litros -((4/100)* litros)
    else:
        reduzido = litros - ((6/100)* litros)
    valor = preco * reduzido
    return valor

def menu(txt):
    tam = len(txt) + 8
    print('-'* tam)
    print(txt)
    print('-'* tam)
    litros = float(input('quantos litros você deseja? \n>>> '))
    print('-'*tam)
    return litros

def combustivel():
    print('Escolha o tipo de combustível \n A- Alcool \n G- Gasolina')
    escolha = ' '
    while True:
        try:
            escolha = str(input('>>> ')).upper()
            if escolha == 'G' or escolha == 'A':
                return escolha
            else: 
                print('\033[31mEscolha inválida\033[m')
        except:
            print('\n\033[31mEscolha inválida\033[m')
            