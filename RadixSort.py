import random
import time

array = [random.randrange(1,1000) for _ in range(1000)]
minList = min(array)
startTime = time.time()
k = 0
while minList != array[0]:
    bin = [[],[],[],[],[],[],[],[],[],[]]
    for number in array:
        ref = (number // 10 ** k) % 10
        bin[ref].append(number)
    l=0
    for i in bin:
        for j in i:
            array[l]=j
            l+=1
    k+=1    
duration = time.time() - startTime
print("-------DURATIONS-------: ",duration)
# print(array)
print("-----------------------")