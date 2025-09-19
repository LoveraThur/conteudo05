from funcoes import *
def menu(texto):
    tam = len(texto) + 12
    print('='*tam)
    print('\033[1;32m',texto.center(tam),'\033[m')
    print('='*tam)

    print(f'Salario Bruto:      R${str(salarioBruto).replace('.', ',')}0')
    
    salarioIR= IR(salarioBruto)
    print(f'(-)IR({salarioIR[1]}%):          R${str(salarioIR[0]).replace('.', ',')}0')
    
    salarioINSS = INSS(salarioBruto)
    print(f'(-) INSS(10%):      R${str(salarioINSS).replace('.', ',')}0')
    
    salarioFGTS = FGTS(salarioBruto)
    print(f'FGTS(11%):          R${str(salarioFGTS).replace('.', ',')}0')

    descTT= descontos(salarioIR[0], salarioINSS) 
    print(f'Total de Descontos: R${(str(descTT).replace('.', ','))}0')

    salario_liq = salarioBruto - descTT
    print(f'Salario Liquido:    R${str(salario_liq).replace('.', ',')}0')

    print('='*tam)



while True:
    try:
        hr = float(input('Digite a quantidade de horas trabalhadas no MÊS: '))
        valor_hr = float(input('Digite o valor de suas horas: '))
    except:
        print('\033[31mIsso é um salário?\033[m')
    else:
        salarioBruto = hr * valor_hr
        menu('FOLHA DE PAGAMENTO')
        break