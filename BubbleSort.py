# Bubble Sort:

def bubble_sort(array):

    #iterarion upto length -2 times
    for i in range(len(array) - 2):

        #iteratoin in whole
        for j in range(0, len(array) - 1):

            #swapping condition
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]
    
# driver code
array = [1, 9, 0, 7, 4, 5, 8, 10, 2, 3, 6]
bubble_sort(array)
print(array)