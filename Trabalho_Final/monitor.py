# Para instalar o Python 3 no Ubuntu 14 ou 15
#
# sudo apt-get install python3 python3-numpy python3-matplotlib ipython3 python3-psutil
#

from math import *
import gc
import random
import numpy as np

from tempo import *

# Vetores de teste
def troca(m,v,n): ## seleciona o nível de embaralhamento do vetor
    m = trunc(m)
    mi = (n-m)//2
    mf = (n+m)//2
    for num in range(mi,mf):
        i = np.random.randint(mi,mf)
        j = np.random.randint(mi,mf)
        #print("i= ", i, " j= ", j)
        t = v[i]
        v[i] = v[j]
        v[j] = t
    return v


def criavet(n, grau=-0.5, inf=-1000, sup=1000):
    passo = (sup - inf)/n
    if grau < 0.0:
        v = np.arange(sup, inf, -passo)
        if grau <= -1.0:
            return v
        else:
            return troca(-grau*n, v, n)
    elif grau > 0.0:
        v = np.arange(inf, sup, passo)
        if grau >= 1.0:
            return v
        else:
            return troca(grau*n, v, n)
    else:
        return np.random.randint(inf, sup, size=n)

#print(criavet(20))

#Tipo                                        grau
#aleatorio                                   0
#ordenado crescente                          1
#ordenado decresente                         -1
#parcialmente ordenado crescente             0.5
#parcialmente ordenado descrescente          -0.5


def executa(fn, v):
    gc.disable()
    with Tempo(True) as tempo:
        fn(v)
    gc.enable()
