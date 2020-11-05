# Merge Sort:
def Merge(array, start, mid, end):
    i = start
    j = start
    m = mid + 1

    temp = [0]*(end - start + 1)
    k = 0

    while j <= end:

        if i > mid:
            temp[k] = array[m]
            m += 1
        
        elif m > end:
            temp[k] = array[i]
            m += 1
        
        elif array[i] < array[m]:
            temp[k] = array[i]
            i += 1

        else:
            temp[k] = array[m]
            m += 1
        
        k += 1
        j += 1
    
    flag = 0
    while flag < k:
        array[start] = temp[flag]
        start += 1
        flag += 1

def merge_sort(array, start, end):
    
    if start < end:
        mid = (start + end) // 2

        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        Merge(array, start, mid , end)
    else:
        return
