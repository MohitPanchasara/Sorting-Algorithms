# radix sort

def radix_sort_counting(array, size, pos):

    temp = max(array)

    Count = (10) * [0]
    Final = size*[0]

    for i in array:
        Count[(i // pos) % 10] += 1

    k = 1
    while k <10:
        Count[k] += Count[k - 1]
        k += 1

    for i in range(size - 1, -1, -1):
        Final[Count[(array[i] // pos) % 10] - 1] = array[i]
        Count[(array[i] // pos) % 10] -= 1
    
    for i in range(size):
        array[i] = Final[i]

def radix_sort(array):
    temp = max(array)
    exp = 1
    while temp // exp > 0:
        radix_sort_counting(array, len(array), exp)
        exp *= 10