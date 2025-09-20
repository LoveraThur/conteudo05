def valida_triangulo(a=0, b=0, c=0):
    if a + b > c and a + c > b and c + b > a:
        print('Com estes valores, \033[32;1mÉ\033[m possivel formar um triangulo')
        return True
    else:
        print('Com estes valores, \033[31;1mNÃO\033[m é possivel formar um triângulo')
        return False

def classificacao(a, b, c):
    if a != b != c:
        print('Este é um triângulo \033[33mEscaleno\033[m')
    elif a == b and a == c and b == c:
        print('Este é um triângulo \033[33mEquilátero\033[m')
    elif a == b or a == c or b == c:
        print('Este é um triângulo \033[33mIsósceles\033[m')
