# Contagem de Caracteres com Dicionário
print()

def contar_carter(s):
    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

if __name__ == '__main__':
    print(contar_carter('Nooviiiiinho'))
    print()



print()
print()
# Contagem de Caracteres com Lista

n = 'Nome'
for i in range(len(n)):
    print(f'{i} : {n[i]}')

print()
print()

nome3 = 'Novinho'
for i in range(len(nome3)):
    print(f'{i} recebe {nome3[i]}')

