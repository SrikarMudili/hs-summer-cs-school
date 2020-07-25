def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				a[j], A[j+1] = A[j+1], A[j]
			else:
				break

A = [7,8,5,4,9,2]
insertion_sort1(A)
print(A)