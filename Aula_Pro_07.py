# Tupla e Id  ( a tupla, ao contrario da lista, é imutável, ou seja não pode alterar )

tpl = (1,4)
print(tpl)
print(type(tpl))
print(type((6,)))
print(dir(tpl))
print(tuple(range(6)))
print(' -== ' *3)
registro = ('Mauricio', 47)
registro2 = ('Eduardo', 13)
print(registro)
print(registro2)
print(registro + registro2)

# desempacotamento do registro
nome, idade = registro
print(nome)
print(idade)

# ID - verificar a identidade de um objeto
print(id(registro))
print(id(registro2))
