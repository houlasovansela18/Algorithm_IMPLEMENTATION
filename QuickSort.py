import random
import time
array = [random.randrange(1,1000) for _ in range(1000)]

startTime = time.time()
start = 0
end = len(array) - 1
call = 0

def partition(array,start,end):
    pivot = array[end]
    partitionIndex = start
    for i in range(start,end):
        if array[i] <= pivot:
            array[i],array[partitionIndex] = array[partitionIndex],array[i]
            partitionIndex += 1
    array[end],array[partitionIndex] = array[partitionIndex],array[end]
    return partitionIndex

def QuickSort(array,start,end):
    if start < end:
        # print(array)
        partitionIndex = partition(array,start,end)
        QuickSort(array,start,partitionIndex - 1)
        QuickSort(array,partitionIndex + 1,end)

QuickSort(array,start,end)
duration = time.time() - startTime
print("-------DURATIONS-------: ",duration)
print("-----------------------")