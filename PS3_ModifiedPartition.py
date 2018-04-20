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
	z = p

	for j in range(p, r):
		if A[j] == pivot:
			temp = A[j] # Swap A[z] with A[j]
			A[j] = A[z]
			A[z] = temp

			z += 1
		elif A[j] < pivot:
			temp = A[j] # Swap A[j] with A[z]
			A[j] = A[z]
			A[z] = temp

			temp = A[i] # Swap A[z] with A[i]
			A[i] = A[z]
			A[z] = temp

			z += 1
			i += 1

	# Final Swap:
	temp = A[z] # Swap A[r] with A[z]
	A[z] = A[r]
	A[r] = temp

	R = [i,z]

	return R

if __name__ == "__main__":
	# A = [2,2,2,2,2,2,2,2]
	# print('index ', partition(A, 0, 7))
	# print(A)

	A = [2,2,2,2,2,2,2,2]
	ret = mod_partition(A, 0, len(A)-1)
	print("Final Sort: ", A)
	print(ret)
	print()

	A = [1,7,2,22,35,2,4,-9,2,2]
	ret = mod_partition(A, 0, len(A)-1)
	print("Final Sort: ", A)
	print(ret)
	print()

	A = [1,5,7,23,3,76,1,-5]
	ret = mod_partition(A, 0, len(A)-1)
	print("Final Sort: ", A)
	print(ret)
	print()

	A = [10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,5]
	ret = mod_partition(A, 0, len(A)-1)
	print("Final Sort: ", A)
	print(ret)
	print()
