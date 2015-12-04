def leia_tempo(arq,nlin):
    fh = open(arq,encoding='utf-8')
    num_linha = 0
    linhas = fh.readlines()
    fh.close()
    n = int(linhas[0].split()[2])
    unidade_tempo = float(linhas[2].split()[2])
    tempo_total = float(linhas[4].split()[2])
    lcomp = linhas[nlin].split()
    num_comps = int(lcomp[1])
    print('{:>7} {:>7} {:13.6f}'.format(n, num_comps, tempo_total))
    return (n, num_comps, tempo_total)

def leia_memoria(arq,nlin):
    fh = open(arq,encoding='utf-8')
    num_linha = 0
    linhas = fh.readlines()
    fh.close()
    n = int(linhas[0].split()[2])
    lcomp = linhas[nlin].split()
    mem_usada = float(lcomp[1])
    incremento = float(lcomp[3])
    print('{:>7} {:11.3f} {:11.3f}'.format(n, mem_usada, incremento))    
    return (n, mem_usada, incremento)
