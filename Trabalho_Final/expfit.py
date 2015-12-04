import numpy as np
import matplotlib.pyplot as plt

def expfit(x,y):
    """ Ajusta os pares de pontos (xi,yi) a f(x)=ae^(bx) usando o 
        método dos minimos quadrados, com regressão linear ponderada.
        Retorna o par de coeficientes (a,b)
    """
    w2 = y * y
    somaw2 = w2.sum()
    w2x = w2 * x
    z = np.log(y)
    w2z = w2 * z
    mp_x = w2x.sum() / somaw2
    mp_z = w2z.sum() / somaw2
    b = (w2z*(x - mp_x)).sum() / (w2x*(x - mp_x)).sum()
    lna = mp_z - b*mp_x
    a = np.exp(lna)
    return (a,b)
    
    
def plota_expfit(x,y):
    a,b = expfit(x,y)
    legenda_ajuste = "${:.3f} e^{{ {:.3f} x }}$".format(a, b)
    plt.plot(x,y,"o",label="dados")
    plt.plot(x, a*np.exp(b*x),"--", label=legenda_ajuste)
    plt.legend(loc='upper left')
    plt.show()

#x = np.array([1.2,  2.8,  4.3,  5.4,   6.8,   7.9])
#y = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])
