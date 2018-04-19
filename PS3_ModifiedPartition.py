# Scratch random partitioner to test collection of duplicate entries

import sys

def partition(A, p, r):
	pivot = A[r]

	i = p

	for j in range(p, r):
		if A[j] <= pivot:
			temp1 = A[j]
			temp2 = A[i]
			A[i] = temp1
			A[j] = temp2
			i = i+1
	temp1 = A[i]
	temp2 = A[r]
	A[i] = temp2
	A[r] = temp1

	return i

def mod_partition(A, p, r):
	pivot = A[r]

	i = p
	q = r
	t = r

	for j in range(p, r):
		if A[j] <= pivot:
			temp1 = A[j]
			temp2 = A[i]
			A[i] = temp1
			A[j] = temp2
			i = i+1
		if A[j-1] == A[j]:
			if A[q] != A[j]:
				q = j - 1
			t = j
			j = j + 1
	temp1 = A[i]
	temp2 = A[r]
	A[i] = temp2
	A[r] = temp1

	R = [q,t]

	return R

if __name__ == "__main__":
	# A = [2,2,2,2,2,2,2,2]
	# print('index ', partition(A, 0, 7))
	# print(A)

	print("All Same:")
	A = [2,2,2,2,2,2,2,2]
	ret = mod_partition(A, 0, 7)
	print(A)
	print(ret)

	print("None Same:")
	A = [1,5,7,23,3,76,1,-5]
	ret = mod_partition(A, 0, 7)
	print(A)
	print(ret)
