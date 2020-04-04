#  ver aula 15 e 16

import matematica.mat
print(matematica.mat.soma(4, 5))

print(' -' *15)
#      ----    ou outra opção   ---
from matematica import mat
print(mat.soma(4,5))


print(' -' *15)
#       -----     ou outra opção   ----
from matematica.mat import soma
print(soma(4,5))


print(' -' *15)
#       -----     ou outra opção  usando um apelido    as "s"   para abreviar  ----
from matematica.mat import soma as s
print(s(4,5))


