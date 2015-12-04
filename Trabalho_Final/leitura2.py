def leia_lprof(arq,nlin):
    fh = open(arq,encoding='utf-8')
    num_linha = 0
    linhas = fh.readlines()
    fh.close()
    n = int(linhas[0].split()[2])
    unidade_tempo = float(linhas[2].split()[2])
    tempo_total = float(linhas[4].split()[2])
    lcomp = linhas[nlin].split()
    num_comps = int(lcomp[1])
    return (n,num_comps, tempo_total)

