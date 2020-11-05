# quick sort:
import random

def partition(Array,first,last): 
    pivot = first
    i = first + 1 
    for j in range(first + 1, last + 1): 

        if Array[j] <= Array[pivot]: 
            Array[i] , Array[j] = Array[j] , Array[i] 
            i = i + 1
    Array[pivot] , Array[i - 1] = Array[i - 1] , Array[pivot] 
    pivot = i - 1
    return (pivot) 

def randpivot(Array , first, last): 
    randpivot = random.randrange(first, last) 
    Array[first], Array[randpivot] = Array[randpivot], Array[first] 
    return partition(Array, first, last) 

def Quicksort(Array, first , last): 
    if(first < last): 
        pivot = randpivot(Array, first, last) 
        Quicksort(Array , first , pivot - 1) 
        Quicksort(Array, pivot + 1, last) 

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Quicksort(A, 0, len(A)- 1)
print(A)