def leia(arq):
    fh = open(arq,encoding='utf-8')
    num_linha = 0
    for linha in fh:
        num_linha += 1
        print('{:>4} {}'.format(num_linha, linha.rstrip()))
    fh.close()
