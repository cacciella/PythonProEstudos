#  Parâmetros de Função

def ola(nome):
    return f'Olá!! {nome}'   # f string
ola('Mauricio')
print(ola('Mauricio'))

def oOpa(nome):
    return f'Olaaaa{nome}'
print(oOpa(' Eduardo'))


def ola(nome, sobrenome):
    return f'Olá!!! {nome} {sobrenome}'
print(ola('Mau', 'Ricio'))

# deixar um item como padrão

def ola(nome, sobrenome='Padrão'):
    return f'Olaaaa {nome} e {sobrenome}'
print(ola('Mauricio'))

def ola(nome, sobrenome, idade=47):
    return f'Olaaa!! {nome} com:{idade}anos e {sobrenome}'
print('Mauricio')
