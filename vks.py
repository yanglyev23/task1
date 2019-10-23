import random


def mymax(arr):
    m = arr[0]
    for i in range(len(arr)):
        if arr[i] > m:
            m = arr[i]
            im = i
    return im


n = random.randint(0, 10)
array = [0]*n
for j in range(n):
    array[j] = random.randint(0, 100)
print(array)
print(mymax(array))
