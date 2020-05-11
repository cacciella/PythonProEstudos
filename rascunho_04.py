# Contagem de Caracteres com Dicionário
# print()
#
# def contar_carter(s):
#     resultado = {}
#     for caracter in s:
#         resultado[caracter] = resultado.get(caracter, 0) + 1
#     return resultado
#
# if __name__ == '__main__':
#     print(contar_carter('Nooviiiiinho'))
#     print()




print()
print()
# Contagem de Caracteres com Lista

# n = 'Nome'
# for i in range(len(n)):
#     print(f'{i} : {n[i]}')

print()
print()

# nome3 = 'Novinho'
# for i in range(len(nome3)):
#     print(f'{i} recebe {nome3[i]}')

# alimenyo = 'Banana, Limão e Laranja'
# for i in range(len(alimenyo)):
#     print(i, alimenyo[i])
#     print(f'{i}, faz muito bem {alimenyo[i]} ')
#

numero4 = 'setenta e oito'
for i in range(1, 79):
    print(i, numero4)

for i in range(len(numero4)):
    print(i, numero4[i])

#          Antes usava este metodo:
lst = []
for i in range(10):
    lst.append(str(i))
print(lst)

#          Agora uso este metodo:
print([str(i) for i in range(10)])

print([int(i) for i in range(10)])
