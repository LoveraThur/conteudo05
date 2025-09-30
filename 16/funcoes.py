def menu(txt):
    tam = len(txt) + 4
    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)

def bhaskara(a=1, b=1, c=1):
    # ax2 + bx + c = 0
    if a == 0:
        return '\033[31mOs valores informados não formam função de 2º grau\033[m'
    else:
        delta = (b*b)- 4*a*c
        print(f'equação informada: \033[33;1m{a}x² + {b}x + {c}\033[m')
        if delta < 0:
            return f'O delta é \033[34m{delta}\033[m, a equação não possui raizes reais'
        elif delta == 0:
            x = -b / (2*a)
            return f'A equação possui uma raiz real \033[34mx = {x:.2f}\033[m'
        else:
            raiz = delta ** 0.5
            eq1 = (-b + raiz)/2*a
            eq2 = (-b - raiz)/2*a
            return f"A equação possui duas raizes reais: \033[34mx'= {eq1:.2f}\033[m e \033[34mx''= {eq2:.2f}\033[m"