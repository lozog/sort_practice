def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def partition(arr, low, high):
	# this partition function will take the last element as the pivot
	pivot = arr[high]

	i = low - 1 # index of smaller element

	for j in range(low, high):
		if (arr[j] <= pivot):
			i += 1
			swap(arr, i, j)

	swap(arr, i+1, high)
	return i+1


def quicksortHelper(arr, low, high):
	if (low < high):

		# partition index
		pi = partition(arr, low, high)

		quicksortHelper(arr, low, pi-1)
		quicksortHelper(arr, pi+1, high)


def quicksort(arr):
	quicksortHelper(arr, 0, len(arr) - 1)


listA = [1, -1, 0, 400, 400000000, 180, 130.312, 3.14159, 0.00]
quicksort(listA)
print(listA)
