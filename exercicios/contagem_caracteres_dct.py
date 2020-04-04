# Contagem de Caracteres com Dicionário
# Nesse tópico será resolvido o clássico problema de entrevistas de emprego de contagem de caracteres.

def contar_caracteres(s):
    """ Função que conta os caracteres de uma string
    Ex:
    >> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1,}
    >> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s)
    caracteres_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_anterior:
            contagem += 1
        else:
            resultado[caracteres_anterior] = contagem
            caracteres_anterior = caracter
            contagem = 1

    resultado[caracteres_anterior] = contagem
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))

