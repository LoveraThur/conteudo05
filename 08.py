v1 = float(input('Digite o preço de um produto: R$'))
v2 = float(input('Digite o preço de outro produto: R$'))
v3 = float(input('Digite o preço do ultimo produto: R$'))

if v1 < v2 and v1 < v3:
    print(f'O Produto mais barato é o primeiro produto, custando R${v1:.2f}')
elif v2 < v1 and v2 < v3:
    print(f'O Produto mais barato é o segundo produto, custando R${v2:.2f}')
elif v3 < v1 and v3 < v2:
    print(f'O Produto mais barato é o terceiro produto, custando R${v3:.2f}')
