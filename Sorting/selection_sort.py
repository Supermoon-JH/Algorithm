def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand

        for i in range(stand + 1, len(data)):
            if data[lowest] > data[i]:
                lowest = i

        data[lowest], data[stand] = data[stand], data[lowest]

    return data

print(selection_sort([3, 4, 2, 5, 1]))