import subprocess
import numpy as np
import matplotlib.pyplot as plt


def executa_teste(arqteste, arqsaida, nlin, intervalo):
    """Executa uma sequência de testes contidos em arqteste, com:
       arqsaida: nome do arquivo de saída, ex: tBolha.dat
       nlin: número da linha no arquivo gerado pelo line_profiler contendo
             os dados de interesse. Ex: 14
       intervalo: tamanhos dos vetores: Ex: 2 ** np.arange(5,10)
    """
    f = open(arqsaida,mode='w', encoding='utf-8')
    f.write('#      n   comparações      tempo(s)\n')

    for n in intervalo:
        cmd = ' '.join(["kernprof -l -v", "testeBubble.py", str(n)])
        str_saida = subprocess.check_output(cmd, shell=True).decode('utf-8')
        linhas = str_saida.split('\n')
        unidade_tempo = float(linhas[1].split()[2])
        tempo_total = float(linhas[3].split()[2])
        lcomp = linhas[nlin].split()
        num_comps = int(lcomp[1])
        str_res = '{:>8} {:>13} {:13.6f}'.format(n, num_comps, tempo_total)
        print(str_res)
        f.write(str_res + '\n')
    f.close()

# executa_teste("testeBubble.py", "tBolha.dat", 14, 2 ** np.arange(5,10))

def plota_teste1(arqsaida):
    n, c, t = np.loadtxt(arqsaida, unpack=True)
    plt.plot(n, n ** 2, label='$n^2$')
    plt.plot(n, c, 'ro', label='bubble sort')

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Posiciona o título
    plt.title('Análise da complexidade de \ntempo do método da bolha')

    # Rotula os eixos
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Número de comparações')

    plt.savefig('bubble1.png')
    plt.show()

def plota_teste2(arqsaida):
    n, c, t = np.loadtxt(arqsaida, unpack=True)
    plt.plot(n, n ** 2, label='$n^2$')
    plt.plot(n, t, 'ro', label='bubble sort')

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Posiciona o título
    plt.title('Análise da complexidade de \ntempo do método da bolha')

    # Rotula os eixos
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Tempo(s)')

    plt.savefig('bubble2.png')
    plt.show()

def plota_teste3(arqsaida):
    n, c, t = np.loadtxt(arqsaida, unpack=True)

    # Calcula os coeficientes de um ajuste a um polinômio de grau 2 usando
    # o método dos mínimos quadrados
    coefs = np.polyfit(n, t, 2)
    p = np.poly1d(coefs)

    plt.plot(n, p(n), label='$n^2$')
    plt.plot(n, t, 'ro', label='bubble sort')

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Posiciona o título
    plt.title('Análise da complexidade de \ntempo do método da bolha')

    # Rotula os eixos
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Tempo(s)')

    plt.savefig('bubble3.png')
    plt.show()

def plota_teste4(arqsaida):
    n, c, t = np.loadtxt(arqsaida, unpack=True)

    # Calcula os coeficientes de um ajuste a um polinômio de grau 2 usando
    # o método dos mínimos quadrados
    coefs = np.polyfit(n, c, 2)
    p = np.poly1d(coefs)

    plt.plot(n, p(n), label='$n^2$')
    plt.plot(n, c, 'ro', label='bubble sort')

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Posiciona o título
    plt.title('Análise da complexidade de \ntempo do método da bolha')

    # Rotula os eixos
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Número de comparações')

    plt.savefig('bubble4.png')
    plt.show()

def plota_teste5(arqsaida):
    n, c, t = np.loadtxt(arqsaida, unpack=True)

    # Calcula os coeficientes de um ajuste a um polinômio de grau 2 usando
    # o método dos mínimos quadrados
    coefs = np.polyfit(n, c, 2)
    p = np.poly1d(coefs)

    # set_yscale('log')
    # set_yscale('log')
    plt.semilogy(n, p(n), label='$n^2$')
    plt.semilogy(n, c, 'ro', label='bubble sort')

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Posiciona o título
    plt.title('Análise da complexidade de \ntempo do método da bolha')

    # Rotula os eixos
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Número de comparações')

    plt.savefig('bubble5.png')
    plt.show()
