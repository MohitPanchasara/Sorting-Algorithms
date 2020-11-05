# counting sort

def counting_sort(array):
    size = len(array)
    #finding max in array
    temp = max(array)

    # count array with all elements 0 and size of temp + 1
    Count = (temp + 1) * [0]

    # final array with all elements 0 and size equal to length of input array
    Final = size * [0]

    for i in array:
        Count[i] += 1

    k = 1
    while k <= temp:
        Count[k] = Count[k] + Count[k-1]
        k += 1
    
    for i in range(size - 1, -1, -1):
        Final[Count[array[i]] - 1] = array[i]
        Count[array[i]] -= 1
    
    #Updates the given array
    for i in range(size):
        array[i] = Final[i]
       
