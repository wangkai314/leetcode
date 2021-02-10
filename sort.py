def bubble_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

def quick_sort(arr):
	if len(arr) >= 2:
		mid = arr[len(arr)//2]
		left, right = [], []
		arr.remove(mid)
		for num in arr:
			if num <= mid:
				left.append(num)
			if num > mid:
				right.append(num)
		return quick_sort(left)+[mid]+quick_sort(right)
	else:
		return arr

arr1 = [2, 45, 38, 7, 6, 88, 77]
print(bubble_sort(arr1))
print(quick_sort(arr1))




