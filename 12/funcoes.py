def IR(salario):
    if salario <= 900:
        desconto = 0
        desc = 'isento'
        return desconto, desc
    elif salario > 900 and salario <= 1500:
        desconto = salario * (5/100)
        desc = 5
        return desconto, desc
    elif salario > 1500 and salario <=2500:
        desconto = salario * (10/100)
        desc = 10
        return desconto, desc
    else:
        desconto = salario * (20/100)
        desc = 20
        return desconto, desc

def INSS(salario):
    desconto = (salario * (10/100))
    return desconto

def FGTS(salario):
    desconto = salario * (11/100)
    return desconto

def descontos(Ir, Inss):
    desc = Ir + Inss
    return desc