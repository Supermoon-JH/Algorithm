def quicksort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 4, 2, 5, 1]))