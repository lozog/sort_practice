def mergesort(arr):
	if (len(arr) > 1):
		m = len(arr)//2
		left = arr[:m]
		right = arr[m:]

		mergesort(left)
		mergesort(right)

		# now merge
		
		i = 0
		j = 0
		k = 0 # index of the first yet-unsorted element

		while (i < len(left)) and (j < len(right)):
			if (left[i] < right[j]):
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		# at this point, we've put the elements from left or right into their correct positions
		# so now copy over the rest of the remaining half (which is already sorted)

		while (i < len(left)):
			arr[k] = left[i]
			i += 1
			k += 1

		while (j < len(right)):
			arr[k] = right[j]
			j += 1
			k += 1

listA = [1, -1, 0, 400, 400000000, 180, 130.312, 3.14159, 0.00]
mergesort(listA)
print(listA)
