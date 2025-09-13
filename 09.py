lista = []

num1 = int(input('Digite o primeiro valor: '))
lista.append(num1)
num2 = int(input('Digite o segundo valor: '))
lista.append(num2)
num3 = int(input('Digite o terceiro valor: '))
lista.append(num3)
lista.sort(reverse=True)
print(f'Você digitou os valores {lista}')
