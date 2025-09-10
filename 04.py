vogal = ['a', 'e', 'i', 'o', 'u' ]

while True:
    letra = str(input('Digite uma letra: '))

    if len(letra) > 1:
        print('\033[31mVocê deve digitar apenas uma letra!\033[m')
    elif letra.isalpha():
        if letra in vogal:
            print(f'A letra {letra} é vogal!')
            break
        else:
            print(f'A letra {letra} é consoante!')
            break
    else:
        print('Eu disse uma LETRA!')
        continue