# Acesso, Tamanho - len e Fatiamento

nome = 'Mauricio'
print(nome[0])
print(nome[1])
print(nome[2])

print(' - '*15)
# numero de elementos  -  len
print(len(nome))

# acessar o ultimo caracter deste elemento
print(nome[len(nome) -1])
# ou
print(nome[-1]) # igual ao anterior, mas mais reduzido

print(nome[len(nome) -2])
# ou
print(nome[-2])  # igual ao anterior, mas mais reduzido

# Fatiamento
print('Fatiamento')
print(nome[-1])
print(nome[-2])
print(nome[2:-2])
print(nome[0: 3])
print(nome[3: 6])
print(nome[-2:len(nome)])
print(nome[-2:])
print(nome[:3])
