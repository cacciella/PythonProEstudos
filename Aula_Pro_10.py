# Dicionários {}  /Mapas

linguas = {'br':'portugues','eua':'ingles'}
print(type(linguas))
print(linguas)
#caso nao tenha definido....
print(linguas.get('esp', 'nao definido'))
print(linguas.get('br', 'nao definido'))
print('br' in linguas)
print('esp' in linguas)

print('  -=   ' *8)
#  outro exemplo
print(6 in range(10))
print(11 in range(10))

# adcionar um novo elemento no dicionário
linguas['esp'] = 'espanhol'
print(linguas ['esp'])
print(linguas)