from funcoes import *

print('-'*30)
print('CALCULADORA'.center(30))
print('-'*30)
operacoes = ['+', '-', '*', '/']
while True:
    try:
        n1 = str(input('Digite o primeiro número: '))
        n2 = str(input('Digite o segundo número: '))
        n1 = float(n1)
        n2 = float(n2)
    except:
        print('\033[31mDigite ambos números válidos!\033[m')
        print('-'*30)
    else:
        print('-'*30)
        print('Operações'.center(30))
        print('Soma[+] \nSubtração[-] \nMultiplicação[*] \nDivisão[/]')
        print('-'*30)
        #operação
        op = ''
        
        while op not in operacoes:
            op= str(input('Digite a operação desejada \n>>> '))
        if op == '+':
            res = soma(n1, n2)
        elif op == '-':
            res = subtracao(n1, n2)
        elif op == '*':
            res = multiplicacao(n1, n2)
        else:
            res = divisao(n1, n2)
        print('-'*30)    
        print(f'O resultado da operação é {res:.2f} \nO número é {classificacao(res)} \nele é um número {positivo_or_not(res)} \nO número é {decimal_or_not(res)}')
        break
