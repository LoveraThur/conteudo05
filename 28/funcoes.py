def fileDuo(qtd,cartao):
    qtd = qtd
    if qtd <= 5:
        valor = qtd * 4.90
    else:
        valor = qtd * 5.80
    if cartao == 'S':
        valor = valor - ((5/100)* valor)
    return valor

def alcatra(qtd, cartao):
    qtd = qtd
    if qtd <= 5:
        valor = qtd * 5.90
    else:
        valor = qtd * 6.80
    if cartao == 'S':
        valor = valor -((5/100)* valor)
    else:
        pass
    return valor

def picanha(qtd, cartao):
    qtd = qtd
    if qtd <= 5:
        valor = qtd * 6.90
    else:
        valor = qtd * 7.80
    if cartao == 'S':
        valor = valor -((5/100)* valor)
    return valor

def menu(txt):
    tam = len(txt)+8
    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)
    print('Filé Duplo[1] \nAlcatra[2] \nPicanha[3]')
    print('-'*tam)