# Selection Sort:

def selection_sort(array):
    
    # itereation in whole
    for i in range(len(array)):
        min_index = i

        # checking for the minimum element index 
        # and swapping to the exact position

        for j in range(i+1 , len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


# driver code
array = [1, 9, 0, 7, 4, 5, 8, 10, 2, 3, 6]
selection_sort(array)
print(array)