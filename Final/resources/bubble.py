def bubbleSort(list):
    i = len(list)

    for j in range(i):

        for k in range(0, i-j-1):
            if list[k] > list[k+1]:
                list[k], list[k+1] = list[k+1], list[k]

    return list
