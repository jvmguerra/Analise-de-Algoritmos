import math

@profile
def intercala(A,p,q,r):
	for i in range(p,(q+1)):
		B[i] = A[i]
	for j in range(q+1,(r+1)):
		B[r+q+1-j] = A[j]

	i = p
	j = r

	for k in range (p,(r+1)):
		if(B[i] <= B[j]):
			A[k] = B[i]
			i = i+1
		else:
			A[k] = B[j]
			j = j-1



def mergeSort(A,esquerda,direita):
	if(esquerda<direita):
		meio = math.floor((esquerda+direita)/2)
		mergeSort(A,esquerda,meio)
		mergeSort(A,meio+1,direita)
		intercala(A,esquerda,meio,direita)

A = [3,20,52,2,54,23,17,18,1,4]
#Para criar uma lista preenchida com 0's e que possua tamanho de A basta
B = [0]*len(A)
mergeSort(A,0,9)
print(A)
