def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def classificacao(res):
    res = int(res)
    if res % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
def positivo_or_not(res):
    res = float(res)
    if res >= 0:
        return 'Positivo'
    else:
        return 'Negativo'

def decimal_or_not(res):
    try:
        res = float(res)
        if res % 1 == 0:
            return 'Inteiro'
        else:
            return 'Decimal'
    except:
        return 'Decimal'
    
        