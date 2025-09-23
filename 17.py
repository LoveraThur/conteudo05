def menu(txt):
    tam = len(txt) + 4
    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)

menu('Calculador de Ano Bissexto')

ano = int(input('Digite um ano\n>>> '))
print('-'*30)
if ano % 4 == 0:
    print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não é um ano bissexto')