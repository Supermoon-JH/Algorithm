def binary_search(data, search):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == search:
            return True
        elif data[mid] < search:
            left += mid + 1
        else:
            right = mid - 1

    return False
        
print(binary_search([3, 4, 6, 7], 6))