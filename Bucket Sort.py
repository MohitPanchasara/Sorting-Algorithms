# bucket sort using quick sort
import random

'''quicksort program'''

def partition(A , F , L):
    pivot = F
    i = F + 1
    for j in range(F + 1 , L + 1):

        if A[j] <= A[pivot]:
            A[i] , A[j] = A[j] , A[i]
            i += 1

    A[pivot] , A[i-1] = A[i-1] , A[pivot]
    pivot = i - 1
    return pivot

#random pivot generator
def randpivot(A , F , L):
    randpivot = random.randrange(F , L)
    A[F] , A [randpivot] = A[randpivot] , A[F]
    return partition(A , F , L)

def Quicksort(A , F , L):
    if (F < L):
        pivot = randpivot(A , F , L)
        Quicksort(A , F , pivot - 1)
        Quicksort(A , pivot + 1 , L)

    return A

'''bucket sort program using quicksort'''

def bucket_sort(A):
    array = []
    Bucket_num = 10

    #2D array, containing 10 buckets/array
    for i in range(Bucket_num):
        array.append([])

    #creating index of particular bucket
    #and appending that value in bucket simultaneously
    for temp in A:
        Bucket_index = int(Bucket_num * temp)
        array[Bucket_index].append(temp)

    #quicksort to solve each bucket
    for i in range(Bucket_num):
        array[i] = Quicksort(array[i] , 0 , len(array[i]) - 1)
    
    #Updating the given array to sorted array
    k = 0
    for i in array:
        for j in i:
            A[k] = j
            k += 1
    return A

#driver code
A = []

for i in range(10):
    A.append(round(random.uniform(0 , 1) , 4))
bucket_sort(A)
print(A)
