a = (input('Digite o seu número binário'))
lista = list(a)
index = 0

for letra in lista:
    if letra == '0':
        lista[index] = '1'
    else:
        lista[index] = '0'
    index = index + 1

numero = " ".join(lista)
print(numero)
print(type(numero))