from funcoes import *
litros = menu('Venda de Combustíveis')
escolha = combustivel()
if escolha == 'A':
    print(f'Você irá pagar R${alcool(litros):.2f} por {litros}L de Alcool')
else:
    print(f'Você irá pagar R${gasolina(litros):.2f} por {litros}L de gasolina')