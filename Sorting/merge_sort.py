def merge(left, right):
    merged = []
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def mergesort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])

    return merge(left, right)

print(mergesort([3, 4, 2, 5, 1]))