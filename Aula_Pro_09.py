#  While e For

nome = 'Mauricio'
i = 0
while i < len(nome):
    print(nome[i])
    i += 1

print(' 02 -=  For ' *8)

nome2 = 'Hello'
for v in nome2:
    print(v)

print(' 03 -=  For ' *8)
# numero de elementos  -  len
for i in range(len(nome2)):
    print(i, nome2[i])


print(' 04 -=  For ' *8)
for i, v in enumerate(nome2):
    print(i, v)
