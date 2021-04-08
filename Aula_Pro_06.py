#  Lista  e  Range

print([1, 2, 3])
print(type([]))
lista = list(range(21))
print(lista)
lista = list(range(1, 16))
print(lista)

lista = list(range(2, 10, 2))  # exemplo: pulando de 2 em 2
print(lista)
lista = list(range(10, 2, -2))
print(lista)

print('  -=  ' *10)
print(dir(lista))

print('   -=  ' *5)
# ordenar os elementos da lista - sort
lista = list(range(10))
print(lista.sort())
print(lista)

print('   -=  ' *5)
# inserir um elemento na lista - append
print(lista.append(12))
print(lista)

print('   -=  ' *5)
# remover elementos na lista - pop
print(lista.pop(2))
print(lista)

# inserir mais de um elemento na lista - extend
# print(lista.extend(19, 63, 85))
print(lista)

# ou para inserir mais , tambem pode ser...
print(lista+[13, 14, 16])

lista2 = list(range(30, 40))
print((lista2 + lista))
print(sorted(lista2 + lista))

print([1, 3]*3)

# separando
print('Estamos todos no mesmo barco - Paython Pro'.split())

# adicionando
# print('Nome'.join(lista))

# dentro de uma lista pode ter diversos objetos,
#  como:  str, int, float, outras listas, booleano, etc
# [ 2, 1.45,  'Nomes', [listas2]]