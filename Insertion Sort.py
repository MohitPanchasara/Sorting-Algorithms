# Insertion Sort:

def insertion_sort(array):

    #iteration in whole
    for i in range(len(array) - 1):

        # checking the previous element with current element
        # and swapping if current is less than previous
        j = i
        while(j >= 0):
            if(array[j+1] < array[j]):
                array[j+1], array[j] = array[j], array[j+1]
            j -= 1

#driver code
array = [1, 9, 0, 7, 4, 5, 8, 10, 2, 3, 6]
insertion_sort(array)
print(array)