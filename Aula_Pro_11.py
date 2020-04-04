#  Iteração em Dicionário

linguas = {'br': 'portugues' ,'eua':'ingles','esp':'espanhol'}
for chave in linguas:
    print(chave)
print('-'*20)
for chave in linguas.keys():
    print(chave)
print('-'*20)
for valor in linguas.values():
    print(valor)

print('-'*20)
for chave, valor in linguas.items():
    print(chave, valor)

print('-'*20)

print('---  Remover elementos   ---- ')
linguas.pop('br')
print(linguas)

print('---  outro método de remover elementos  --- ')
del linguas ['eua']
print(linguas)