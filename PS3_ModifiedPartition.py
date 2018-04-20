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

	q = i
	t = i
	print("Initial Sort: ", A)
	print("Pivot: ", i)

	for x in range(p, i-1):
		if A[q] == pivot:
			q= q-1
		elif A[x] == pivot:
			temp1 = A[x]
			temp2 = A[q]
			A[x] = temp2
			A[q] = temp1
			q = q-1

	R = [q,t]

	return R

if __name__ == "__main__":
	# A = [2,2,2,2,2,2,2,2]
	# print('index ', partition(A, 0, 7))
	# print(A)

	print("All Same:")
	A = [2,2,2,2,2,2,2,2]
	ret = mod_partition(A, 0, 7)
	print("Final Sort: ", A)
	print(ret)
	print()

	print("All Same:")
	A = [1,7,2,22,35,2,4,-9,2,2]
	ret = mod_partition(A, 0, len(A)-1)
	print("Final Sort: ", A)
	print(ret)
	print()

	print("None Same:")
	A = [1,5,7,23,3,76,1,-5]
	ret = mod_partition(A, 0, 7)
	print("Final Sort: ", A)
	print(ret)
	print()
