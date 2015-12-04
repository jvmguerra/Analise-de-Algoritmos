import numpy as np
import matplotlib.pyplot as plt
# Ajuste os dados à função exponencial f(x) = ae^(bx)

x = np.array([1.2,  2.8,  4.3,  5.4,   6.8,   7.9])
y = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])

z = np.log(y)

# Ajuste
# Calcula os coeficientes b e c de F(x) = ln f(x) = bx + c, com c = ln a
coefs = np.polyfit(x,z,1) 
f = np.poly1d(coefs)

legenda_ajuste = "${:.3f} e^{{ {:.3f} x }}$".format(np.exp(coefs[1]), coefs[0])
plt.plot(x,y,"o",label="dados")
plt.plot(x, np.exp(f(x)),"--", label=legenda_ajuste)
plt.legend(loc='upper left')
plt.show()
