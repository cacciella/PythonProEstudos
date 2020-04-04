# Lista e Range

print([1, 2, 3])
print(type([]))
lista = list(range(10))
print(lista)
lista = list(range(1, 10))
print(lista)
lista = list(range(2, 10, 2))
print(lista)
lista = list(range(10, 2, -2))
print(lista)

print('  -=  ' *10)
print(dir(lista))

# ordenar os elementos da lista - sort
lista = list(range(10))
print(lista.sort())
print(lista)

# inserir um elemento na lista - append
print(lista.append(12))
print(lista)

# remover elementos na lista - pop
print(lista.pop(2))
print(lista)

# inserir mais de um elemento na lista - extend
# print(lista.extend(19, 63, 85))
print(lista)

# ou para inserir mais , tambem pode ser...
print(lista+[13, 14, 16])
print([1, 3]*3)

# separando
print('Estamos todos no mesmo barco - Paython Pro'.split())

# adicionando
# print('Nome'.join(lista))

# dentro de uma lista pode ter diversos objeots, como:  str, int, float, outras listas, booleano, etc
# [ 2, 1.45,  'Nomes', [listas2]]