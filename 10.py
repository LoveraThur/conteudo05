print('M - Matutino\nV - Vespertino\nN - Noturno')
print('-'*30)
turno = str(input('Digite seu turno: ')).upper()

tupla= ('M', 'V', 'N')
if turno in tupla:
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    else:
        print('Boa Noite!')
else:
    print('Valor Inválido!')