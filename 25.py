print('-'*30)
print('Crime'.center(30))
print('-'*30)

respostas = ('S', 'N')

cont_S = 0

resp1= ''
while resp1 not in respostas:
    resp1 = str(input('Você telefonou a vítima?\n>>> ')).upper()
    if resp1 not in respostas:
        print('\033[31mRespostas válidas: "S" e "N"\033[m')
        print('-'*30)

if resp1 == 'S':
    cont_S += 1

print()
resp2 = ''
while resp2 not in respostas:
    resp2 = str(input('Você esteve no local do crime?\n>>> ')).upper()
    if resp2 not in respostas:
        print('\033[31mRespostas válidas: "S" e "N"\033[m')
        print('-'*30)

if resp2 == 'S':
    cont_S += 1

print()
resp3 = ''
while resp3 not in respostas:
    resp3 = str(input('Você mora perto da vítima?\n>>> ')).upper()
    if resp3 not in respostas:
        print('\033[31mRespostas válidas: "S" e "N"\033[m')
        print('-'*30)

if resp3 == 'S':
    cont_S += 1

print()
resp4 = ''
while resp4 not in respostas:
    resp4 = str(input('Você devia[R$] para a vítima?\n>>> ')).upper()
    if resp4 not in respostas:
        print('\033[31mRespostas válidas: "S" e "N"\033[m')
        print('-'*30)

if resp4 == 'S':
    cont_S += 1

print()
resp5 = ''
while resp5 not in respostas:
    resp5 = str(input('Você já trabalhou com a vítima?\n>>> ')).upper()
    if resp5 not in respostas:
        print('\033[31mRespostas válidas: "S" e "N"\033[m')
        print('-'*30)

if resp5 == 'S':
    cont_S += 1

def participacao():
    if cont_S == 1:
        print('Você \033[32mNÃO é SUSPEITO\033[m')
    elif cont_S == 2:
        print('Você é \033[33mSUSPEITO!\033[m ')
    elif cont_S > 2 and cont_S <= 4:
        print('Você é \033[33mCUMPLICE!\033[m')
    else:
        print('Você é o \033[31mASSASSINO!\033[m')

participacao()