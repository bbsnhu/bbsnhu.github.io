def partition(list, low, high):
    i = (low-1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)


def quickSort(list, low, high):
    if low < high:
        part = partition(list, low, high)
        # Recursively calls itself to continue
        # partitioning
        quickSort(list, low, part-1)
        quickSort(list, part+1, high)
