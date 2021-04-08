# Contagem de Caracteres com Dicionário

def contar_caracteres(s):
    """ Função que conta os caracteres de uma string
    Ex:
    >> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1,}
    >> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    resultado = {}

# resultado mais simplifacado que o anterior

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))


print()
print()

def contar_carac(s):
    result = {}
    for caract in s:
        result[caract] = result.get(caract, 0) + 1
    return result

if __name__ == '__main__':
    print(contar_carac('Mauricio'))
    print(contar_carac('Maaaaaaaaaaau'))




