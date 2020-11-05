# Build Heap
# Heap Inserton
# Heap Deletion
# Heap Sort

import time
import random

def Swap(Heap , i , j):
    Heap[i] , Heap[j] = Heap[j] , Heap[i]

def heapify(Heap, n, i): 
    largest = i  
    left_child = 2 * i + 1    
    right_child = 2 * i + 2   
    if left_child < n and Heap[i] < Heap[left_child]: 
        largest = left_child 

    if right_child < n and Heap[largest] < Heap[right_child]: 
        largest = right_child 

    if largest != i: 
        Swap(Heap , largest , i)
        heapify(Heap, n, largest) 

def delete_root(Heap , size):
    element = Heap[0]
    Heap[0] = Heap[size - 1]
    heapify(Heap , size - 1 , 0)
    return element 

def Heap_Sort(Heap):
    size = len(Heap)
    for i in range ((size // 2) - 1 , -1 , -1):
        heapify(Heap , size , i)

    for i in range (size - 1 , 0 , -1):
        Swap(Heap , 0 , i)
        heapify(Heap , i , 0)

def Heapify_One_element(Heap , size , i):
    parent = int((i - 1) / 2)
    S = int(i)
    
    if Heap[S] > Heap[parent]:
        Swap(Heap , parent , S)
        Heapify_One_element(Heap , size , parent)

def Insert_Node(Heap , size , key):
    Heap.append(key)
    Heapify_One_element(Heap , size , size)

        
# driver code to run program
Heap = []
#initially a empty array/list is created

#INSERTION OF EACH ELEMENT
time_Insertion_1 = time.time()
#start time
for i in range(1 , 2001):
    Insert_Node(Heap, len(Heap) , i)
    #inserts each element and heapify simultaneously
time_Insertion_2 = time.time()
#end time
print("The time taken for running the insertion of heap element one by one :")
#runtime in seconds and microseconds
print(f"{time_Insertion_2 - time_Insertion_1} seconds")
print("-------------------------------------------------------------------------")

#DELETION OF ROOT
time_Insertion_1 = time.time()
#start time of deletion
print("Time Taken in perfoming the deetion of root operation :")
p = delete_root(Heap , len(Heap)) 
time_Insertion_2 = time.time()
#endtime
#runtime in seconds and microseconds
print(f"{time_Insertion_2 - time_Insertion_1} seconds")
print("-------------------------------------------------------------------------")

#HEAP SORT
time_Insertion_1 = time.time()
#start time
print("Time taken in perfoming the Heap sort algorithm :")
Heap_Sort(Heap) 
time_Insertion_2 = time.time()
#end time
#runtime in seconds and microseconds
print(f"{time_Insertion_2 - time_Insertion_1} seconds")