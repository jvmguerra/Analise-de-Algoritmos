#@profile
def Particiona(A,p,r):
	x = A[r] #pivo é o último elemento
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1
			aux = A[i]
			A[i] = A[j]
			A[j] = aux
	temp = A[i+1]
	A[i+1] = A[r]
	A[r] = temp
	return i+1

#@profile
def quickSort(A,p=A[0],r=A[-1]):
	if(p < r):
		q = Particiona(A,p,r)
		quickSort(A,p,(q-1))
		quickSort(A,(q+1),r)

#@profile
def quick(A):
	quickSort(A,A[0],A[-1])
#A = [40, 12, 34, 1, 3, 5, 80]
#quickSort(A,0,6)
#print(A)
