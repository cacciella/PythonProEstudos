#  Parâmetros Variáveis

def soma(*args):
    print(args)
    print(type(args))
print(soma(1,4))

def soma(*args):
    aux = 0
    for valor in args:
        aux += valor
    return aux
print(soma(2,4))

print('-'*20)
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
print(f(nome = 'Mauricio', sobrenome = 'Fernandes'))

print('-'*20)
args = (2,4,10)
kwargs = {'nome': 'Renzo', 'sobrenome': 'Nuccitelli'}
def f(*args, **kwargs):
    print(args)
    print(kwargs)
print(f())
print(f(1,3, nome='Mauricio'))
print(f(args, kwargs))
print(' -- Desempacotando -- ')
print(f(*args, **kwargs))
