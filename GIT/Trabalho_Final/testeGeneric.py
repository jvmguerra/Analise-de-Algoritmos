##adicionei - Serve para importar arquivos em outro diretório

import sys
sys.path.append('/home/gmarson/Git/AnaliseDeAlgoritmos/Trabalho_Final/Codigos/Bubble')

from monitor import *


from BubbleSort import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="número de elementos no vetor de teste")
args = parser.parse_args()

v = criavet(args.n)
bubble_sort(v)



## A EXECUÇÃO DESSE ARQUIVO EH ASSIM
## NA LINHA DE COMANDO VC MANDA O NOME DO ARQUIVO E O TAMANHO DO ELEMNTO DO vetor
##EXEMPLO testeBubble.py 10
##ele gera um vetor aleatório (criavet) e manda pro bubble_sort
